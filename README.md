# Product-agent-
**********PLEASE MAKE USE OF A RAW OPTION FOR BETTER DESCRIPTION***************************


1. This the interaction Diagram
User
 │
 │ (button click / form submit)
UI Controller (Streamlit)
 │
 │ (state mutation)
Agent Logic (LangChain)
 │
 │ (bounded prompt)

LLM (Gemini)
 │
 │ (≤120 chars enforced)
UI Renderer

2. States management
UI STATE
- step: int
- buttons visible
- inputs enabled/disabled
AGENT STATE
- product
- audience
- generation prompt
MEMORY STATE (Session)
- product: str
- audience: str
- result: str
- confidence: float


3. Failure Scenario: Low-Confidence Output

*What happens
LLM generates a vague or weak description
Confidence score is low (e.g. 45%)

Recovery Mechanism 

*User options:
Edit audience
Regenerate output

*What the system does:
Keeps product intact
Updates only audience or generation step
Re-invokes agent with improved context
