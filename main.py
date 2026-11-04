import os
import PyPDF2
from groq import Groq
from dotenv import load_dotenv

# Load env vars
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("Error: GROQ_API_KEY is missing from the .env file")
    exit()

client = Groq(api_key=api_key)

def get_pdf_text(path):
    # Extract text from each page of the pdf
    pages_text = []
    try:
        with open(path, "rb") as f:
            pdf = PyPDF2.PdfReader(f)
            for page in pdf.pages:
                txt = page.extract_text()
                if txt:
                    pages_text.append(txt)
        
        full_text = "\n".join(pages_text)
        print(f"Done. Extracted {len(full_text)} chars from {len(pdf.pages)} pages.")
        return full_text
    except Exception as e:
        print(f"Couldn't read PDF: {e}")
        return None

def summarize_text(text):
    # Simple prompt for the AI
    prompt = f"""Summarize the following text from a PDF. 
    Focus on the key insights, main arguments, and conclusions. 
    Use 5-7 detailed bullet points.

    Text:
    {text}"""

    try:
        res = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="qwen/qwen3.8-27b",
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"AI Error: {e}"

def main():
    path = input("Enter PDF path: ").strip()
    
    if not os.path.exists(path):
        print("File not found. Please check the path.")
        return

    print("Reading file...")
    content = get_pdf_text(path)
    
    if not content or len(content) < 50:
        print("Not enough text found. Is it a scanned image/OCR PDF?")
        return
    
    print("Summarizing...")
    summary = summarize_text(content)
    
    print("\n--- Summary ---\n")
    print(summary)

if __name__ == "__main__":
    main()
