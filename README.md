# 🧭 Nomad - Intent-Based Travel Planning with Gemini

Nomad is an AI-powered travel decision engine that **reverses traditional travel planning**.

Instead of choosing a destination first, users describe their **constraints, preferences, and tradeoffs** — and Gemini reasons about *where*, *when*, and *why* to travel.

Built for MLH Hackathons · Best Use of Gemini API

---

## ✨ What Makes Nomad Different

Most travel platforms rely on:
- Keyword search
- Predefined filters
- Destination-first thinking

**Nomad does the opposite.**

It:
- Extracts constraints from natural language
- Eliminates incompatible options
- Reasons about timing, cost, distance, and experience
- Explains *why* each recommendation fits

This is **constraint-driven reasoning**, not search.

---

## 🧠 Powered by Google Gemini

Nomad uses the **Gemini API** to:
- Understand complex, human travel intent
- Perform multi-step reasoning over constraints
- Generate transparent explanations and tradeoffs

Gemini is essential here — rule-based systems cannot reason about vague human needs like:
> “Good value for money, relaxed pace, not overcrowded, family-friendly.”

---

## 🧳 Example Prompt

> I have one main vacation this year.  
> I can take 9–11 days off between late April and mid-May.  
> My budget is limited, and I’m traveling with my partner and one child.  
>  
> We want warm weather, beach access, safe walkable areas, and short flights.  
> We do NOT want crowded tourist hotspots or expensive resorts.  
>  
> Recommend destinations and explain your reasoning and tradeoffs.

---

## 🧭 Example Output

- Explicit constraints identified
- Destinations eliminated with justification
- Final recommendations with:
  - Why they fit
  - Cost level (relative)
  - Timing rationale
- Risks & tradeoffs (weather, logistics, complexity)

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** (UI)
- **Google Gemini API**
- Clean, minimal design focused on reasoning clarity

---

## 🚀 Running Locally

```bash
pip install streamlit google-genai
streamlit run app.py
