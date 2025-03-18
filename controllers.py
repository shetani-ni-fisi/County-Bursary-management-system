# app/controllers.py
from app.models import Bursary

def create_bursary(applicant_name, amount):
    return Bursary(applicant_name, amount)
