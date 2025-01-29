import os
import requests
import zipfile
import shutil

url = "https://archive.ics.uci.edu/static/public/383/cervical+cancer+risk+factors.zip"

def download():
    response = requests.get(url)
    with open("cervical_cancer_risk_factors.zip", "wb") as f:
        f.write(response.content)

def unzip():
    with zipfile.ZipFile("cervical_cancer_risk_factors.zip", 'r') as zip_ref:
        zip_ref.extractall("cervical_cancer_risk_factors")

def transform_csv():
    input_file = 'cervical_cancer_risk_factors/risk_factors_cervical_cancer.csv'
    output_file = 'data/cervical-cancer.csv'

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            outfile.write(line.replace('?', ''))  # Replaces '?' but keeps everything else


def clean():
    shutil.rmtree("cervical_cancer_risk_factors")
    os.remove("cervical_cancer_risk_factors.zip")

if __name__=='__main__':
    download()
    unzip()
    transform_csv()
    clean()
