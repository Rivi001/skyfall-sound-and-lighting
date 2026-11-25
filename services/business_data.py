"""
Skyfall Sound & Light — Business Data Services
Durban, KwaZulu-Natal, South Africa
"""

LOCATIONS = [
    {
        "area": "Durban Central & Beachfront",
        "address": "Serving Durban CBD, Point Waterfront, & Moses Mabhida Precinct",
        "phone": "+27 31 555 0199",
        "hours": "Mon-Sun: 08:00 - 20:00 (24/7 Event On-Call Support)"
    },
    {
        "area": "Umhlanga & Ballito North Coast",
        "address": "Serving Umhlanga Rocks, Gateway, Sibaya & Ballito",
        "phone": "+27 81 718 1206",
        "hours": "Mon-Sun: 08:00 - 20:00 (24/7 Event On-Call Support)"
    },
    {
        "area": "Upper Highway & Westville",
        "address": "Serving Westville, Kloof, Hillcrest & Pinetown",
        "phone": "+27 81 718 1206",
        "hours": "Mon-Sun: 08:00 - 20:00 (24/7 Event On-Call Support)"
    }
]

# EXACT 6 SERVICES AS REQUESTED BY USER
SERVICES = [
    {
        "id": "live-sound",
        "title": "LIVE SOUND",
        "icon": "speaker",
        "short_desc": "High-fidelity PA speaker systems, subwoofer arrays, and sound engineering for live events, bands, and functions.",
        "features": [
            "Active Line Array & Subwoofer Arrays",
            "Shure & Sennheiser Wireless Microphones",
            "Digital Mixing Consoles & Stage Monitors",
            "On-site Live Sound Technicians"
        ]
    },
    {
        "id": "birthdays",
        "title": "BIRTHDAYS",
        "icon": "sparkles",
        "short_desc": "Full party audio rigs, dynamic dancefloor lighting, and DJ setups tailored for milestone birthday celebrations.",
        "features": [
            "High-Power Party PA System",
            "T-Bar LED Party Lights & Haze",
            "Custom Birthday Playlist Curation",
            "Delivery, Setup & Technical Support"
        ]
    },
    {
        "id": "wedding-dj",
        "title": "WEDDING DJ",
        "icon": "heart",
        "short_desc": "Bespoke wedding reception DJ services, seamless music transitions, speech audio, and ambient lighting.",
        "features": [
            "Professional Wedding DJ & MC Support",
            "Reception Speech Microphones & Sound",
            "Warm Ambient Mood Uplighting",
            "Custom First Dance Song Timing"
        ]
    },
    {
        "id": "ceremoney",
        "title": "CEREMONEY",
        "icon": "sun",
        "short_desc": "Discreet ceremony PA systems, wireless lapel microphones, and prelude music setup for wedding ceremonies.",
        "features": [
            "Discreet Compact Column Speakers",
            "Wireless Lapel & Handheld Microphones",
            "Battery-Powered Outdoor Ceremony Sound",
            "Prelude & Processional Music Control"
        ]
    },
    {
        "id": "dj-service",
        "title": "DJ SERVICE",
        "icon": "disc",
        "short_desc": "Industry-standard pro DJ services for clubs, corporate functions, private parties, and festival stages.",
        "features": [
            "Pioneer CDJ-3000 & DJM-900NXS2 Setup",
            "Versatile Multi-Genre DJ Music Curation",
            "High-Output Booth Monitors",
            "Synchronized DJ Lighting Effects"
        ]
    },
    {
        "id": "equipment-hire",
        "title": "EQUIPMENT HIRE",
        "icon": "tv",
        "short_desc": "Pro audio gear, PA speakers, moving head lights, wireless microphones, and DJ equipment rentals across Durban.",
        "features": [
            "Pro Audio Speakers & Subwoofers",
            "DMX Moving Head Beams & Uplights",
            "Wireless Microphone Packages",
            "Trussing, Staging & Power Distribution"
        ]
    }
]

PACKAGES = [
    {
        "id": "birthday-package",
        "name": "Birthday & Private Party Setup",
        "badge": "Popular Choice",
        "guests": "Up to 150 Guests",
        "price": "R 3,500",
        "description": "Complete sound, party lighting, and DJ setup for birthdays and social gatherings.",
        "includes": [
            "High-Power 15\" Tops + 18\" Subwoofer",
            "Wireless Microphone for Speeches",
            "T-Bar LED Moving Head Party Lights",
            "Fog Machine & Full Setup"
        ]
    },
    {
        "id": "wedding-package",
        "name": "Complete Wedding DJ & Ceremony Rig",
        "badge": "Most Popular",
        "guests": "100 to 350 Guests",
        "price": "R 7,500",
        "description": "Ceremony sound, reception PA, professional wedding DJ, wireless speech mics, and ambient uplighting.",
        "includes": [
            "Discreet Ceremony PA + Lapel Mic",
            "Reception PA System + Dual Subs",
            "12x Ambient Room Uplights",
            "Professional Wedding DJ & Tech Operator"
        ]
    },
    {
        "id": "live-sound-package",
        "name": "Live Sound & Concert Rig",
        "badge": "Full Stage Sound",
        "guests": "500 to 3,000+ Guests",
        "price": "Custom Quote",
        "description": "Line array speaker system and stage monitor mix engineered for live bands and outdoor concerts.",
        "includes": [
            "Ground-stacked or Flown Line Array PA",
            "32-Channel Digital Mixing Console",
            "Stage Monitors & Drum Fill",
            "Dedicated Sound Engineers"
        ]
    },
    {
        "id": "equipment-hire-package",
        "name": "Pro Audio & DJ Equipment Hire",
        "badge": "Gear Rental",
        "guests": "Flexible Capacity",
        "price": "From R 2,500",
        "description": "Dry hire or delivered pro audio, Pioneer DJ CDJs, wireless mics, and lighting rigs.",
        "includes": [
            "Pioneer CDJ-3000 & DJM-900NXS2",
            "Active Powered Loudspeakers",
            "Shure Wireless Microphone Systems",
            "Delivery & Pickup in Durban"
        ]
    }
]

TEAM = [
    {
        "name": "Kieron Govender",
        "role": "Principal Audio Engineer & Director",
        "bio": "Over 14 years of acoustic engineering and live festival sound experience in KwaZulu-Natal.",
        "image": "/static/images/concert_sound.jpg"
    },
    {
        "name": "Nathan Pillay",
        "role": "Senior Lighting Designer & FX Tech",
        "bio": "Specialist in DMX stage lighting and visual atmospheres for concerts, weddings, and parties.",
        "image": "/static/images/hero_stage.jpg"
    },
    {
        "name": "Sarah Naidoo",
        "role": "Head of Event Operations",
        "bio": "Ensures seamless logistics, on-time setup, and flawless execution for events across Durban.",
        "image": "/static/images/wedding_lighting.jpg"
    }
]

BRANDS = [
    {"name": "Pioneer DJ", "category": "DJ Gear"},
    {"name": "RCF Audio", "category": "Pro Audio"},
    {"name": "JBL Professional", "category": "Speakers"},
    {"name": "Chauvet Professional", "category": "Stage Lighting"},
    {"name": "ADJ Lighting", "category": "Intelligent Beams"},
    {"name": "Shure", "category": "Microphones"},
    {"name": "Sennheiser", "category": "Wireless Audio"},
    {"name": "Allen & Heath", "category": "Digital Consoles"}
]
