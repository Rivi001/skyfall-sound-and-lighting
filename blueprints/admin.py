from flask import Blueprint, render_template
from services.database import get_all_enquiries, get_all_bookings

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/")
def dashboard():
    enquiries = get_all_enquiries()
    bookings = get_all_bookings()
    return render_template("admin.html", enquiries=enquiries, bookings=bookings)
