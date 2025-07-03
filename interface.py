import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json

from scr.main import matcli
from scr.extract_html import divisiontext
from scr.extract_CRM_portfolio import json_file
from scr.extract_CRM_portfolio import count_sections_in_json
from scr.extract_CRM_portfolio import prompt_association
from scr.extract_CRM_portfolio import associate_titles_with_clients
from scr.extract_CRM_portfolio import prompt_final

class DragDropApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Traitement Portefeuille Clients")
        self.master.geometry("900x700")

        self.html_path = None
        self.xlsx_path = None
        self.text_zones = []

        self.html_label = tk.Label(master, text="Aucun fichier HTML sélectionné", fg="blue")
        self.xlsx_label = tk.Label(master, text="Aucun fichier Excel sélectionné", fg="blue")
        self.html_label.pack(pady=10)
        self.xlsx_label.pack(pady=10)

        self.html_button = tk.Button(master, text="Sélectionner le fichier HTML", command=self.select_html)
        self.html_button.pack(pady=5)
        self.xlsx_button = tk.Button(master, text="Sélectionner le fichier Excel", command=self.select_xlsx)
        self.xlsx_button.pack(pady=5)

        self.process_button = tk.Button(master, text="Lancer le traitement", command=self.process_files, state=tk.DISABLED)
        self.process_button.pack(pady=20)

        # Scrollable sections area
        self.sections_canvas = tk.Canvas(master, height=400)
        self.sections_scrollbar = tk.Scrollbar(master, orient="vertical", command=self.sections_canvas.yview)
        self.sections_frame = tk.Frame(self.sections_canvas)

        self.sections_frame.bind(
            "<Configure>",
            lambda e: self.sections_canvas.configure(
                scrollregion=self.sections_canvas.bbox("all")
            )
        )

        self.sections_canvas.create_window((0, 0), window=self.sections_frame, anchor="nw")
        self.sections_canvas.configure(yscrollcommand=self.sections_scrollbar.set)

        self.sections_canvas.pack(side="left", fill="both", expand=True)
        self.sections_scrollbar.pack(side="right", fill="y")

    def select_html(self):
        filename = filedialog.askopenfilename(
            title="Sélectionner le fichier HTML",
            filetypes=[("Fichiers HTML", "*.html *.htm")]
        )
        if filename:
            self.html_path = filename
            self.html_label.config(text=os.path.basename(filename))
            self.check_ready()

    def select_xlsx(self):
        filename = filedialog.askopenfilename(
            title="Sélectionner le fichier Excel",
            filetypes=[("Fichiers Excel", "*.xlsx *.xls")]
        )
        if filename:
            self.xlsx_path = filename
            self.xlsx_label.config(text=os.path.basename(filename))
            self.check_ready()

    def check_ready(self):
        if self.html_path and self.xlsx_path:
            self.process_button.config(state=tk.NORMAL)

    def copy_to_clipboard(self, text):
        self.master.clipboard_clear()
        self.master.clipboard_append(text)
        from tkinter import messagebox
        messagebox.showinfo("Copié", "Le prompt a été copié dans le presse-papier.")

    titres = ['BHP ( Market-Perform vs Outperform, TP 1900p vs 2000p)',
              'Défense',
              'Telco France',
              'Eco Australie',
              'Eco Chine',
              'Centrica (=)',
              'Equinor (+)',
              'Kering (=)',
              'Vodafone (=)',
              'Land Securities',
              'Aramis (=/+)',
              'H&M (Underperform, TP: 110SEK)',
              'Conviction Thinking',
              'Equity Strategy',
              'Covered Bonds Special',
              'Credit Strategy Weekly Webcast – Can you spell insatiable?',
              'Credit Strategy Weekly Webcast',
              'EM Trade Idea Monitor - SG EM Trade Idea Monitor',
              'Fixed Income Portfolio Strategy',
              'Technical Analysis: 10y UST',
              'Diageo',
              'Emeis',
              'Electric Revolution: Divergence — From Centralized Energy to Portable Power — Powering the Sustainable',
              'Global Trucks: Pair trade - Long PACCAR',
              'Porsche (04/06)',
              'BMW (26/06)']

    def process_all_text_zones(self):
        # General list to accumulate all lists
        all_lists = []
        # List to accumulate all summaries
        all_summaries = []

        for text_zone in self.text_zones:
            user_text = text_zone.get("1.0", "end").strip()
            the_list, the_summary = divisiontext(user_text)
            all_lists.append(the_list)
            all_summaries.append(the_summary)

        # Save to a JSON file
        output_data = {
            "all_lists": all_lists,
            "all_summaries": all_summaries
        }
        with open("data/results_processed.json", "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        # Optional: Show a confirmation dialog
        from tkinter import messagebox
        messagebox.showinfo("Succès", "Les résultats ont été enregistrés dans results_processed.json !")


    def on_generate_prompt(self):
        # Check file existence
        if not os.path.exists("data/results_processed.json"):
            messagebox.showerror("Erreur", "Le fichier results_processed.json n'existe pas encore.")
            return
        if not os.path.exists("data/newsletter_md.md"):
            messagebox.showerror("Erreur", "Le fichier newsletter_md.md n'existe pas.")
            return
        try:
            prompt = prompt_final(self.titres, "data/results_processed.json", "../data/newsletter_md.md")
            self.copy_to_clipboard(prompt)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la génération du prompt:\n{e}")

    def process_files(self):
        # 1. Show message about file processing
        messagebox.showinfo(
            "Traitement",
            f"HTML: {self.html_path}\nExcel: {self.xlsx_path}\nTraitement à lancer ici..."
        )

        # 2. Process files and create data
        matrix_client_events = matcli(self.html_path)
        json_file('ROLLAND JEAN-MARC', self.xlsx_path)
        print(matrix_client_events)
        nbr_section = count_sections_in_json('data/clients_sections.json')

        # 3. CLEAR the interface (remove previous section widgets)
        for widget in self.sections_frame.winfo_children():
            widget.destroy()
        self.text_zones = []

        # 4. Dynamically create buttons and text zones for each section
        for i in range(nbr_section):
            # TODO: Replace with logic to generate your prompt text for section i
            prompt_text = prompt_association(['BHP ( Market-Perform vs Outperform, TP 1900p vs 2000p)',
              'Défense',
              'Telco France',
              'Eco Australie',
              'Eco Chine',
              'Centrica (=)',
              'Equinor (+)',
              'Kering (=)',
              'Vodafone (=)',
              'Land Securities',
              'Aramis (=/+)',
              'H&M (Underperform, TP: 110SEK)',
              'Conviction Thinking',
              'Equity Strategy',
              'Covered Bonds Special',
              'Credit Strategy Weekly Webcast – Can you spell insatiable?',
              'Credit Strategy Weekly Webcast',
              'EM Trade Idea Monitor - SG EM Trade Idea Monitor',
              'Fixed Income Portfolio Strategy',
              'Technical Analysis: 10y UST',
              'Diageo',
              'Emeis',
              'Electric Revolution: Divergence — From Centralized Energy to Portable Power — Powering the Sustainable',
              'Global Trucks: Pair trade - Long PACCAR',
              'Porsche (04/06)',
              'BMW (26/06)'], 'data/news_résume.md', i, json_path="../data/clients_sections.json")
            # Create the copy button, capture prompt_text using default argument in lambda
            button = tk.Button(
                self.sections_frame,
                text=f"Copy Section {i + 1}",
                command=lambda t=prompt_text: self.copy_to_clipboard(t)
            )
            button.pack(anchor='w', padx=10, pady=2)

            # Create the text zone for user input or comments
            text_zone = tk.Text(self.sections_frame, height=4, width=80)
            text_zone.pack(padx=20, pady=2)
            self.text_zones.append(text_zone)

        self.confirm_button = tk.Button(
            self.sections_frame,
            text="Confirmer",
            command=self.process_all_text_zones
        )
        self.confirm_button.pack(pady=20)

        #titres_client = associate_titles_with_clients("../data/results_processed.json",self.titres)

        self.generate_prompt_button = tk.Button(
            self.sections_frame,
            text="Générer le prompt",
            command=self.on_generate_prompt
        )
        self.generate_prompt_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = DragDropApp(root)
    root.mainloop()