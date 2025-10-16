# **Project: AI Engineering Daily Progress Tracker**

## **🚀 Overview**

This repository documents my daily progress in the AI Engineering journey, focusing on two distinct tracks: **Foundational Python Development** and **Workflow Automation**.

It includes production-ready Python scripts for data handling and an automated low-code n8n workflow for content delivery.

## **🛠️ Core Technologies & Structure**

| Feature | Technologies Used | Directory |
| :---- | :---- | :---- |
| **Foundations** | Python (3.x), JSON, CSV | python-practice/ |
| **Automation** | n8n, LinkedIn Marketing API, DevTools | n8n-workflows/ |
| **Documentation** | Markdown, Git | Root Directory |
| **Data Storage** | JSON, Excel (as source data) | data/ |

## **1\. Foundational Python Progress**

The focus has been on mastering data persistence, serialization, and creating utility applications.

### **Key Applications & Skills Mastered:**

* **Personal Finance Tracker (python-practice/day3\_expense\_tracker.py):**  
  * A command-line application for tracking expenses.  
  * **Skill:** Robust **JSON file handling** for data saving and loading.  
  * **Skill:** Calculating and displaying a financial summary with breakdown by category.  
* **Data Structures Practice (python-practice/day3\_data\_structures.py):**  
  * **Skill:** Practical use of Lists, Dictionaries, and Sets for efficient data manipulation.

## **2\. Workflow Automation (n8n & LinkedIn)**

This track focuses on creating a fully automated system for publishing daily progress updates to LinkedIn.

### **System Components:**

1. **Daily Trigger:** Sets the workflow schedule (e.g., Cron job).  
2. **Data Fetch:** Retrieves progress data (e.g., the JSON output from the Python expense tracker).  
3. **Content Generation:** Uses an LLM to generate a professional, engaging LinkedIn post based on the fetched data.  
4. **LinkedIn Post Node:** Publishes the finalized content.

### **🔑 Technical Breakthrough: LinkedIn API User ID**

The primary challenge was securely identifying the user for the posting node. We overcame this by using **DevTools deep debugging** to capture the specific /me? API endpoint. This allowed us to retrieve the non-public and essential urn:li:person:\[ID\] required to maintain a persistent, authorized connection for content posting.

## **3\. Setup and Run Instructions**

1. **Clone the Repository:**  
   git clone \[YOUR\_REPO\_URL\]  
   cd \[YOUR\_REPO\_NAME\]

2. **Python:** Navigate to the python-practice/ directory and run the expense tracker:  
   cd python-practice/  
   python day3\_expense\_tracker.py

3. **n8n:** Import the n8n workflow JSON file (to be placed in the n8n-workflows/ directory) into your n8n instance and configure your LinkedIn OAuth credentials.