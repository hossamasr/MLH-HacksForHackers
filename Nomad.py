import streamlit as st
from google import genai
from google.genai import types

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Nomad – Intent-Based Travel Engine",
    page_icon="🧭",
    layout="centered"
)

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.title("🔐 Settings")
    api_key = st.text_input("Gemini API Key", type="password")
    st.caption("Your key is used only for this session.")

# ----------------------------
# Main UI
# ----------------------------
st.title("🧭 Nomad")
st.markdown("### *Intent-Based Travel Planning powered by Gemini*")
st.markdown(
    "Nomad reverses traditional travel platforms. "
    "Instead of choosing a city and dates, you describe **constraints** "
    "and Gemini reasons about the best destinations, timing, and tradeoffs."
)

st.divider()

mode = st.selectbox(
    "Planning Mode",
    [
        "Family-friendly",
        "Budget Optimized",
        "Adventure",
        "Romantic",
        "Remote Work / Digital Nomad"
    ]
)

user_input = st.text_area(
    "Describe your trip needs and constraints",
    placeholder=(
        "Example:\n"
        "I have 10 days off in April. Budget is limited. "
        "I want somewhere warm, kid-friendly, "
        "no long flights, and not very crowded."
    ),
    height=160
)

# ----------------------------
# System Instruction (CORE)
# ----------------------------
SYSTEM_INSTRUCTION = """
You are Nomad, an expert travel decision engine.

Your job is NOT to list random destinations.
Your job is to reason like a human travel agent.

You MUST follow this structure exactly:

## Constraints Identified
- Extract budget, time, mobility, preferences, risks

## Reasoning
- Explain tradeoffs and elimination logic
- Show why some options are better than others

## Recommended Destinations
Provide 2–3 destinations. For each:
- Why it fits the constraints
- Estimated cost level (Low / Medium / High)
- Best time to travel

## Risks & Tradeoffs
- What might not be ideal
- What the user should be aware of

Be concise, insightful, and human.
"""

# ----------------------------
# Action Button
# ----------------------------
if st.button("🧠 Compute My Best Trip"):
    if not api_key:
        st.error("Please enter your Gemini API key.")
    elif not user_input.strip():
        st.error("Please describe your trip needs.")
    else:
        with st.spinner("Gemini is reasoning about your trip..."):
            try:
                client = genai.Client(api_key=api_key)

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=f"""
Planning Mode: {mode}

User Input:
{user_input}
""",
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION
                    )
                )

                st.divider()
                st.markdown("## 🧳 Nomad’s Recommendation")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"Something went wrong:\n{e}")

# ----------------------------
# Footer
# ----------------------------
st.divider()
st.caption(
    "Built for MLH Hackathons · Best Use of Gemini API · "
    "Nomad demonstrates constraint-driven reasoning, not keyword search."
)
