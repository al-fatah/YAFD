# YAFD – Yet Another Food Delivery (Proof of Concept)

YAFD is a prototype food delivery system designed to explore innovative and equitable incentive mechanisms for consumers, riders, and merchants. This project prioritizes robustness, maintainability, and extensibility over scalability, with a focus on core software engineering practices in a monolithic, client-server web application.

---

## 📌 Project Objectives

- Manage consumers, riders, and merchants
- Enable food ordering and delivery tracking
- Support food preparation and handover by merchants
- Automate incentive schemes for all user groups
- Facilitate feedback and ratings
- Recommend food items based on preferences
- Demonstrate clean software design patterns and DevOps practices

---

## 🏗️ System Architecture

- **Architecture**: Client/Server (Web frontend + Monolithic backend)
- **Backend**: Python Flask / Java Spring Boot (monolith)
- **Frontend**: HTML/CSS/JS (separate views for each user role)
- **Database**: Relational (e.g., PostgreSQL, MySQL)
- **CI/CD**: GitHub Actions with Docker-based build and test

---

## 🧱 Modules

| Module | Description |
|--------|-------------|
| `User Management` | Registration, login, roles |
| `Menu & Orders` | Consumer ordering, merchant menus |
| `Delivery Workflow` | Rider delivery assignments |
| `Incentive Engine` | Role-based incentive calculation |
| `Ratings System` | Feedback for all users |
| `Recommendation Engine` | Suggests food items to consumers |

---

