# Exam Management System (Django Backend)

A backend-focused Django application for managing exams, questions, submissions, and results.

## Features
- Exam creation and management
- Question handling with multiple options
- Exam submission and automatic score calculation
- Prevention of exam reattempts
- Student-wise result tracking

## Backend APIs Implemented

- GET /exams/
  - List all exams
  - Returns JSON with status codes

- GET /exams/<exam_id>/questions/
  - Fetch questions for a specific exam
  - Handles no-question case with 404

- POST /exams/<exam_id>/take/
  - Submit answers
  - Calculates score
  - Prevents re-attempts

- GET /results/<student_id>/
  - Fetch results for a student

## Tech Stack
- Python
- Django
- SQLite
- Django ORM

## Focus
- Backend logic
- ORM-based relational modeling
- Clean request–response flow
- Validation and error handling