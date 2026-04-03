# 🛡️ AI-Driven Insurance Underwriting Agent

An automated insurance risk assessment system built with **Agentic AI** to streamline the underwriting process for brokers and insurers.

## 🚀 Overview
This project automates the transition from raw applicant data and unstructured medical reports to a final underwriting decision. By leveraging **LangChain** and **Groq (llama-3.3-70b-versatile)**, it reduces manual review time by extracting key clinical data and calculating risk scores instantly.

## ✨ Core Features
* **Automated Risk Profiling:** Processes applicant data including age, smoking status, and physical metrics (Height/Weight).
* **Intelligent PDF Extraction:** Uses LLMs to parse unstructured medical report PDFs and identify pre-existing conditions.
* **Advanced Orchestration:** A LangChain agent coordinates multiple custom tools to:
    * **Calculate BMI:** Automatically determines risk category based on body metrics.
    * **Decision Logic:** Computes a final risk score to output a status: `ACCEPT`, `DECLINE`, or `FLAG`.
* **Broker Dashboard:** A specialized **Streamlit UI** allowing underwriters to upload files and receive instant feedback.

## 🛠️ Tech Stack
* **Orchestration:** LangChain (Agentic Workflow)
* **LLM:** `openai/gpt-oss-20b` via **Groq** (LPU Inference)
* **Frontend:** Streamlit
* **Database (Optional):** Supabase / PostgreSQL (for audit logs)
* **Language:** Python 3.11

## 📊 How it Works
1.  **Input:** User enters demographics and uploads a medical PDF.
2.  **Reasoning:** The Agent analyzes the input and decides which tool to call first (e.g., `calculate_bmi`).
3.  **Extraction:** The medical report is sent to the Groq-powered LLM to summarize key health risks.
4.  **Decision:** The system applies business rules to determine the premium and risk status.
