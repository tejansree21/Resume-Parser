# Resume Parser using NLP (spaCy + Regex)
# Extracts key information like name, email, phone, education, skills, and experience.

import re
import spacy
import pandas as pd
import docx2txt
from pdfminer.high_level import extract_text

# Load the spaCy NLP model
nlp = spacy.load('en_core_web_sm')

# Extract Text from Resume
def extract_text_from_file(file_path):
    if file_path.endswith('.pdf'):
        text = extract_text(file_path)
    elif file_path.endswith('.docx'):
        text = docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX.")
    return text

# Extract Email, Phone, Name
def extract_email(text):
    pattern = r'\S+@\S+'
    matches = re.findall(pattern, text)
    return matches[0] if matches else None

def extract_phone(text):
    pattern = r'\+?\d[\d -]{8,12}\d'
    matches = re.findall(pattern, text)
    return matches[0] if matches else None

def extract_name(nlp_text):
    for ent in nlp_text.ents:
        if ent.label_ == 'PERSON':
            return ent.text
    return None


# Extract Skills
def extract_skills(text):
    # You can expand this list
    skills_list = [
        'python', 'java', 'c++', 'sql', 'machine learning', 'deep learning',
        'data analysis', 'excel', 'power bi', 'nlp', 'tensorflow',
        'pytorch', 'aws', 'html', 'css', 'javascript'
    ]
    text = text.lower()
    found_skills = [skill for skill in skills_list if skill in text]
    return list(set(found_skills))

# Extract Education
def extract_education(nlp_text):
    edu_keywords = ['bachelor', 'master', 'b.tech', 'b.e', 'm.tech', 'phd', 'diploma']
    sentences = [sent.text.lower() for sent in nlp_text.sents]
    education = [sent for sent in sentences if any(edu in sent for edu in edu_keywords)]
    return education

# Extract Experience
def extract_experience(text):
    exp_pattern = r'(\d+)\s*(?:years|year|yrs|yr)\s*(?:of)?\s*(?:experience)?'
    matches = re.findall(exp_pattern, text.lower())
    return matches[0] + " years" if matches else "Not specified"

# Main Parser Function
def parse_resume(file_path):
    text = extract_text_from_file(file_path)
    nlp_text = nlp(text)

    name = extract_name(nlp_text)
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)
    education = extract_education(nlp_text)
    experience = extract_experience(text)

    data = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Skills": ', '.join(skills),
        "Education": education,
        "Experience": experience
    }

    return data
