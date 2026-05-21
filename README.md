# AI Document Summarizer
A Python desktop application that automatically summarizes 
documents using the LexRank NLP algorithm. Supports multiple 
file formats with export and text-to-speech capabilities.

## Features
- Upload TXT, PDF, or DOCX files
- AI-powered summarization using LexRank algorithm
- Dynamic summary length based on document size
- Export summary as PDF or DOCX
- Text-to-speech playback of summary
- Clean and simple desktop GUI

## Tech Stack
- Python
- Tkinter (GUI)
- Sumy / LexRank (NLP Summarization)
- pdfminer (PDF reading)
- python-docx (DOCX reading & export)
- ReportLab (PDF export)
- pyttsx3 (Text-to-speech)

## How to Run

1. Clone the repository:
git clone https://github.com/Ramzi0929/ai-document-summarizer

2. Install dependencies:
pip install sumy pdfminer.six python-docx reportlab pyttsx3

3. Run the app:
python gui.py

## Project Structure
- `gui.py` — Desktop interface and user interaction
- `summarizer_main.py` — Core summarization, file reading, 
   and export logic

## Author
Ramzi Mohammed
