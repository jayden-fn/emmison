# ROLSA (sample Django site)

This repository is a small Django site used as a demo for ROLSA Technologies.

What's included

- A small `website` app with pages: home, calculate, booking, and a few static templates
- Simple form validation and unit tests for the core forms/views
- Opinionated code-style config: Black/isort/ruff and Prettier settings
- Basic CI workflow to run linters on push/PR

Getting started (development)

1. Create a virtual environment and install dependencies (Django and dev tools):

   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt

2. Run migrations and start the dev server:

   python manage.py migrate
   python manage.py runserver

Testing

- Run unit tests with:

  python manage.py test

Notes

- This repository was lightly refactored for readability, better validation, accessibility, and maintainability.
- If you'd like, I can continue by adding more tests, running automatic formatting, or introducing components like a contact persistence model and email sending.