# YAFD – Yet Another Food Delivery

YAFD is a prototype food delivery system designed to explore innovative and equitable incentive mechanisms for consumers, riders, and merchants. This project prioritizes robustness, maintainability, and extensibility over scalability, with a focus on core software engineering practices in a monolithic, client-server web application.

---

## Project Objectives

- Manage consumers, riders, and merchants
- Enable food ordering and delivery tracking
- Support food preparation and handover by merchants
- Automate incentive schemes for all user groups
- Facilitate feedback and ratings
- Recommend food items based on preferences
- Demonstrate clean software design patterns and DevOps practices

---

## System Architecture

- **Architecture**: Client/Server (Web frontend + Monolithic backend)
- **Backend**: Python Flask / Java Spring Boot (monolith)
- **Frontend**: HTML/CSS/JS (separate views for each user role)
- **Database**: Relational (e.g., PostgreSQL, MySQL)
- **CI/CD**: GitHub Actions with Docker-based build and test

---

## Modules

| Module | Description |
|--------|-------------|
| `User Management` | Registration, login, roles |
| `Menu & Orders` | Consumer ordering, merchant menus |
| `Delivery Workflow` | Rider delivery assignments |
| `Incentive Engine` | Role-based incentive calculation |
| `Ratings System` | Feedback for all users |
| `Recommendation Engine` | Suggests food items to consumers |

---

## DevOps Highlights

- **Containerized** using Docker
- **GitHub Actions** pipeline includes:
  - Linting
  - Unit testing
  - Docker build and push
- Minimal security (hashed passwords, input validation)

---

## Agile Artifacts

- Product Backlog and User Stories
- Sprint Plans (2-week sprints)
- Burndown Chart
- Sprint Reviews and Retrospectives

---

## Design Patterns Used

| Pattern | Purpose |
|--------|---------|
| Factory | User creation based on role |
| Strategy | Incentive calculation per role |
| Observer | Dynamic rating updates |
| Singleton | Database connection |
| Template Method | Custom order flows |

---

## Limitations

- Not cloud-native or microservices-based
- Minimal security & no production scalability
- Intended as a functional prototype only

---
