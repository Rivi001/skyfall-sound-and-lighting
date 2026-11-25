import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "skyfall-sound-light-durban-secret-key-2026")
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), "instance", "skyfall.db")
    LOG_PATH = os.path.join(os.path.dirname(__file__), "contact_submissions.log")
    COMPANY_NAME = "Skyfall Sound & Light"
    COMPANY_LOCATION = "Durban, KwaZulu-Natal, South Africa"
    COMPANY_PHONE = "+27 81 718 1206"
    COMPANY_WHATSAPP = "27817181206"
    COMPANY_EMAIL = "info@skyfallsoundandlight.co.za"
