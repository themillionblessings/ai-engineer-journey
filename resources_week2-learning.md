# **Week 2 Learning Resources**

Curated list of resources for Week 2 topics: **Cloud Deployment, Web Scraping, and LangChain.**

## **📦 Cloud Deployment**

**Render Documentation:**

* https://render.com/docs  
* **Focus:** "Deploy a Web Service" (This is what FastAPI runs as)  
* **Focus:** "Environment Variables" (How to securely manage API keys on the cloud)

**Video Tutorial (Search Term):**

* Search YouTube for: "fastapi render deployment 2025" (Aim for recent tutorials to ensure accuracy with current UI/settings.)

**Cheat Sheet (Preparing for Deployment):**

\# 1\. Create a virtual environment  
python \-m venv venv

\# 2\. Activate the environment (Mac/Linux)  
source venv/bin/activate

\# 3\. Install dependencies  
pip install fastapi uvicorn python-dotenv

\# 4\. Generate requirements.txt (CRITICAL for Render)  
pip freeze \> requirements.txt

\# 5\. Git workflow (to sync with Render)  
git add .  
git commit \-m "Prepare for Render deployment"  
git push origin main  
\# Then connect Render to the GitHub repository

## **🕷️ Web Scraping**

**BeautifulSoup Documentation (The main library):**

* https://www.crummy.com/software/BeautifulSoup/bs4/doc/

**Recommended Tutorial:**

* Real Python: "Beautiful Soup: Build a Web Scraper With Python"  
* Link: https://realpython.com/beautiful-soup-web-scraper-python/ (A reliable source for in-depth Python tutorials)

**Ethics Guide (Mandatory Review):**

* Always check robots.txt (e.g., https://www.example.com/robots.txt)  
* Respect rate limits (use time.sleep() between requests)  
* Don't overwhelm servers (avoid continuous rapid requests)  
* Only target public, non-sensitive data

**Legal Considerations:**

* **LinkedIn/Major Job Sites:** Often have strict Terms of Service against scraping. Use their public APIs when possible. For this learning project, focus on structuring the scraper and storing the data, rather than high-volume operation.

## **🦜 LangChain**

**Official Documentation (The best place to start):**

* https://python.langchain.com/docs/get\_started/introduction

**Free Course (Recommended by the community):**

* DeepLearning.AI: "LangChain for LLM Application Development"  
* Link: https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/

**Quick Start (Installation):**

\# Install the core LangChain package  
pip install langchain

\# Install the Google-specific integration for the Gemini API  
pip install langchain-google-genai

**Key Concepts to Understand:**

1. **Chains:** Sequence of operations (e.g., Prompt \-\> Model \-\> Output Parser)  
2. **Prompts:** Template management for LLM instructions  
3. **Models:** LLM integration (connecting to the Gemini API)  
4. **Memory:** Storing and retrieving past conversation context  
5. **Retrieval (RAG):** The key concept for Week 2—Retrieval Augmented Generation.

## **🔐 Environment Variables**

**Python Best Practices (.env for local development):**

\# Install python-dotenv  
pip install python-dotenv

\# Create .env file (NEVER commit this to GitHub\!)  
GEMINI\_API\_KEY=your\_secret\_key  
DATABASE\_URL=your\_db\_url  
\# ... etc

\# Use in code (FastAPI setup)  
from dotenv import load\_dotenv  
import os

load\_dotenv()  
API\_KEY \= os.getenv("GEMINI\_API\_KEY")

**Add to .gitignore (MANDATORY):**

\# Python environment files  
.env  
\*.env  
.env.local  
venv/  
\_\_pycache\_\_/

## **📚 Additional Resources**

**Python Packaging:**

* requirements.txt generation (as shown above)  
* Virtual environments review

**SQL Optimization:**

* Index strategy basics  
* Simple query optimization patterns (e.g., avoiding SELECT \*)

**API Security:**

* CORS basics (to allow your API to be called from other domains)  
* API rate limiting (protecting your endpoints)  
* Authentication patterns (bearer tokens, API keys)

**Last Updated:** October 19, 2025