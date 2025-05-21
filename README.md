# K12 Syllabus Reviser

Welcome to **K12 Syllabus Reviser** — an AI-powered study assistant tailored for K-12 students. This tool helps generate custom study questions across multiple subjects and formats to enhance learning and revision effectiveness.

---

## 🚀 Features

- Generate questions by **Subject**, **Topic**, and **Study Format** (MCQ, Q&A, Fill in the blanks, Type Answer)  
- Supports **custom subjects** for personalized study needs  
- **User inputs answers first**, then checks correctness with detailed explanations  
- Download question sets as **PDF** for offline or printed study  
- Clean and intuitive **Streamlit frontend**  
- Powerful **Flask backend** integrated with Groq LLaMA 3 API for smart AI-generated questions

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit (Python)  
- **Backend:** Flask (Python)  
- **AI Model:** Groq LLaMA 3 API  
- **PDF Generation:** FPDF (Python)  

---

## ⚙️ Setup & Installation

### Backend Setup

1. Clone the repo and navigate to the backend folder:  
   ```bash
   git clone https://github.com/nty23/k12-syllabus-reviser.git
   cd k12-syllabus-reviser/backend

### Create and activate a virtual environment

python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

### Install dependencies 

pip install -r requirements.txt

### Create a .env file in the backend folder and add your Groq API key:
GROQ_API_KEY=your_groq_api_key

### Run the backend server
python app.py

### Frontend setup
### Open a new terminal and navigate to frontend folder
cd ../frontend

### Install dependencies
pip install -r requirements.txt

### Run the frontend app
streamlit run app.py

### 🎯 Usage Guide
1. Select a subject or enter a custom subject if needed.
2. Enter the study topic.
3. Select the number of questions you want.
4. Choose your preferred study format: MCQ, Q&A, Fill in the blanks, or Type Answer.
5. Click Generate Questions to get your questions.
6. Provide your answers in the app interface.
7. Click Check Answers to verify your responses and view explanations.
8. Use Generate More Questions to add fresh questions on the same topic.
9. Download your entire Q&A set as a PDF to study offline or share.

### 📐 High-Level Design & Architecture
The system consists of:

Frontend: Streamlit app for user interaction, question display, answer input, and PDF export.
Backend: Flask API server that handles question generation requests, communicates with the Groq LLaMA 3 AI model, and returns structured question data.
AI Model: Groq’s LLaMA 3 large language model, generating contextually accurate and format-specific questions and answers based on user input.
Hardware Requirements
Local Development: Standard laptop/desktop with Python environment and internet for API calls.
Deployment: Cloud VM or server (e.g., AWS EC2, DigitalOcean) with at least 2 vCPUs, 4GB RAM recommended for smooth Flask and Streamlit operation.
API: Internet connection for Groq AI API access.
For detailed design diagrams, component interaction, and data flow, see the DESIGN.md file.


### 📁 Project Structure
k12-syllabus-reviser/
│
├── backend/
│   ├── app.py           # Flask backend API
│   ├── requirements.txt # Backend dependencies
│   ├── .env             # API key storage (not included in repo)
│
├── frontend/
│   ├── app.py           # Streamlit frontend app
│   ├── requirements.txt # Frontend dependencies
│
├── DESIGN.md            # High-level design & architecture document
├── README.md            # This file


### 🙋‍♂️ About Me

Created with ❤️ by Nitya Dhawan
https://www.linkedin.com/in/nitya-dhawan/ | https://github.com/nty23

Feel free to reach out for feedback, questions, or collaboration!

Thank you for exploring K12 Syllabus Reviser — your friendly AI study buddy for smarter revision! 📚✨

