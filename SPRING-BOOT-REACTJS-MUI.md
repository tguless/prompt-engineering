# Project Prompt Template

Use this template to kick off a ReactJS + Spring Boot cloud-native application. Fill in your project-specific details under **Your Requirements** and update as you progress.

---

## Project Overview

> Briefly describe what you’re building, who it’s for, and why.

**Your Requirements**  
> List high-level goals, non-functional requirements, or constraints.

---

## 1. Tech Stack

- **Frontend**  
  - React (initialized with `npx create-react-app`)  
  - Material UI for UI components
- **Backend**  
  - Spring Boot (latest stable version)  
  - Spring Data JPA for persistence  
  - OpenFeign (modern version) for REST clients
- **Database**  
  - PostgreSQL (dockerized, dev port 5635)  
  - Liquibase for schema management

---

## 2. Database & Migration

1. **Schema Design**  
   - Define entities and relationships.  
   - Support multi-tenancy if needed.
2. **Liquibase Configuration**  
   - Use a **privileged** Liquibase user for migrations.  
   - Application uses a **separate, lower-privileged** user.  
   - Store Liquibase changelog tables in your application schema.  
   - Name changesets sequentially:
   ```xml
   00001-create-users-table.xml
   00002-add-email-index.xml
   ```
3. **Local Dev Setup**  
   ```yaml
   # docker-compose.yml
   version: '3.8'
   services:
     db:
       image: postgres:latest
       ports:
         - "5635:5432"
       environment:
         POSTGRES_USER: liquibase_user
         POSTGRES_PASSWORD: <secure-pw>
         POSTGRES_DB: your_app_db
   ```

---

## 3. Code Conventions

- Use Lombok for DTOs and JPA entities (`@Getter`, `@Setter`, `@Builder`, etc.).  
- Always depend on the most recent stable versions of Spring Boot, Spring Data, OpenFeign, etc.  
- Organize packages clearly: `com.yourcompany.app.domain`, `.service`, `.web`, etc.

---

## 4. README & Project Plan

1. **Initial Sections**  
   - Project overview & goals  
   - Tech stack & architecture diagram  
2. **Implementation Details**  
   - DB user roles & Liquibase setup  
   - Docker Compose instructions  
   - React frontend scaffold instructions  
   - How to run & test the Spring Boot app  
3. **Project Plan**  
   - Track tasks in a “To Do / In Progress / Done” list  
   - Link to issue tracker or Kanban board

---

## 5. Development Roadmap

| Phase       | Tasks                                           |
|-------------|-------------------------------------------------|
| **Database**    | Finalize ERD, configure Liquibase & users     |
| **Backend**     | Scaffold Spring Boot, implement entities & repos |
| **Frontend**    | Scaffold CRA, integrate Material UI           |
| **Integration** | Define REST endpoints, OpenFeign & UI calls    |
| **Testing**     | Unit/integration tests, end-to-end smoke tests |

---

## 6. Optional (Marketing & SaaS)

- **Homepage**: Landing page to promote your automation platform.  
- **Multi-tenancy**: Ensure DB schema & Spring Security support multiple tenants.

---

**Usage:** Copy this file into your repo, fill in each section, and share with your team or AI assistant to generate boilerplate code.
