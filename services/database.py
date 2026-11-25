import sqlite3
import os
from datetime import datetime
from config import Config
from services.business_data import SERVICES as BUSINESS_SERVICES

def get_db_connection():
    db_path = Config.DATABASE_PATH
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enquiries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            location TEXT,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            event_type TEXT NOT NULL,
            event_date TEXT,
            venue_location TEXT,
            guest_count TEXT,
            services_needed TEXT,
            budget TEXT,
            notes TEXT,
            status TEXT DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS newsletter (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS site_services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            slug TEXT UNIQUE NOT NULL,
            icon TEXT,
            short_desc TEXT,
            features TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS instagram_posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            caption TEXT,
            post_url TEXT UNIQUE NOT NULL,
            image_url TEXT,
            is_featured INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS site_settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
    ''')

    conn.commit()
    _seed_default_content(conn)
    conn.commit()
    conn.close()


def _seed_default_content(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM site_services")
    if cursor.fetchone()[0] == 0:
        for service in BUSINESS_SERVICES:
            cursor.execute(
                "INSERT INTO site_services (title, slug, icon, short_desc, features) VALUES (?, ?, ?, ?, ?)",
                (
                    service["title"],
                    service["id"],
                    service.get("icon", "speaker"),
                    service.get("short_desc", ""),
                    "|".join(service.get("features", [])),
                ),
            )

    posts = [
        {
            "title": "Instagram Post 1",
            "caption": "LETS GO 2025!",
            "post_url": "https://www.instagram.com/p/DExrrUZMbsM/",
            "image_url": "/static/images/insta_DExrrUZMbsM.jpg",
        },
        {
            "title": "Instagram Post 2",
            "caption": "😎😎😎",
            "post_url": "https://www.instagram.com/p/DExsc6Gs-II/",
            "image_url": "/static/images/insta_DExsc6Gs-II.jpg",
        },
        {
            "title": "Instagram Post 3",
            "caption": "Book now",
            "post_url": "https://www.instagram.com/p/C5Y4uXysHZ2/",
            "image_url": "/static/images/hero_stage.jpg",
        },
    ]
    for post in posts:
        cursor.execute(
            """
            INSERT INTO instagram_posts (title, caption, post_url, image_url, is_featured)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(post_url) DO UPDATE SET
                title = excluded.title,
                caption = excluded.caption,
                image_url = excluded.image_url,
                is_featured = excluded.is_featured
            """,
            (post["title"], post["caption"], post["post_url"], post["image_url"], 1),
        )

    default_settings = [
        ("site_title", "Skyfall Sound & Light"),
        ("site_tagline", "Durban's Premier Event Production"),
        ("hero_image", "/static/images/hero_stage.jpg"),
        ("logo_file", "/static/images/skyfall_logo.jpg"),
    ]
    for key, value in default_settings:
        cursor.execute(
            """
            INSERT INTO site_settings (key, value)
            VALUES (?, ?)
            ON CONFLICT(key) DO UPDATE SET value = excluded.value
            """,
            (key, value),
        )

def save_enquiry(name, email, phone, location, message):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO enquiries (name, email, phone, location, message) VALUES (?, ?, ?, ?, ?)",
        (name, email, phone, location, message)
    )
    conn.commit()
    conn.close()

def save_booking(name, email, phone, event_type, event_date, venue_location, guest_count, services_needed, budget, notes):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''INSERT INTO bookings
           (name, email, phone, event_type, event_date, venue_location, guest_count, services_needed, budget, notes)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (name, email, phone, event_type, event_date, venue_location, guest_count, services_needed, budget, notes)
    )
    conn.commit()
    conn.close()

def save_newsletter(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO newsletter (email) VALUES (?)", (email,))
        conn.commit()
        success = True
    except sqlite3.IntegrityError:
        success = False
    conn.close()
    return success

def get_all_enquiries():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM enquiries ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_all_bookings():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_services():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM site_services ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row["id"],
            "title": row["title"],
            "slug": row["slug"],
            "icon": row["icon"],
            "short_desc": row["short_desc"],
            "features": row["features"].split("|") if row["features"] else [],
        }
        for row in rows
    ]


def get_instagram_posts():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM instagram_posts ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row["id"],
            "title": row["title"],
            "caption": row["caption"],
            "post_url": row["post_url"],
            "image_url": row["image_url"],
            "is_featured": bool(row["is_featured"]),
        }
        for row in rows
    ]


def get_site_settings():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT key, value FROM site_settings")
    rows = cursor.fetchall()
    conn.close()
    return {row["key"]: row["value"] for row in rows}
