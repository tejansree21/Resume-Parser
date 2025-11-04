# Resume Parser using NLP

## Project Overview
This project automatically extracts key information from resumes (PDF or DOCX) using **Natural Language Processing (NLP)** techniques.  
It’s designed to assist recruiters and HR systems in filtering candidate data like **skills, education, experience, and contact details** automatically.

---

## Features
Extracts structured data such as:
- Full Name  
- Email Address  
- Phone Number  
- Technical Skills  
- Education Details  
- Work Experience  

- Supports multiple file formats — `.pdf` and `.docx`  
- Works using **spaCy**, **Regex**, and **PDF/Text processing libraries**

---

## Project Structure
Resume-Parser/
│
├── resume_parser.py # Main script
├── Resume_Sample.pdf # Example resume for testing
├── requirements.txt # Dependencies
├── parsed_resumes.csv # Output (if parsing multiple resumes)
└── README.md


---

## Requirements
Install all required dependencies:
```bash
pip install spacy pandas pdfminer.six docx2txt nltk
python -m spacy download en_core_web_sm
