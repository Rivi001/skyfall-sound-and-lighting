"""
Social Data & Reviews Service for Skyfall Sound & Light
Recreating Smash Balloon Social Feed Features with Local Original Thumbnails
"""

import os
import requests
from services.database import get_instagram_posts

INSTAGRAM_PROFILE_URL = "https://www.instagram.com/skyfall_sound_and_light/"
INSTAGRAM_POST_URLS = [
    "https://www.instagram.com/p/DExrrUZMbsM/",
    "https://www.instagram.com/p/DExsc6Gs-II/",
    "https://www.instagram.com/p/C5Y4uXysHZ2/",
]
INSTAGRAM_POST_IMAGES = [
    "/static/images/insta_DExrrUZMbsM.jpg",
    "/static/images/insta_DExsc6Gs-II.jpg",
    "/static/images/insta_C5Y4uXysHZ2.jpg",
]
INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")


def _fetch_instagram_posts():
    if not INSTAGRAM_ACCESS_TOKEN:
        return None

    try:
        response = requests.get(
            "https://graph.instagram.com/me/media",
            params={
                "fields": "id,caption,media_type,media_url,thumbnail_url,permalink,timestamp",
                "access_token": INSTAGRAM_ACCESS_TOKEN,
                "limit": 3,
            },
            timeout=15,
        )
        response.raise_for_status()
        payload = response.json()
        posts = []
        for item in payload.get("data", [])[:3]:
            caption = (item.get("caption") or "Instagram post").strip()
            media_url = item.get("media_url") or item.get("thumbnail_url") or "/static/images/hero_stage.jpg"
            posts.append({
                "id": item.get("id"),
                "platform": "instagram",
                "handle": "@skyfall_sound_and_light",
                "author_name": "Skyfall Sound & Light",
                "avatar": "/static/images/skyfall_logo.jpg",
                "title": "Instagram Post",
                "type": "Featured Instagram Post",
                "media_type": item.get("media_type", "IMAGE"),
                "image": media_url,
                "likes": 340,
                "comments": 25,
                "shares": 14,
                "timestamp": "Just posted",
                "caption": caption,
                "url": item.get("permalink") or INSTAGRAM_PROFILE_URL,
                "featured": True,
            })
        return posts
    except Exception:
        return None


def get_social_accounts():
    return {
        "instagram": {
            "name": "Skyfall Sound & Light",
            "handle": "@skyfall_sound_and_light",
            "followers": "14.8K",
            "posts_count": 342,
            "avatar": "/static/images/skyfall_logo.jpg",
            "url": INSTAGRAM_PROFILE_URL
        },
        "facebook": {
            "name": "Skyfall Sound & Light Durban",
            "handle": "@skyfall.durban",
            "followers": "22.5K",
            "likes_count": "21K",
            "avatar": "/static/images/skyfall_logo.jpg",
            "url": "https://facebook.com"
        },
        "tiktok": {
            "name": "Skyfall Event FX",
            "handle": "@skyfall_fx",
            "followers": "38.2K",
            "avatar": "/static/images/skyfall_logo.jpg",
            "url": "https://tiktok.com"
        }
    }

def get_google_reviews():
    return [
        {
            "author": "Dr. Rajesh & Priya Patel",
            "rating": 5,
            "relative_time": "2 weeks ago",
            "text": "Skyfall Sound & Light transformed our wedding at Umhlanga Function Centre into a fairytale! The cold spark fountains during our entrance and the low fog dance on clouds were absolutely mind-blowing. Sound was crystal clear throughout the venue.",
            "avatar": "R"
        },
        {
            "author": "Craig Campbell (East Coast Event Productions)",
            "rating": 5,
            "relative_time": "1 month ago",
            "text": "We hired Skyfall for a 1,500-person beach festival in Durban. Their line array setup and moving head beams were rock solid. Professional crew, on-time setup, and zero technical hitches. Top tier pro audio supplier in KZN!",
            "avatar": "C"
        },
        {
            "author": "Melanie De Villiers",
            "rating": 5,
            "relative_time": "3 weeks ago",
            "text": "Outstanding service for our corporate gala at Gateway Hotel. The speech audio was extremely clear for all 300 delegates, and the LED backdrop screen made our visual presentations shine.",
            "avatar": "M"
        },
        {
            "author": "DJ Zane K",
            "rating": 5,
            "relative_time": "2 months ago",
            "text": "Top notch Pioneer CDJ-3000 backline gear hire! Skyfall supplied our club night in Florida Road with zero hassle. Gear was immaculate and sound punchy.",
            "avatar": "Z"
        }
    ]

