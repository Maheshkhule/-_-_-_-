# tools.py
from langchain.tools import tool
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from utils import extract_text_from_pdf

load_dotenv()

# Use your custom model via Groq's OpenAI-compatible endpoint
# If Groq doesn't support "openai/gpt-oss-20b", change to a valid Groq model like "llama3-70b-8192"
llm = ChatGroq(
    model="llama-3.3-70b-versatile",   # Replace with actual model name if different
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

@tool
def calculate_bmi(height_cm: float, weight_kg: float) -> str:
    """
    Calculate BMI from height (cm) and weight (kg) and return risk category.
    """
    bmi = weight_kg / ((height_cm / 100) ** 2)
    if bmi < 18.5:
        category = "Underweight (low risk)"
        multiplier = 0.9
    elif bmi < 25:
        category = "Normal (low risk)"
        multiplier = 1.0
    elif bmi < 30:
        category = "Overweight (moderate risk)"
        multiplier = 1.2
    else:
        category = "Obese (high risk)"
        multiplier = 1.5
    return f"BMI: {bmi:.1f} - {category} (risk multiplier: {multiplier})"

@tool
def extract_medical_conditions(medical_text: str) -> str:
    """
    Extract diseases and severity from the medical report text.
    """
    prompt = f"""
    From the following medical report, list all medical conditions and their severity (mild/moderate/severe).
    If none, say "None". Return as bullet points.

    Report:
    {medical_text[:3000]}
    """
    response = llm.invoke(prompt)
    return response.content

@tool
def calculate_risk_score(age: int, smoker: str, bmi: float, conditions_summary: str) -> str:
    """
    Calculate numeric risk score (0-100) and return decision (Accept/Decline/Flag).
    """
    score = 0
    if age > 70:
        score += 40
    elif age > 50:
        score += 20
    elif age > 30:
        score += 5
    if smoker.lower() == "yes":
        score += 25
    if bmi > 35:
        score += 20
    elif bmi > 30:
        score += 10
    if "severe" in conditions_summary.lower():
        score += 30
    elif "cancer" in conditions_summary.lower():
        return "DECLINE: High-risk condition (Cancer) found."

    if score >= 70:
        decision = "DECLINE: Risk score too high."
    elif score >= 40:
        decision = f"FLAG FOR MANUAL REVIEW. Risk score: {score}"
    else:
        multiplier = 1 + (score / 100)
        decision = f"ACCEPT. Base premium multiplier: {multiplier:.2f}"
    return f"Risk score: {score}. {decision}"