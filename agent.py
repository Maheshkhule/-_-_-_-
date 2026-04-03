# agent.py
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from tools import calculate_bmi, extract_medical_conditions, calculate_risk_score

load_dotenv()

# Initialize Groq LLM with temperature 0 for deterministic outputs
llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # Change to your model if different
    temperature=0,            # CRITICAL: Zero reduces hallucinations
    api_key=os.getenv("GROQ_API_KEY")
)

# List of available tools
tools = [calculate_bmi, extract_medical_conditions, calculate_risk_score]

# Optimized system prompt to prevent hallucinations
agent = create_agent(
    llm, 
    tools, 
    system_prompt="""You are an AI insurance underwriting assistant.
Your job is to assess risk and recommend a decision (Accept/Decline/Flag).
Follow this plan:
1. Calculate BMI using the calculate_bmi tool (needs height in cm and weight in kg).
2. Extract medical conditions from the report using extract_medical_conditions.
3. Calculate the final risk score using calculate_risk_score (needs age, smoker, bmi, conditions).
4. Provide a clear final decision and explanation.

Be thorough and transparent."""

)

# Agent executor (the agent is callable directly)
agent_executor = agent