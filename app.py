# app.py

# ============================================================
# Author: Indrajit Kalita
# Date: 26-Aug-2023
# Address: Computing and Data Science, Boston University, MA, USA 
# ============================================================

from flask import Flask, render_template, request, send_file, session
import bibtexparser
import secrets
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from SimilarityFinder import find_duplicate_entries

app = Flask(__name__)
secret_key = secrets.token_hex(32)
app.secret_key = secret_key



@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.bib'):
            content = file.read().decode('utf-8')
            parser = BibTexParser()
            parser.ignore_nonstandard_types = False
            parser.homogenise_fields = True
            bib_database = bibtexparser.loads(content, parser=parser)
            duplicate_names = find_duplicate_entries(bib_database.entries)
            result = duplicate_names
    return render_template('index.html', result=result)

def generate_output_content(duplicate_pairs, original_bib_database):
    output_bib_database = BibDatabase()
    for pair in duplicate_pairs:
        entry1 = next(entry for entry in original_bib_database.entries if entry['ID'] == pair[0])
        entry2 = next(entry for entry in original_bib_database.entries if entry['ID'] == pair[1])
        output_bib_database.entries.append(entry1)
        output_bib_database.entries.append(entry2)
    output_bibtex = BibTexWriter().write(output_bib_database)
    return output_bibtex

@app.route('/download')
def download():
    if 'result' in session:
        result = session['result']
        if result:
            output_content = "\n".join([f"{entry[0]} and {entry[1]}" for entry in result])
            return Response(output_content,
                            content_type='text/plain',
                            headers={"Content-Disposition": "attachment; filename=duplicate_entries.txt"})
    return "No duplicate entries found."

if __name__ == '__main__':
    app.run(debug=True)
