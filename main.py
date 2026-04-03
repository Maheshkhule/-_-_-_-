# main.py
from agent import agent_executor

def run_underwriting(age, smoker, medical_text, height, weight):
    """
    Call the LangChain agent to perform underwriting.
    Returns (explanation_text, premium_estimate).
    """
    # Build the user query with all available information
    query = f"""
    Please perform insurance underwriting for this applicant:
    
    - Age: {age}
    - Smoker: {smoker} (answer Yes or No)
    - Height: {height} cm
    - Weight: {weight} kg
    - Medical report text: {medical_text if medical_text else 'No medical report provided'}
    
    Please use the available tools to assess risk and provide a final decision.
    """
    
    # Invoke the agent
    result = agent_executor.invoke({"messages": [("user", query)]})
    
    # Extract the response
    explanation = result["messages"][-1].content
    premium = "Calculated based on risk score (see analysis above)"
    
    return explanation, premium