import os
import PyPDF2
from groq import Groq
from dotenv import load_dotenv

# 1. Load API key from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ Error: GROQ_API_KEY not found in .env file. Please add it!")
    exit()

# Initialize Groq Client
client = Groq(api_key=api_key)

def extract_text_from_pdf(pdf_path):
    """Extracts all text from a given PDF file."""
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            print(f"📄 PDF contains {len(reader.pages)} pages.")
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        print(f"✅ Successfully extracted {len(text)} characters.")
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
    return text

def summarize_text(text):
    """Sends the extracted text to Groq AI for summarization."""
    # Professional prompt to ensure the AI reads the whole document
    prompt = (
        "You are a professional research assistant. I will provide you with text extracted from a PDF. "
        "Please analyze the ENTIRE text from start to finish. "
        "Ensure that you include key insights from the beginning, middle, and end of the document. "
        "Provide a comprehensive summary in 5-7 detailed bullet points. "
        f"\n\nTEXT TO SUMMARIZE:\n{text}"
    )

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="qwen/qwen3.8-27b", # Using the model confirmed by your check_groq.py
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"❌ AI Error: {e}"

if __name__ == "__main__":
    print("--- Welcome to AI PDF Summarizer (Powered by Groq) ---")
    pdf_file = input("Enter the path to your PDF file (e.g., test.pdf): ")
    
    try:
        print("\n--- Step 1: Extracting Text ---")
        extracted_text = extract_text_from_pdf(pdf_file)
        
        if len(extracted_text) < 50:
            print("⚠️ Warning: Very little text was found. The PDF might be a scanned image.")
        
        print("\n--- Step 2: Generating AI Summary (Groq is super fast!) ---")
        summary = summarize_text(extracted_text)
        
        print("\n--- 🚀 FINAL SUMMARY ---\n")
        print(summary)
        print("\n-----------------------")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
