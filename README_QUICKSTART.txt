Refactory Day 2 — SQL Injection Assignment
==========================================

Run locally in 6 commands:

    python -m venv venv
    . venv/bin/activate            # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py seed_parts
    python manage.py runserver

Open http://127.0.0.1:8000/
    /vulnerable/   The INSECURE search — attack it
    /secure/       The SAFE search — try the same attacks

Full write-up is in REPORT.md
