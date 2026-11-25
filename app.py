import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify

from config import Config
from services.social_data import get_google_reviews, get_social_posts, get_social_accounts
from services.email_service import init_mail, send_contact_email
from services.business_data import LOCATIONS, TEAM, PACKAGES, BRANDS
from services.database import init_db, save_enquiry, get_services, get_instagram_posts, get_site_settings
from blueprints.api import api_bp
from blueprints.admin import admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize mail & database
    init_mail(app)
    init_db()

    # Register blueprints
    app.register_blueprint(api_bp)
    app.register_blueprint(admin_bp)

    @app.context_processor
    def inject_global_vars():
        settings = get_site_settings()
        return {
            "company_name": Config.COMPANY_NAME,
            "company_phone": Config.COMPANY_PHONE,
            "company_whatsapp": Config.COMPANY_WHATSAPP,
            "company_email": Config.COMPANY_EMAIL,
            "locations": LOCATIONS,
            "brands": BRANDS,
            "current_year": datetime.now().year,
            "site_settings": settings,
        }

    @app.route("/")
    def home():
        reviews = get_google_reviews()
        posts = get_social_posts()
        services = get_services()
        return render_template("index.html", reviews=reviews, posts=posts, services=services, packages=PACKAGES)

    @app.route("/about")
    def about():
        return render_template("about.html", team=TEAM)

    @app.route("/services")
    def services():
        return render_template("services.html", services=get_services())

    @app.route("/packages")
    def packages():
        return render_template("packages.html", packages=PACKAGES)

    @app.route("/updates")
    def updates():
        posts = get_social_posts()
        accounts = get_social_accounts()
        instagram_posts = get_instagram_posts()
        return render_template("updates.html", posts=posts, accounts=accounts, instagram_posts=instagram_posts)

    @app.route("/contact", methods=["GET", "POST"])
    def contact():
        submitted = False
        mail_status = None
        if request.method == "POST":
            name = request.form.get("name", "").strip()
            email = request.form.get("email", "").strip()
            phone = request.form.get("phone", "").strip()
            message = request.form.get("message", "").strip()
            location = request.form.get("location", "Durban Central").strip()

            if name and email and message:
                submitted = True
                save_enquiry(name, email, phone, location, message)
                sent, mail_status = send_contact_email(app, name, email, phone, message, location)

        return render_template("contact.html", submitted=submitted, mail_status=mail_status)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
