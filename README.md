Overview

GoodFoods is a multi-location restaurant chain looking to streamline and scale its reservation management process.
This project implements an end-to-end conversational AI reservation agent that understands user intent, recommends suitable restaurants, and completes reservations using a tool-calling architecture powered by a small LLM.

The solution is designed to demonstrate both GenAI engineering skills and business strategy thinking, within a realistic 4–6 hour build scope.

Key Objectives

Replace manual reservation handling with an AI-driven conversational agent

Improve table utilization and reduce staff overhead

Provide intelligent restaurant recommendations instead of static booking flows

Demonstrate modern LLM agent design without using LangChain or similar frameworks

Core Features

✅ LLM-driven intent detection (no hardcoded flows)

✅ Multi-turn conversation handling

✅ Restaurant recommendation based on constraints (location, cuisine, party size)

✅ Capacity-aware booking

✅ Natural language → structured data normalization

✅ Tool-calling architecture using Groq + LLaMA

✅ Streamlit frontend for rapid demo and evaluation

Architecture Overview
Streamlit UI
    ↓
Conversation Manager
    ↓
LLM (llama-3.1-8b-instant via Groq)
    ↓
Tool Router
    ├── search_restaurants
    ├── recommend_restaurants
    └── create_reservation
    ↓
JSON-based Data Store


Key design principle:
The LLM decides what to do, tools decide how to do it.

Tech Stack
Component	Technology
Language	Python
Frontend	Streamlit
LLM	llama-3.1-8b-instant (Groq API)
Agent Design	Custom tool-calling (no LangChain)
Data Storage	JSON (restaurants & reservations)
Config Management	python-dotenv
Project Structure
restaurant-reservation-agent/
├── app.py
├── requirements.txt
├── .env.example
│
├── config/
│   ├── settings.py
│   └── prompts.py
│
├── agent/
│   ├── llm_client.py
│   ├── conversation.py
│   └── tool_router.py
│
├── tools/
│   ├── restaurant_tools.py
│   └── reservation_tools.py
│
├── data/
│   ├── restaurants.json
│   └── reservations.json
│
├── utils/
│   ├── data_loader.py
│   └── validators.py
│
└── scripts/
    └── generate_data.py

Setup Instructions
1. Clone the repository
git clone <repo_url>
cd restaurant-reservation-agent

2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# or
source venv/bin/activate    # macOS/Linux

3. Install dependencies
pip install -r requirements.txt

4. Configure API key

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here

5. Generate restaurant data
python scripts/generate_data.py

6. Initialize reservations file

Create data/reservations.json with:

[]

7. Run the application
streamlit run app.py


The app will be available at:

http://localhost:8501

Example User Journeys
1️⃣ Clarification-First Interaction
User: I want to book a table
Agent: Asks for party size, date, time, cuisine/location

2️⃣ Recommendation Flow
User: 2 people, tomorrow at 7 pm, Italian food in Madhapur
Agent: Recommends best-fit restaurants

3️⃣ Booking Completion
User: Yes, please book it
Agent: Confirms reservation and stores it

Tool-Calling Design

The agent uses structured tools exposed to the LLM:

search_restaurants

recommend_restaurants

create_reservation

The LLM:

Selects the correct tool

Extracts structured arguments

Requests missing information when needed

Never assumes incomplete details

This avoids brittle rule-based logic and improves robustness.

Prompt Engineering Approach

The system prompt enforces:

No assumptions on missing data

Clarifying questions before actions

Preference for recommendations when user intent is vague

Separation between reasoning and execution

This ensures safe, predictable agent behavior.

Business Impact & ROI
Business Problems Addressed

Manual booking overhead

Uneven table utilization

Poor customer experience

No reservation intelligence

Measurable Impact

Reduced staff hours for reservation handling

Increased off-peak bookings

Higher table utilization

Fewer booking errors

Estimated ROI Example
Saving 2 staff hours/day/location across 50 locations → significant monthly cost reduction.

Vertical Expansion Potential

The same agent architecture can be adapted for:

Cafés & breweries

Event venues

Salons & spas

Clinics & diagnostics

Co-working spaces

Only tool implementations change — agent logic remains reusable.

Assumptions & Limitations

JSON storage used for simplicity (no DB)

No authentication or user profiles

Single-language (English) support

Not production-hardened (demo scope)

These are intentional tradeoffs for a 4–6 hour build.

Future Enhancements

Persistent database integration

User accounts & booking history

Cancellation & modification flows

No-show prediction

Multi-language support

Calendar/email integrations

Final Notes

This project focuses on correct agent architecture, business relevance, and clean execution, rather than over-engineering.

The goal is to demonstrate how a GenAI engineer bridges user needs, LLM capabilities, and real-world constraints effectively.