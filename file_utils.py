import PyPDF2
import requests

def extract_text_from_pdf(uploaded_file):
    text = ""
    reader = PyPDF2.PdfReader(uploaded_file)

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def extract_text_from_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8")


def extract_text_from_url(url):
    try:
        response = requests.get(url)
        return response.text
    except:
        return ""