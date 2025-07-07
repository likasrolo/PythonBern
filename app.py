import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
import traceback

from scr.main import matcli
from scr.extract_html import divisiontext
from scr.extract_CRM_portfolio import json_file, count_sections_in_json, prompt_association, associate_titles_with_clients, prompt_final

app = Flask(__name__)
app.secret_key = 'newsletter_secret_key_2024'

# Configuration
UPLOAD_FOLDER = 'data'
ALLOWED_EXTENSIONS = {'html', 'htm', 'xlsx', 'xls'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Créer le dossier data s'il n'existe pas
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Titres prédéfinis (comme dans le code original)
TITRES = [
    'BHP ( Market-Perform vs Outperform, TP 1900p vs 2000p)',
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
    'BMW (26/06)'
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        # Vérifier les fichiers uploadés
        if 'html_file' not in request.files or 'excel_file' not in request.files:
            flash('Veuillez sélectionner à la fois un fichier HTML et un fichier Excel', 'error')
            return redirect(url_for('index'))
        
        html_file = request.files['html_file']
        excel_file = request.files['excel_file']
        
        if html_file.filename == '' or excel_file.filename == '':
            flash('Veuillez sélectionner les deux fichiers', 'error')
            return redirect(url_for('index'))
        
        if html_file and allowed_file(html_file.filename) and excel_file and allowed_file(excel_file.filename):
            # Sauvegarder les fichiers
            html_filename = secure_filename(html_file.filename)
            excel_filename = secure_filename(excel_file.filename)
            
            html_path = os.path.join(app.config['UPLOAD_FOLDER'], html_filename)
            excel_path = os.path.join(app.config['UPLOAD_FOLDER'], excel_filename)
            
            html_file.save(html_path)
            excel_file.save(excel_path)
            
            # Traitement des fichiers (comme dans interface.py)
            matrix_client_events = matcli(html_path)
            json_file('ROLLAND JEAN-MARC', excel_path)
            
            # Compter le nombre de sections
            nbr_section = count_sections_in_json('data/clients_sections.json')
            
            flash(f'Fichiers traités avec succès! {nbr_section} sections créées.', 'success')
            return redirect(url_for('sections', nb_sections=nbr_section))
        
        else:
            flash('Types de fichiers non autorisés', 'error')
            return redirect(url_for('index'))
            
    except Exception as e:
        flash(f'Erreur lors du traitement: {str(e)}', 'error')
        traceback.print_exc()
        return redirect(url_for('index'))

@app.route('/sections/<int:nb_sections>')
def sections(nb_sections):
    return render_template('sections.html', nb_sections=nb_sections, titres=TITRES)

@app.route('/api/generate_prompt/<int:section_id>')
def generate_prompt_api(section_id):
    try:
        prompt_text = prompt_association(
            TITRES, 
            'data/news_résume.md', 
            section_id, 
            json_path="data/clients_sections.json"
        )
        return jsonify({'success': True, 'prompt': prompt_text})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/save_responses', methods=['POST'])
def save_responses():
    try:
        responses = request.json.get('responses', [])
        
        # Traiter toutes les zones de texte (comme process_all_text_zones)
        all_lists = []
        all_summaries = []
        
        for response_text in responses:
            if response_text.strip():
                the_list, the_summary = divisiontext(response_text)
                all_lists.append(the_list)
                all_summaries.append(the_summary)
            else:
                all_lists.append([])
                all_summaries.append("")
        
        # Sauvegarder dans le fichier JSON
        output_data = {
            "all_lists": all_lists,
            "all_summaries": all_summaries
        }
        
        with open("data/results_processed.json", "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        
        return jsonify({'success': True, 'message': 'Réponses sauvegardées avec succès!'})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/generate_final_prompt')
def generate_final_prompt_api():
    try:
        # Vérifier l'existence des fichiers requis
        if not os.path.exists("data/results_processed.json"):
            return jsonify({'success': False, 'error': 'Le fichier results_processed.json n\'existe pas encore.'})
        
        if not os.path.exists("data/newsletter_md.md"):
            return jsonify({'success': False, 'error': 'Le fichier newsletter_md.md n\'existe pas.'})
        
        prompt = prompt_final(TITRES, "data/results_processed.json", "data/newsletter_md.md")
        return jsonify({'success': True, 'prompt': prompt})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/final')
def final():
    return render_template('final.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)