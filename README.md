# BibTeX Duplicate Finder

BibTeX Duplicate Finder is a Flask web application that helps you find duplicate entries in a BibTeX file. It takes a BibTeX file as input and displays any duplicate author entries.

## Features

- Upload a BibTeX file for processing.
- Identify and display duplicate author entries.
- No installation is required; runs as a Flask web application.

## Prerequisites

- Python (>=3.6)
- Flask
- bibtexparser

## Installation/Instructions

1. Clone or download the repository to your local machine.

```bash
git clone https://github.com/indrakalita/BibTex-DuplicateFinder.git

2. Install the required dependencies using pip.
pip install Flask bibtexparser

3. Navigate to the project directory.
cd BibTex-DuplicateFinder

4. Run the Flask application.
python app.py

Open your web browser and go to http://localhost:5000 to access the application.

Upload a BibTeX file using the provided form and click the "Process" button.

The application will identify any duplicate author entries and display the results.
**Note: Nothing will be printed if no duplicate is identified.**
Example:
![alt text]([http://url/to/img.png](https://github.com/indrakalita/BibTex-DuplicateFinder/blob/main/test.png)https://github.com/indrakalita/BibTex-DuplicateFinder/blob/main/test.png)

