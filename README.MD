# DevTrack

DevTrack is a Django-based job application management platform designed to help users organize, track, and manage their job search from one centralized dashboard.

Users can create an account, track applications across multiple companies, update application statuses, store job-specific notes, and maintain a clear view of their hiring pipeline.

The project is focused on practical full-stack development concepts including authentication, relational data modeling, CRUD workflows, authorization, API design, and clean Django architecture.

---

## Overview

Job searching often becomes difficult to manage across spreadsheets, browser tabs, saved job postings, emails, and personal notes.

DevTrack centralizes that workflow into a single application where users can manage:

* Companies
* Job applications
* Application statuses
* Job posting URLs
* Salary information
* Application dates
* Notes
* Interview progress
* Offer and rejection outcomes

The long-term goal is to provide a lightweight but extensible platform for managing the entire job application lifecycle.

---

## Core Features

### User Authentication

Users can:

* Create an account
* Log in securely
* Log out
* Access protected application data

### Job Application Management

Users can:

* Create job applications
* View all applications
* View individual application details
* Update application information
* Delete applications
* Track application status
* Store notes and relevant job links

### Company Management

Applications are associated with companies.

Company data may include:

* Company name
* Website
* Location
* Company logo

### Application Status Tracking

Applications can move through stages such as:

* Saved
* Applied
* Interview
* Offer
* Rejected

### User Data Isolation

Application data is tied to the authenticated user.

Users should only be able to view, update, or delete their own job applications.

---

# Data Model

DevTrack uses Django's built-in authentication system along with application-specific relational models.

```text
User
 |
 | one-to-many
 |
 v
JobApplication
 |
 | many-to-one
 |
 v
Company
```

## User

Django's built-in User model handles authentication and account management.

A single user can own multiple job applications.

## Company

Represents a company associated with one or more job applications.

Planned fields include:

```text
name
website
location
logo
```

## JobApplication

Represents an individual job opportunity or submitted application.

Planned fields include:

```text
user
company
position
status
job_url
salary
notes
applied_date
created_at
updated_at
```

---

# User Experience

A typical DevTrack workflow looks like this:

```text
Create Account
      ↓
Log In
      ↓
Add Company
      ↓
Create Job Application
      ↓
Track Application Status
      ↓
Add Notes / Updates
      ↓
Interview / Offer / Rejection
```

A user's dashboard may provide a summary such as:

```text
Total Applications: 24
Saved: 3
Applied: 11
Interviews: 5
Offers: 1
Rejected: 4
```

---

# Development Roadmap

## Phase 1 — Foundation

* Set up Django project structure
* Configure Python virtual environment
* Configure application settings
* Set up dependency management
* Configure Git and repository structure
* Create shared project documentation
* Establish base application architecture

---

## Phase 2 — Data Layer

* Create `Company` model
* Create `JobApplication` model
* Associate job applications with authenticated users
* Define model relationships
* Create and apply database migrations
* Register models with Django Admin
* Validate model behavior through administrative workflows

---

## Phase 3 — Authentication

* Implement user registration
* Implement login
* Implement logout
* Create authentication templates
* Protect authenticated routes
* Add navigation based on authentication state

---

## Phase 4 — Job Application CRUD

Implement full create, read, update, and delete workflows for job applications.

### Create

* Create application form
* Save applications to the database
* Automatically associate applications with the logged-in user

### Read

* Display application list
* Display application detail pages
* Display related company information

### Update

* Edit job application details
* Update application status
* Update notes and job metadata

### Delete

* Add delete confirmation workflow
* Safely remove applications

---

## Phase 5 — Authorization & Data Security

* Restrict application queries by authenticated user
* Prevent users from accessing another user's application
* Prevent unauthorized updates
* Prevent unauthorized deletes
* Validate ownership at the view level

---

## Phase 6 — Dashboard & Frontend

* Create shared `base.html`
* Build application navigation
* Create authenticated dashboard
* Display application statistics
* Display recent applications
* Add application status summaries
* Add responsive CSS styling
* Improve form usability
* Improve empty states and application feedback

---

## Phase 7 — Search, Filtering & Productivity

* Search applications by position or company
* Filter applications by status
* Sort applications by date
* Sort applications by company
* Add recent activity views
* Improve dashboard visibility into active applications

---

## Phase 8 — File & Image Support

* Add company logo uploads
* Configure Django media storage
* Display uploaded logos in company and application views
* Validate uploaded file types

---

## Phase 9 — REST API

Expose application data through RESTful endpoints using Django REST Framework.

Potential endpoints:

```text
GET    /api/applications/
POST   /api/applications/
GET    /api/applications/<id>/
PUT    /api/applications/<id>/
DELETE /api/applications/<id>/
```

The API can support future clients such as:

* React frontend
* Mobile applications
* Browser extensions
* External automation tools

---

## Phase 10 — Analytics

Add dashboard analytics for the user's job search pipeline.

Potential metrics include:

* Total applications
* Applications per week
* Interview rate
* Offer rate
* Rejection rate
* Applications by status
* Applications by company
* Recent activity

---

## Phase 11 — AI-Assisted Job Analysis

Integrate an LLM-powered job analysis workflow.

Potential functionality:

* Paste a job description
* Extract required skills
* Identify matching skills
* Identify missing skills
* Summarize job requirements
* Generate interview preparation topics
* Compare job descriptions against user-provided experience

Example output:

```text
Job Match Analysis

Matching Skills
- Python
- Django
- REST APIs
- JavaScript

Skills to Strengthen
- AWS
- Docker
- PostgreSQL

Recommended Interview Topics
- Django ORM
- RESTful API design
- Authentication
- Database relationships
```

---

# Planned Architecture

Initial architecture:

```text
Browser
   ↓
Django Templates
   ↓
Django Views
   ↓
Django ORM
   ↓
SQLite
```

Future architecture may evolve toward:

```text
React / External Client
          ↓
       REST API
          ↓
        Django
          ↓
     PostgreSQL
```

---

# Tech Stack

## Backend

* Python
* Django

## Database

* SQLite for local development
* PostgreSQL planned for production

## Frontend

* HTML
* CSS
* Django Templates

## Authentication

* Django Authentication System

## API

* Django REST Framework

## Development Tools

* VS Code
* Git
* GitHub
* Python Virtual Environments

---

# Project Structure

```text
devtrack/
│
├── applications/
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   └── css/
│
├── templates/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Local Development

## 1. Clone the repository

```bash
git clone <repository-url>
cd DevTrack
```

## 2. Create a virtual environment

```powershell
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

## 4. Apply database migrations

```powershell
python manage.py migrate
```

## 5. Start the development server

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# Future Direction

DevTrack is designed to begin as a focused Django application while leaving room for more advanced architecture and integrations.

Future development may include:

* PostgreSQL deployment
* React frontend
* REST API integrations
* Job board API integrations
* Email-based application tracking
* Interview reminders
* Resume-to-job matching
* AI-assisted job analysis
* Analytics and reporting
* Cloud deployment
