import asyncio
import os
import sys
sys.path.append(os.getcwd())
from app.db.mongodb import connect_to_mongo, get_database, close_mongo_connection

async def update_all_biz_cards():
    await connect_to_mongo()
    db = get_database()
    
    # Configuration for all pages
    # Structure: 3 Glance Cards, 4 Business Cards per page
    config = {
        "IT Consulting": {
            "glance": [
                {"title": "Agile Development", "desc": "Fast-paced development cycles with high-quality output.", "img": "https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg"},
                {"title": "Cloud Native", "desc": "Building for the future on scalable cloud architectures.", "img": "https://images.pexels.com/photos/373543/pexels-photo-373543.jpeg"},
                {"title": "AI Ready", "desc": "Harnessing the power of machine learning for business.", "img": "https://images.pexels.com/photos/8386440/pexels-photo-8386440.jpeg"}
            ],
            "business": [
                {"title": "Software Dev", "desc": "Custom enterprise applications for web and mobile.", "img": "https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg"},
                {"title": "Automation", "desc": "Reducing overhead with intelligent RPA and CRM.", "img": "https://images.pexels.com/photos/3182812/pexels-photo-3182812.jpeg"},
                {"title": "Data Analytics", "desc": "Turning raw data into actionable intelligence.", "img": "https://images.pexels.com/photos/590022/pexels-photo-590022.jpeg"},
                {"title": "Cybersecurity", "desc": "Protecting your digital perimeter from threats.", "img": "https://images.pexels.com/photos/60504/security-protection-anti-virus-software-60504.jpeg"}
            ]
        },
        "Enterprise Data Centers & Hosting Services": {
            "glance": [
                {"title": "99.9% Uptime", "desc": "Tier III standard reliability for critical operations.", "img": "https://images.pexels.com/photos/2582937/pexels-photo-2582937.jpeg"},
                {"title": "Green Data", "desc": "Energy-efficient cooling and power systems.", "img": "https://images.pexels.com/photos/1148820/pexels-photo-1148820.jpeg"},
                {"title": "Max Security", "desc": "Biometric access and 24/7 physical surveillance.", "img": "https://images.pexels.com/photos/60504/security-protection-anti-virus-software-60504.jpeg"}
            ],
            "business": [
                {"title": "Managed Hosting", "desc": "Dedicated servers with proactive monitoring.", "img": "https://images.pexels.com/photos/2582931/pexels-photo-2582931.jpeg"},
                {"title": "Cloud Infra", "desc": "Flexible, scalable virtual private servers.", "img": "https://images.pexels.com/photos/325229/pexels-photo-325229.jpeg"},
                {"title": "Domain Hub", "desc": "White-label domain registration and DNS.", "img": "https://images.pexels.com/photos/163097/computer-workplace-desk-laptop-163097.jpeg"},
                {"title": "Disaster Recovery", "desc": "Automated backups and instant failover.", "img": "https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg"}
            ]
        },
        "Green Energy & Solar Manufacturing": {
            "glance": [
                {"title": "Solar Future", "desc": "Harnessing the sun for a sustainable future.", "img": "https://images.pexels.com/photos/356036/pexels-photo-356036.jpeg"},
                {"title": "Eco Innovation", "desc": "Cutting-edge photovoltaic module tech.", "img": "https://images.pexels.com/photos/414860/pexels-photo-414860.jpeg"},
                {"title": "Sustainability", "desc": "Reducing reliance on carbon-heavy power.", "img": "https://images.pexels.com/photos/1108572/pexels-photo-1108572.jpeg"}
            ],
            "business": [
                {"title": "Solar Install", "desc": "Turnkey solutions for home and business.", "img": "https://images.pexels.com/photos/2800832/pexels-photo-2800832.jpeg"},
                {"title": "Performance Care", "desc": "Regular cleaning and system optimization.", "img": "https://images.pexels.com/photos/9875441/pexels-photo-9875441.jpeg"},
                {"title": "Smart Storage", "desc": "Storing excess energy for peak hours.", "img": "https://images.pexels.com/photos/356036/pexels-photo-356036.jpeg"},
                {"title": "Energy Audit", "desc": "Professional audits to maximize efficiency.", "img": "https://images.pexels.com/photos/159213/hall-congress-architecture-building-159213.jpeg"}
            ]
        },
        "Logistics Services": {
            "glance": [
                {"title": "Global Reach", "desc": "Integrated supply chain solutions worldwide.", "img": "https://images.pexels.com/photos/1556704/pexels-photo-1556704.jpeg"},
                {"title": "Speed & Safety", "desc": "Ensuring timely delivery with zero damage.", "img": "https://images.pexels.com/photos/6169033/pexels-photo-6169033.jpeg"},
                {"title": "Real-time Tracking", "desc": "Full visibility into your shipment status.", "img": "https://images.pexels.com/photos/6169668/pexels-photo-6169668.jpeg"}
            ],
            "business": [
                {"title": "Freight Forward", "desc": "Efficient sea and air freight logistics.", "img": "https://images.pexels.com/photos/2199293/pexels-photo-2199293.jpeg"},
                {"title": "Warehousing", "desc": "Secure storage and inventory management.", "img": "https://images.pexels.com/photos/236705/pexels-photo-236705.jpeg"},
                {"title": "Last Mile", "desc": "Direct-to-consumer delivery services.", "img": "https://images.pexels.com/photos/4391470/pexels-photo-4391470.jpeg"},
                {"title": "Supply Chain", "desc": "End-to-end operational integration.", "img": "https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg"}
            ]
        },
        "Export & Import": {
            "glance": [
                {"title": "Fresh Quality", "desc": "Sourcing the finest exotic fruits & veg.", "img": "https://images.pexels.com/photos/1132047/pexels-photo-1132047.jpeg"},
                {"title": "Global Network", "desc": "Connecting farmers to global markets.", "img": "https://images.pexels.com/photos/1123260/pexels-photo-1123260.jpeg"},
                {"title": "Certified Safe", "desc": "Meeting international food safety standards.", "img": "https://images.pexels.com/photos/2255938/pexels-photo-2255938.jpeg"}
            ],
            "business": [
                {"title": "Exotic Produce", "desc": "Export of premium dragon fruit and berries.", "img": "https://images.pexels.com/photos/1435735/pexels-photo-1435735.jpeg"},
                {"title": "B2B Trade", "desc": "Bulk supply for retailers and wholesalers.", "img": "https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg"},
                {"title": "Direct-to-Home", "desc": "Fresh farm-to-table delivery subscriptions.", "img": "https://images.pexels.com/photos/4391470/pexels-photo-4391470.jpeg"},
                {"title": "Natural Oils", "desc": "Import of pure essential and exotic oils.", "img": "https://images.pexels.com/photos/3951628/pexels-photo-3951628.jpeg"}
            ]
        },
        "IT Training": {
            "glance": [
                {"title": "Job Ready", "desc": "Practical training for the modern IT world.", "img": "https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg"},
                {"title": "Expert Mentors", "desc": "Learning from industry professionals.", "img": "https://images.pexels.com/photos/1181359/pexels-photo-1181359.jpeg"},
                {"title": "Certification", "desc": "Globally recognized IT credentials.", "img": "https://images.pexels.com/photos/3760067/pexels-photo-3760067.jpeg"}
            ],
            "business": [
                {"title": "Full Stack Dev", "desc": "Mastering web technologies from MERN to Java.", "img": "https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg"},
                {"title": "Cloud Computing", "desc": "AWS and Azure cloud architecture training.", "img": "https://images.pexels.com/photos/325229/pexels-photo-325229.jpeg"},
                {"title": "AI & Data Science", "desc": "Python-based ML and big data analytics.", "img": "https://images.pexels.com/photos/590022/pexels-photo-590022.jpeg"},
                {"title": "Cyber Security", "desc": "Ethical hacking and network protection.", "img": "https://images.pexels.com/photos/60504/security-protection-anti-virus-software-60504.jpeg"}
            ]
        },
        "Yoga & Wellness": {
            "glance": [
                {"title": "Inner Peace", "desc": "Holistic self-healing and yoga academy.", "img": "https://images.pexels.com/photos/3822906/pexels-photo-3822906.jpeg"},
                {"title": "Mindful Living", "desc": "Wellness programs for modern lifestyles.", "img": "https://images.pexels.com/photos/3759657/pexels-photo-3759657.jpeg"},
                {"title": "Body Balance", "desc": "Achieving physical and mental harmony.", "img": "https://images.pexels.com/photos/4056723/pexels-photo-4056723.jpeg"}
            ],
            "business": [
                {"title": "Asana Mastery", "desc": "Guided sessions for all skill levels.", "img": "https://images.pexels.com/photos/3759657/pexels-photo-3759657.jpeg"},
                {"title": "Meditation", "desc": "Deep relaxation and mental clarity hub.", "img": "https://images.pexels.com/photos/3822906/pexels-photo-3822906.jpeg"},
                {"title": "Nutritional Care", "desc": "Balanced diet and wellness consulting.", "img": "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg"},
                {"title": "Teacher Training", "desc": "Professional yoga certification courses.", "img": "https://images.pexels.com/photos/4056723/pexels-photo-4056723.jpeg"}
            ]
        },
        "Plantations & Exotic Trees": {
            "glance": [
                {"title": "Green Assets", "desc": "Long-term investment in natural wealth.", "img": "https://images.pexels.com/photos/1108572/pexels-photo-1108572.jpeg"},
                {"title": "Exotic Growth", "desc": "Cultivating rare and valuable tree species.", "img": "https://images.pexels.com/photos/3820380/pexels-photo-3820380.jpeg"},
                {"title": "Biodiversity", "desc": "Maintaining balanced ecosystem plantations.", "img": "https://images.pexels.com/photos/1072179/pexels-photo-1072179.jpeg"}
            ],
            "business": [
                {"title": "Teak & Sandal", "desc": "High-value timber plantation management.", "img": "https://images.pexels.com/photos/1632790/pexels-photo-1632790.jpeg"},
                {"title": "Fruit Orchards", "desc": "Exotic dragon fruit and avocado groves.", "img": "https://images.pexels.com/photos/1132047/pexels-photo-1132047.jpeg"},
                {"title": "Carbon Offsets", "desc": "Environmental conservation and credits.", "img": "https://images.pexels.com/photos/1108572/pexels-photo-1108572.jpeg"},
                {"title": "Garden Design", "desc": "Professional landscaping and exotic plants.", "img": "https://images.pexels.com/photos/3820380/pexels-photo-3820380.jpeg"}
            ]
        },
        "Property Services": {
            "glance": [
                {"title": "Asset Growth", "desc": "Wealth preservation via real estate.", "img": "https://images.pexels.com/photos/280222/pexels-photo-280222.jpeg"},
                {"title": "Prime Location", "desc": "Sourcing high-valuation land and homes.", "img": "https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg"},
                {"title": "Legal Trust", "desc": "Clear titles and transparent transactions.", "img": "https://images.pexels.com/photos/811587/pexels-photo-811587.jpeg"}
            ],
            "business": [
                {"title": "Residential Sales", "desc": "Luxury homes and affordable apartments.", "img": "https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg"},
                {"title": "Commercial Space", "desc": "Modern office and retail infrastructure.", "img": "https://images.pexels.com/photos/3183153/pexels-photo-3183153.jpeg"},
                {"title": "Plot Dev", "desc": "Gated community and residential plots.", "img": "https://images.pexels.com/photos/101808/pexels-photo-101808.jpeg"},
                {"title": "Leasing", "desc": "Professional property management hub.", "img": "https://images.pexels.com/photos/3182812/pexels-photo-3182812.jpeg"}
            ]
        },
        "Travel & Rentals": {
            "glance": [
                {"title": "Expert Travel", "desc": "Memorable tourism and rental experiences.", "img": "https://images.pexels.com/photos/237272/pexels-photo-237272.jpeg"},
                {"title": "Safe Journey", "desc": "Vetted drivers and premium fleet rentals.", "img": "https://images.pexels.com/photos/116675/pexels-photo-116675.jpeg"},
                {"title": "Global Tours", "desc": "Customized international travel packages.", "img": "https://images.pexels.com/photos/1051073/pexels-photo-1051073.jpeg"}
            ],
            "business": [
                {"title": "Fleet Rental", "desc": "Luxury cars and buses for all occasions.", "img": "https://images.pexels.com/photos/116675/pexels-photo-116675.jpeg"},
                {"title": "Holiday Packages", "desc": "All-inclusive family and solo tours.", "img": "https://images.pexels.com/photos/237272/pexels-photo-237272.jpeg"},
                {"title": "Corporate Travel", "desc": "Dedicated travel desk for business groups.", "img": "https://images.pexels.com/photos/3183153/pexels-photo-3183153.jpeg"},
                {"title": "Local Tourism", "desc": "Exploring hidden gems and heritage sites.", "img": "https://images.pexels.com/photos/1051073/pexels-photo-1051073.jpeg"}
            ]
        }
    }

    for sub_name, items in config.items():
        print(f"Syncing: {sub_name}")
        
        # Clean existing cards for both categories
        await db["universal_content"].delete_many({
            "mainPage": "Business Verticals",
            "subSection": sub_name,
            "category": {"$in": ["At a Glance", "Our Business"]}
        })
        
        # Add Glance Cards (exactly 3)
        for i, card in enumerate(items["glance"]):
            await db["universal_content"].insert_one({
                "mainPage": "Business Verticals",
                "subSection": sub_name,
                "category": "At a Glance",
                "title": card["title"],
                "description": card["desc"],
                "image": card["img"],
                "isActive": True,
                "order": i
            })
            
        # Add Business Cards (exactly 4)
        for i, card in enumerate(items["business"]):
            await db["universal_content"].insert_one({
                "mainPage": "Business Verticals",
                "subSection": sub_name,
                "category": "Our Business",
                "title": card["title"],
                "description": card["desc"],
                "image": card["img"],
                "isActive": True,
                "order": i
            })
            
    print("All business pages synchronized successfully.")
    await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(update_all_biz_cards())
