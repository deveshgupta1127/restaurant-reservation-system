ASSUMPTIONS_LIMITATIONS.md
Assumptions, Constraints, and Future Enhancements
1. Assumptions

The following assumptions were intentionally made to keep the solution focused, evaluatable, and aligned with a 4–6 hour build scope.

1.1 Data Storage

Restaurant and reservation data are stored in local JSON files

Data volume is assumed to be small (demo-scale)

Rationale:
This avoids unnecessary database setup while still demonstrating correct data modeling and persistence logic.

1.2 Single User Context

The agent operates in a single-session, single-user context

No user authentication or profiles are implemented

Rationale:
Authentication is orthogonal to agent intelligence and not required to evaluate tool-calling or intent detection.

1.3 English Language Only

The agent currently supports English-language input only

Rationale:
Multi-language support would require additional prompt logic and testing, outside the challenge scope.

1.4 Ideal Backend Availability

Tools are assumed to execute successfully

No external service failures are simulated

Rationale:
The focus is on agent behavior, not infrastructure resilience.

2. Limitations
2.1 Not Production-Hardened

No rate limiting

No authentication

No concurrency control

No persistent database

This implementation is a functional prototype, not a production system.

2.2 Limited Natural Language Normalization

Only basic normalization is applied (e.g., “tomorrow” → ISO date)

Advanced time parsing (e.g., “next Friday evening”) is not implemented

2.3 No Modification or Cancellation Flow

The current version supports booking creation only

Reservation modification and cancellation are not implemented

2.4 Static Recommendation Logic

Recommendations are based on simple filters (rating, capacity)

No machine learning ranking or personalization is applied

3. Trade-Off Decisions
Decision	Trade-Off
JSON storage	Simplicity over scalability
No LangChain	Full control over agent logic
Small LLM	Lower cost and latency
Streamlit UI	Rapid demo over custom frontend

All trade-offs were made deliberately to optimize for clarity, correctness, and evaluation speed.

4. Future Enhancements
4.1 Backend & Data Layer

Replace JSON storage with a relational or NoSQL database

Add transactional safety and concurrency handling

4.2 User Accounts & History

User authentication

Reservation history

Repeat-customer personalization

4.3 Advanced Agent Capabilities

Reservation modification and cancellation

Multi-location comparison

Preference learning over time

4.4 Analytics & Intelligence

Demand forecasting

No-show prediction

Dynamic pricing or slot-based incentives

4.5 Multi-Channel Deployment

WhatsApp

Web chat

Voice assistants

5. Summary

The current system is intentionally scoped as a working, end-to-end GenAI agent prototype.
It prioritizes:

Correct agent behavior

Safe tool execution

Business relevance

Clear extensibility paths

The documented limitations represent opportunities for iteration, not design flaws.

✅ Status

✔ Assumptions documented
✔ Limitations acknowledged
✔ Trade-offs justified
✔ Future roadmap defined