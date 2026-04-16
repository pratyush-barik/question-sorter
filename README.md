# Question Sorter: An NLP-Based Question Classification System

This project implements a Natural Language Processing (NLP) pipeline for automatically mapping examination questions to their corresponding syllabus units. The system processes unstructured textual input and produces a structured output in the form of a categorized PDF document.

---

## Overview

Academic question banks are often unorganized, making it difficult to align them with syllabus topics. This system addresses the problem by applying text processing and similarity-based matching techniques to classify questions under appropriate units.

The application follows a lightweight NLP approach, prioritizing efficiency, interpretability, and ease of deployment.

---

## Core NLP Engine

The primary component of this system is the NLP pipeline implemented in `pipeline.py`. It consists of the following stages:

### 1. Syllabus Parsing
- The syllabus text is segmented into units using pattern recognition.
- Each unit acts as a category with associated descriptive content.

### 2. Text Preprocessing
- Input questions and syllabus content are normalized (lowercasing, token splitting).
- Noise such as numbering and formatting is removed.

### 3. Token-Based Matching
- Each question is tokenized into a set of words.
- Each unit’s content is similarly tokenized.
- A similarity score is computed using word overlap.

### 4. Unit Assignment
- Each question is assigned to the unit with the highest similarity score.
- In case of no match, a fallback unit is selected.

### 5. Output Generation
- Questions are grouped unit-wise.
- A structured PDF is generated using ReportLab.

---

## Algorithmic Approach

The current system uses a deterministic lexical matching approach:

- Set-based similarity scoring
- Greedy assignment strategy
- Rule-based syllabus segmentation

This ensures:
- Low computational overhead
- High interpretability
- No dependency on external NLP models

---

## Technology Stack

- Python (Flask)
- ReportLab (PDF generation)
- HTML/CSS/JavaScript (interface)
- Render (deployment platform)

---

## Project Structure

backend/
├── server.py # API and request handling
├── pipeline.py # NLP processing logic
├── requirements.txt # Dependencies
├── templates/
│ └── index.html
└── static/
├── script.js
└── style.css
---

## Execution Flow

1. User uploads syllabus and question files
2. Backend extracts raw text
3. NLP pipeline processes and classifies questions
4. Structured PDF is generated
5. Output is returned to the user

---

## Local Setup

git clone https://github.com/pratyush-barik/question-sorter.git  
cd question-sorter/backend  
pip install -r requirements.txt  
python server.py  

Access at: http://127.0.0.1:5000

---

## Deployment

The application is deployed as a web service using Render.

---

## Live Application

https://question-sorter.onrender.com/

---

## Limitations

- Relies on lexical similarity (no deep semantic understanding)
- Sensitive to vocabulary mismatch
- Does not currently use embeddings or trained models

---

## Future Enhancements

- TF-IDF based similarity scoring
- Word embeddings (Word2Vec / BERT)
- Semantic similarity using transformer models
- Question difficulty and marks classification
- Multi-format input support (PDF, DOCX)

---

## Author

Pratyush Barik
