# AI PDF Summarizer (Powered by Groq)

An ultra-fast AI-powered tool that extracts text from multi-page PDF documents and generates high-quality, comprehensive summaries using the Groq LPU inference engine and the Qwen model.

##  Features
- **Full-Document Analysis:** Unlike basic summarizers, this tool analyzes the entire PDF from start to finish.
- **Blazing Fast:** Uses Groq's LPU technology for near-instant AI responses.
- **High-Quality Output:** Employs professional prompt engineering to ensure the summary captures the beginning, middle, and end of the text.
- **Secure:** Uses environment variables to manage API permissions.

##  Tech Stack
- **Language:** Python 3.9+
- **AI Model:** Qwen (via Groq Cloud API)
- **PDF Parsing:** PyPDF2
- **Environment Management:** python-dotenv

## Installation & Setup

### 1. Clone the Project
```bash
git clone https://github.com/YOUR_USERNAME/AI-PDF-Summarizer.git
cd AI-PDF-Summarizer

### 2. Set Up a Virtual Environment (Recommended)

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate

### 3. Install Required Dependencies
pip install -r requirements.txt

### Permissions & API Configuration
To use this project, you need an API key from Groq.

Go to the Groq Cloud Console.
Create a free account and generate an API Key.
In the root folder of this project, create a file named .env.
Add your key to the .env file like this:

GROQ_API_KEY=your_actual_api_key_here


### How to Use
Place the PDF you want to summarize in the project folder.
Run the program:
        python3 main.py
When prompted, enter the name of your PDF file (e.g., test.pdf).
Wait a few seconds, and your AI summary will be generated!

