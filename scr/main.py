from scr import extract_CRM_portfolio
import re
from scr.extract_html import get_all_events
from scr.extract_html import html_to_markdown_with_table
from scr.extract_html import remove_titles_from_html
from scr.extract_html import add_clients_after_titles

def matrix_client_events(list_events):
    return [[event, []] for event in list_events]


def add_client_in_matrice(matrix, client_num, text_file):
    """
    For each line in text_file, if the line (event) matches one in the matrix, add the client number.
    Args:
        matrix (list): Output from matrix_client_events
        client_num (int or str): Client number to add
        text_file (str): Path to the text file with event titles
    Modifies:
        matrix in-place (adds client_num where there is a match)
    """
    # Read the text file and clean up each line
    with open(text_file, "r", encoding="utf-8") as f:
        lines = [line.strip("- \n\t").strip() for line in f if line.strip()]

    # For each event in the matrix, check if it is present in the lines
    for event_row in matrix:
        event = event_row[0]
        if event in lines:
            event_row[1].append(client_num)
    return matrix

def add_clients_from_report(matrix, report_txt_path, max_event_prefix=10):
    """
    Fills the matrix (event -> clients) and collects explanations for each client.
    Returns: (matrix, explanations_list)
      explanations_list: list of (client_number, explanation_text)
    """
    # Build event map as before
    event_map = {}
    for idx, (event, _) in enumerate(matrix):
        event_prefix = event.split('-')[0][:max_event_prefix].strip().lower()
        event_map[event_prefix] = idx

    with open(report_txt_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split into blocks by client, pattern: "=== MCxxxxxxx ==="
    client_blocks = re.split(r"^===\s*(MC\d+)\s*===\s*$", text, flags=re.MULTILINE)
    # re.split alternates: ['', client1, block1, client2, block2, ...]
    explanations = []

    # Process each client block
    for i in range(1, len(client_blocks), 2):
        client_number = client_blocks[i]
        block = client_blocks[i+1]
        if not client_number or not block:
            continue

        # Split block into lines and remove empty lines
        lines = [line.strip() for line in block.strip().split('\n') if line.strip()]
        if not lines:
            continue

        # Find event lines: lines with a '-' within first 10 chars, or matching normalized event names
        event_lines = []
        explanation_start_idx = 0
        for idx, line in enumerate(lines):
            dash_pos = line.find('-')
            event_candidate = line[:dash_pos][:max_event_prefix].strip().lower() if dash_pos != -1 else ''
            if dash_pos != -1 and event_candidate in event_map:
                event_lines.append(line)
            else:
                explanation_start_idx = idx
                break

        # Add client to matrix for each detected event in event_lines
        for line in event_lines:
            dash_pos = line.find('-')
            if dash_pos == -1:
                continue
            event_candidate = line[:dash_pos][:max_event_prefix].strip().lower()
            if event_candidate in event_map:
                idx = event_map[event_candidate]
                if client_number not in matrix[idx][1]:
                    matrix[idx][1].append(client_number)

        # The explanation is everything from explanation_start_idx onward
        explanation = "\n".join(lines[explanation_start_idx:]).strip()
        if explanation and not explanation.lower().startswith("aucun"):
            explanations.append((explanation))

    return matrix, explanations

def remove_titles_from_matrix(matrice, titre_NP):
    """
    Removes any row from matrice whose first element matches a title in titre_NP.
    Args:
        matrice (list): Matrix of [title, clients] pairs.
        titre_NP (list): List of titles to remove.
    Returns:
        list: Filtered matrix.
    """
    titre_NP_set = set(titre_NP)
    return [row for row in matrice if row[0] not in titre_NP_set]



def matcli(path):
    print("matcli function is running")
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
    matrix_client_events = [[event, []] for event in titres]
    html_to_markdown_with_table(path, "data/newsletter_md.md")
    return matrix_client_events

if __name__ == "__main__":
    main('../data/newsletter.html')

