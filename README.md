# **Project Title: Workflow Automation Backend**

## **Overview**

This project is a simple **Python FastAPI** application designed to serve as a backend service for an external workflow automation tool. The goal is to create a robust and secure API that can be consumed by other services to fetch data, execute tasks, and demonstrate seamless external API integration.

This README documents the journey so far (Days 1-4) and provides instructions for setting up and running the application.

## **🚀 Getting Started**

### **Prerequisites**

To run this project locally, you will need:

* **Python 3.8+**  
* **ngrok** (to expose your local server to the internet)

### **Installation**

1. **Clone the repository:**  
   git clone \[YOUR\_REPO\_URL\]  
   cd \[your-project-folder\]

2. **Create a virtual environment (Recommended):**  
   python \-m venv venv  
   source venv/bin/activate  \# On macOS/Linux  
   .\\venv\\Scripts\\activate   \# On Windows

3. **Install dependencies:**  
   pip install fastapi uvicorn

### **Running the Server**

1. Start the FastAPI server:  
   The API will run on http://localhost:9000.  
   python \-m uvicorn api\_server:app \--host 0.0.0.0 \--port 9000

2. Expose the server with ngrok:  
   In a new terminal window, use ngrok to create a public HTTPS tunnel to your local server.  
   ngrok http 9000

   This will provide you with a public URL (e.g., https://example-tunnel.ngrok-free.dev) that external tools can use to communicate with your application.

## **🗓️ Development Log: Days 1 \- 4**

### **Day 1 & 2: Project Setup and Initial Structure**

* **Objective:** Define project goals, set up the development environment, and install core libraries (**FastAPI**, **Uvicorn**).  
* **Result:** Established a basic project structure with api\_server.py. Successfully initialized and ran a simple "Hello, World" test endpoint to ensure the server was functioning correctly on a local port.

### **Day 3: Defining the Service and Public Exposure**

* **Objective:** Create the first functional endpoint (/skills) and integrate the server with **ngrok** to make it accessible to the external workflow automation tool.  
* **Result:**  
  * Implemented the /skills endpoint to return mock JSON data.  
  * Successfully created an ngrok tunnel forwarding to http://localhost:9000.

### **Day 4: Debugging the 404 Routing Issue**

* **Objective:** Execute the first live test from the external workflow tool.  
* **Result & Challenge:**  
  * **Success:** Confirmed full external network connectivity via ngrok. The request successfully reached the ngrok URL and was forwarded to the local machine.  
  * **Failure:** The FastAPI application responded with a persistent **404 Not Found** error for the /skills endpoint. Debugging confirmed the error originated from the application layer, suggesting a potential routing, code version, or process management conflict. This issue is paused and is the first task for Day 5\.