# L1.1 — One-Page SDLC Plan: City Bus Fleet Tracking (600 Buses)

| Phase | Key Activities | Output Artifact | Owner |
| :--- | :--- | :--- | :--- |
| **1. Planning & Scope** | Define system scope for 600 buses, GPS ingestion rate, arrival prediction goals, driver roster constraints, budget, and risk register | Project Charter & Risk Register | Project Manager |
| **2. Requirements Analysis** | Elicit functional and non-functional requirements with fleet operators, dispatchers, and commuters; define API and telemetry contracts | Software Requirements Specification (SRS) | Business / Systems Analyst |
| **3. System & Software Design** | Architect GPS ingestion pipeline, ETA prediction model, roster scheduling engine, database schema, and dispatch/commuter UIs | Architecture Design Doc, DB Schema & UI Wireframes | Lead Architect & Tech Lead |
| **4. Implementation** | Build GPS telemetry ingestor, ETA estimation service, driver roster module, REST/WebSocket APIs, and frontend dashboards | Source Code & Unit Test Suite | Backend & Frontend Engineers |
| **5. Testing & Verification** | Execute unit, integration, load (600+ concurrent bus streams), boundary, and negative tests; validate ETA accuracy and roster rules | QA Test Report & Defect Log | QA Lead & Test Engineers |
| **6. Deployment & Rollout** | Provision production cloud/on-prem infrastructure, configure CI/CD pipelines, run pilot route rollout, and cut over full 600-bus fleet | Production Release & Runbook | DevOps / Release Engineer |
| **7. Operations & Maintenance** | Monitor GPS latency, drift in ETA predictions, roster compliance, incident tickets, and iterative model/feature updates | SLA Telemetry Reports & Patch Releases | Fleet Operations & Support Team |
