import os
from datetime import datetime
from config import Config

def init_mail(app):
    pass

def send_contact_email(app, name, email, phone, message, location="Durban"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] CONTACT | Name: {name} | Email: {email} | Phone: {phone} | Location: {location} | Msg: {message}\n"
    
    try:
        os.makedirs(os.path.dirname(Config.LOG_PATH), exist_ok=True)
        with open(Config.LOG_PATH, "a", encoding="utf-8") as f:
            f.write(log_line)
        return True, "Log Saved Successfully"
    except Exception as e:
        return False, str(e)

def send_booking_email(app, name, email, phone, event_type, event_date, venue_location, guest_count, services_needed, notes):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] BOOKING REQUEST | Name: {name} | Email: {email} | Phone: {phone} | Event: {event_type} | Date: {event_date} | Venue: {venue_location} | Guests: {guest_count} | Services: {services_needed} | Notes: {notes}\n"
    
    try:
        os.makedirs(os.path.dirname(Config.LOG_PATH), exist_ok=True)
        with open(Config.LOG_PATH, "a", encoding="utf-8") as f:
            f.write(log_line)
        return True, "Log Saved Successfully"
    except Exception as e:
        return False, str(e)
