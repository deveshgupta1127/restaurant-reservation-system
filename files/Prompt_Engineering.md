PROMPT_ENGINEERING.md
Prompt Design & Conversation Control for the GoodFoods AI Agent
1. Objective of Prompt Engineering

The primary goal of prompt engineering in this project is to ensure that the AI agent behaves as a reliable, decision-making assistant, not a free-form chatbot.

The prompts are designed to:

Accurately identify user intent

Avoid hallucinated actions

Enforce information completeness before booking

Trigger structured tool calls when appropriate

Maintain a consistent and professional conversational tone

2. System Prompt Overview

The system prompt defines the role, responsibilities, and constraints of the agent.

System Prompt Used
You are a restaurant reservation AI agent for GoodFoods.

Your responsibilities:
- Understand user intent (search, recommend, reserve, cancel)
- Use tools when required
- Ask clarifying questions if information is missing
- Never assume missing details
- Prefer recommending restaurants when user is unsure
- Be concise and professional


This prompt establishes:

Clear role boundaries

Safety constraints

Behavioral priorities

3. Key Prompt Design Principles
3.1 No Assumptions Policy

The agent is explicitly instructed to never assume missing information such as:

Party size

Date or time

Location or cuisine

Preferred restaurant

This prevents:

Incorrect reservations

User frustration

Hallucinated backend actions

3.2 Clarification Before Action

Before invoking booking tools, the agent must:

Confirm all required parameters

Ask targeted follow-up questions

Validate user intent

This ensures every tool call is deterministic and safe.

3.3 Tool-First Execution Strategy

The agent is guided to:

Use tools for structured actions (search, recommend, reserve)

Avoid generating fabricated data

Treat tools as the source of truth

The LLM decides which tool to call, but the tool executes the business logic.

4. Intent Detection via Prompting (Not Rules)

The agent does not rely on hardcoded intent classification.

Instead, the prompt allows the LLM to infer intent based on:

User phrasing

Conversation context

Previously gathered information

Example intents inferred:

“I want to book a table” → Reservation intent (incomplete)

“Italian food in Madhapur” → Search intent

“Yes, book it” → Confirmation intent

5. Preventing Hallucinations

The prompt explicitly limits the agent to:

Ask questions when data is missing

Call tools instead of fabricating responses

Avoid confirming bookings unless a tool confirms success

This significantly reduces:

False confirmations

Inconsistent responses

Invalid data persistence

6. Conversation Consistency & Tone

The system prompt enforces:

Polite and professional tone

Concise responses

Action-oriented messaging

The agent avoids:

Over-verbosity

Informal or casual language

Unnecessary explanations

This makes the agent suitable for real customer-facing use.

7. Prompt-Tool Interaction Design
How prompts enable tool usage:

The system prompt explains when tools should be used

Tool schemas define what parameters are required

The LLM fills parameters based on conversation context

Tool execution returns structured results

The agent responds using tool outputs

This design cleanly separates:

Language understanding

Business logic

Data persistence

8. Handling Ambiguity & Edge Cases

When user input is ambiguous, the agent:

Requests clarification

Does not guess or infer silently

Maintains conversational continuity

Example:

“I want dinner tomorrow”
Agent asks for party size, time, and location.

9. Benefits of This Prompting Strategy

Reliable multi-turn conversations

Safe backend interactions

Scalable across domains

Easy to audit and extend

Minimal prompt complexity

10. Summary

The prompt engineering strategy focuses on control, safety, and clarity, ensuring that the agent:

Behaves predictably

Uses tools correctly

Delivers a smooth booking experience

This approach prioritizes production-ready agent behavior over free-form conversational creativity.

✅ Status

✔ System prompt defined
✔ Hallucination prevention enforced
✔ Tool usage aligned with intent
✔ Conversation reliability achieved