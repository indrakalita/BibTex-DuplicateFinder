import bibtexparser
from bibtexparser.bparser import BibTexParser

def read_bibtex_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def find_duplicate_entries(entries):
    seen_titles = {}
    duplicate_names = []
    
    for entry in entries:
        title = entry.get('title', '').lower()
        if title in seen_titles:
            duplicate_names.append((seen_titles[title], entry['ID']))
        else:
            seen_titles[title] = entry['ID']
    
    return duplicate_names

def main():
    file_path = 'H2OFORALL.bib'  # Replace with the path to your BibTeX file

    bibtex_content = read_bibtex_file(file_path)

    parser = BibTexParser()
    parser.ignore_nonstandard_types = False
    parser.homogenise_fields = True

    bib_database = bibtexparser.loads(bibtex_content, parser=parser)
    
    duplicate_names = find_duplicate_entries(bib_database.entries)

    if len(duplicate_names) > 0:
        print("Duplicate BibTeX entries based on titles:")
        for name1, name2 in duplicate_names:
            print(f"{name1} and {name2} are duplicates.")
    else:
        print("No duplicate BibTeX entries based on titles found.")

if __name__ == "__main__":
    main()

