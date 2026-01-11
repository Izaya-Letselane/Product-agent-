Initial State (Step 1: Product)
- Product name input
- Confirm product button
- All steps pending

Partial Completion (Step 2: Audience)
- Product confirmed
- Audience input
- Option to edit product

Generation Trigger (Step 3)
- Generate description button only

Agent Output (Step 4)
- Generated description (≤120 chars)
- Agent confidence shown
- Options to accept, edit, or regenerate

2. Interaction Diagrams

High-Level Flow:
User → UI Controller → Agent Logic → LLM → UI Renderer

State Machine:
Step 1 → Step 2 → Step 3 → Step 4
Corrections loop back without reset.

3. UI vs Agent vs Memory State Model

UI State:
- Controls visible inputs and buttons

Agent State:
- Uses product and audience to generate output

Memory State:
- Persists task data across steps

4. Failure Scenario and Recovery

Failure:
- Low confidence or vague output

Recovery:
- User edits audience or regenerates
- Previous state preserved
- No restart required

5. Why Plain Text Chat Would Fail

- No deterministic state
- No enforced constraints
- Higher prompt injection risk
- Increased cognitive load for users