def get_social_posts(platform="all"):
    instagram_posts = _fetch_instagram_posts()

    posts = []
    if instagram_posts:
        posts.extend(instagram_posts)
    else:
        db_posts = get_instagram_posts()
        posts.extend([
            {
                "id": post["id"],
                "platform": "instagram",
                "handle": "@skyfall_sound_and_light",
                "author_name": "Skyfall Sound & Light",
                "avatar": "/static/images/skyfall_logo.jpg",
                "title": post.get("title") or "Instagram Post",
                "type": "Featured Instagram Post",
                "media_type": "Photo",
                "image": post.get("image_url") or INSTAGRAM_POST_IMAGES[min(post["id"] - 1, len(INSTAGRAM_POST_IMAGES) - 1)],
                "likes": 340,
                "comments": 25,
                "shares": 14,
                "timestamp": "Latest Post",
                "caption": post.get("caption") or "Instagram post",
                "url": post.get("post_url") or INSTAGRAM_POST_URLS[min(post["id"] - 1, len(INSTAGRAM_POST_URLS) - 1)],
                "featured": True,
            }
            for post in db_posts
        ])

    posts.extend([
        {
            "id": 4,
            "platform": "facebook",
            "handle": "@skyfall.durban",
            "author_name": "Skyfall Sound & Light Durban",
            "avatar": "/static/images/skyfall_logo.jpg",
            "title": "Main Stage Pro Audio Engineering",
            "type": "Concert Audio",
            "media_type": "Photo",
            "image": "/static/images/concert_sound.jpg",
            "likes": 275,
            "comments": 19,
            "shares": 22,
            "timestamp": "4 days ago",
            "caption": "Rigged and ready for 2,000 live attendees in Durban Central. Precision acoustic tuning for absolute clarity across every row. #LiveAudio #LineArray #FestivalSound",
            "url": "https://facebook.com",
        },
        {
            "id": 5,
            "platform": "tiktok",
            "handle": "@skyfall_fx",
            "author_name": "Skyfall Event FX",
            "avatar": "/static/images/skyfall_logo.jpg",
            "title": "Cold Spark Pyrotechnic Entrance Burst",
            "type": "Special Effects",
            "media_type": "Video",
            "image": "/static/images/wedding_lighting.jpg",
            "likes": 1240,
            "comments": 87,
            "shares": 195,
            "timestamp": "5 days ago",
            "caption": "Watch this bride & groom entrance! Indoor safe cold spark fountains popping on cue. #TikTokDurban #ColdSparks #EventFX #WeddingVibes",
            "url": "https://tiktok.com",
        },
        {
            "id": 6,
            "platform": "facebook",
            "handle": "@skyfall.durban",
            "author_name": "Skyfall Sound & Light Durban",
            "avatar": "/static/images/skyfall_logo.jpg",
            "title": "Gateway Corporate Summit LED Wall Backdrop",
            "type": "Corporate AV",
            "media_type": "Photo",
            "image": "/static/images/hero_stage.jpg",
            "likes": 198,
            "comments": 12,
            "shares": 9,
            "timestamp": "1 week ago",
            "caption": "Full high-definition P3 LED video panel backdrop & speech PA system supplied for Gateway Conference Center. #CorporateEvents #DurbanBusiness #AVProduction",
            "url": "https://facebook.com",
        },
    ])

    if platform != "all":
        posts = [p for p in posts if p["platform"] == platform]

    return posts
