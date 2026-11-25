from flask import Blueprint, request, jsonify, current_app
from services.database import save_enquiry, save_booking, save_newsletter
from services.email_service import send_contact_email, send_booking_email
from services.social_data import get_social_posts, get_social_accounts

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route("/book", methods=["POST"])
def book_event():
    data = request.get_json() or request.form
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    phone = data.get("phone", "").strip()
    event_type = data.get("event_type", "General Event").strip()
    event_date = data.get("event_date", "").strip()
    venue_location = data.get("venue_location", "Durban").strip()
    guest_count = data.get("guest_count", "100-200").strip()
    services_needed = data.get("services_needed", "Sound & Lighting").strip()
    budget = data.get("budget", "Standard").strip()
    notes = data.get("notes", "").strip()

    if not name or not email or not phone:
        return jsonify({"success": False, "error": "Name, Email, and Phone number are required"}), 400

    save_booking(name, email, phone, event_type, event_date, venue_location, guest_count, services_needed, budget, notes)
    send_booking_email(current_app, name, email, phone, event_type, event_date, venue_location, guest_count, services_needed, notes)

    return jsonify({
        "success": True,
        "message": f"Thank you {name}! Your Skyfall Sound & Light quote request has been received. Our Durban technical team will contact you shortly."
    })

@api_bp.route("/quote-calculator", methods=["POST"])
def calculate_quote():
    data = request.get_json() or {}
    event_type = data.get("event_type", "wedding")
    guest_count = int(data.get("guest_count", 150))
    sound_tier = data.get("sound_tier", "standard")
    lighting_tier = data.get("lighting_tier", "standard")
    fx_items = data.get("fx_items", [])

    base_price = 2500
    if event_type == "wedding":
        base_price = 3500
    elif event_type == "concert":
        base_price = 6500
    elif event_type == "corporate":
        base_price = 4500

    if guest_count > 500:
        base_price += 3000
    elif guest_count > 250:
        base_price += 1500

    if sound_tier == "concert":
        base_price += 4000
    elif sound_tier == "standard":
        base_price += 1800

    if lighting_tier == "intelligent":
        base_price += 2500
    elif lighting_tier == "ambient":
        base_price += 1200

    if "cold_sparks" in fx_items:
        base_price += 1500
    if "low_fog" in fx_items:
        base_price += 1200
    if "laser" in fx_items:
        base_price += 1800
    if "led_wall" in fx_items:
        base_price += 3500

    min_est = base_price
    max_est = int(base_price * 1.25)

    return jsonify({
        "success": True,
        "estimated_min": f"R {min_est:,}",
        "estimated_max": f"R {max_est:,}",
        "summary": f"Estimated package for {guest_count} guests ({event_type.capitalize()})"
    })

@api_bp.route("/social-feed", methods=["GET"])
def social_feed():
    platform = request.args.get("platform", "all").lower()
    posts = get_social_posts(platform=platform)
    accounts = get_social_accounts()
    return jsonify({
        "success": True,
        "platform": platform,
        "count": len(posts),
        "posts": posts,
        "accounts": accounts
    })

@api_bp.route("/newsletter", methods=["POST"])
def newsletter():
    data = request.get_json() or request.form
    email = data.get("email", "").strip()

    if not email:
        return jsonify({"success": False, "error": "Email is required"}), 400

    saved = save_newsletter(email)
    if saved:
        return jsonify({"success": True, "message": "Subscribed to Skyfall Sound & Light updates!"})
    else:
        return jsonify({"success": True, "message": "You are already subscribed!"})
