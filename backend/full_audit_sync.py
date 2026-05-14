import asyncio
import os
import sys
sys.path.append(os.getcwd())
from app.db.mongodb import connect_to_mongo, get_database, close_mongo_connection

async def audit_all_pages():
    await connect_to_mongo()
    db = get_database()
    
    local_base = "/static/images/vjs_business/"
    
    # Auditing and finalizing the remaining 5 business pages
    config = {
        "IT Training": {
            "services": [
                {"title": "Software Engineering", "desc": "Intensive bootcamps in Full-Stack development, Java, Python, and modern frameworks.", "img": "https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg"},
                {"title": "Cloud & DevOps", "desc": "Hands-on certification programs for AWS, Azure, and infrastructure automation.", "img": "https://images.pexels.com/photos/325229/pexels-photo-325229.jpeg"},
                {"title": "AI & Data Science", "desc": "Python-based ML and big data analytics training for the future of tech.", "img": local_base + "woman-presenting-artificial-intelligence-technolog-2026-01-09-13-01-03-utc.jpg"},
                {"title": "Cybersecurity", "desc": "Ethical hacking and network protection courses for aspiring security professionals.", "img": local_base + "cyber-security-message-with-padlock-and-letter-til-2026-01-08-05-42-34-utc.jpg"}
            ],
            "glance": [
                {"title": "Job Ready", "desc": "Practical training programs designed to make students industry-ready from day one.", "img": local_base + "diverse-group-of-children-in-modern-school-class-2026-03-19-22-08-17-utc.jpg"},
                {"title": "Expert Mentors", "desc": "Learning from industry professionals with real-world project experience.", "img": "https://images.pexels.com/photos/1181359/pexels-photo-1181359.jpeg"},
                {"title": "Certification", "desc": "Achieve globally recognized IT credentials to accelerate your career growth.", "img": "https://images.pexels.com/photos/3760067/pexels-photo-3760067.jpeg"}
            ]
        },
        "Yoga & Wellness": {
            "services": [
                {"title": "Asana Mastery", "desc": "Expert-led yoga classes focused on physical alignment, strength, and flexibility.", "img": "https://images.pexels.com/photos/3759657/pexels-photo-3759657.jpeg"},
                {"title": "Meditation", "desc": "Deep relaxation and mental clarity sessions to reduce stress and improve focus.", "img": "https://images.pexels.com/photos/3822906/pexels-photo-3822906.jpeg"},
                {"title": "Holistic Healing", "desc": "Personalized wellness consulting integrating traditional wisdom with modern health.", "img": "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg"},
                {"title": "Wellness Programs", "desc": "Comprehensive health and wellness programs for individuals and corporate teams.", "img": local_base + "medical-professional-examines-child-outdoors-on-su-2026-03-25-02-51-48-utc.jpg"}
            ],
            "glance": [
                {"title": "Inner Peace", "desc": "A dedicated academy for holistic self-healing, yoga, and mindfulness.", "img": local_base + "hands-holding-singing-bowl-outdoors-for-meditation-2026-01-05-06-14-41-utc.jpg"},
                {"title": "Mindful Living", "desc": "Wellness programs tailored for modern, high-stress lifestyles.", "img": local_base + "group-of-seniors-enjoying-yoga-in-the-park-2026-03-24-01-29-52-utc.jpg"},
                {"title": "Body Balance", "desc": "Achieving physical and mental harmony through natural practices.", "img": "https://images.pexels.com/photos/4056723/pexels-photo-4056723.jpeg"}
            ]
        },
        "Plantations & Exotic Trees": {
            "services": [
                {"title": "Timber Management", "desc": "Large-scale cultivation and management of high-value Teak and Sandalwood.", "img": "https://images.pexels.com/photos/1632790/pexels-photo-1632790.jpeg"},
                {"title": "Exotic Orchards", "desc": "Specialized production of premium dragon fruit, avocado, and seasonal exotic fruits.", "img": "https://images.pexels.com/photos/1132047/pexels-photo-1132047.jpeg"},
                {"title": "Carbon Offsets", "desc": "Environmental conservation projects aimed at carbon sequestration and biodiversity.", "img": "https://images.pexels.com/photos/1108572/pexels-photo-1108572.jpeg"},
                {"title": "Nursery Services", "desc": "Supplying rare and exotic saplings for commercial and private landscaping.", "img": "https://images.pexels.com/photos/3820380/pexels-photo-3820380.jpeg"}
            ],
            "glance": [
                {"title": "Green Assets", "desc": "Long-term investment in natural wealth through sustainable forestry.", "img": local_base + "pathway-winding-through-a-lush-forest-of-tall-tree-2026-03-18-08-25-55-utc.jpg"},
                {"title": "Exotic Growth", "desc": "Cultivating rare and valuable tree species for premium markets.", "img": local_base + "new-seedling-growing-on-moss-in-sunlight-2026-03-24-10-24-42-utc.jpg"},
                {"title": "Biodiversity", "desc": "Maintaining balanced and healthy ecosystem plantations for the future.", "img": "https://images.pexels.com/photos/1072179/pexels-photo-1072179.jpeg"}
            ]
        },
        "Property Services": {
            "services": [
                {"title": "Real Estate Sales", "desc": "Expert brokerage for luxury residences, commercial plots, and industrial land.", "img": "https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg"},
                {"title": "Leasing Services", "desc": "Professional property management and leasing for owners and tenants.", "img": "https://images.pexels.com/photos/280222/pexels-photo-280222.jpeg"},
                {"title": "Commercial Space", "desc": "Sourcing and managing modern office and retail infrastructure.", "img": "https://images.pexels.com/photos/3183153/pexels-photo-3183153.jpeg"},
                {"title": "Legal Compliance", "desc": "Ensuring clear titles and full regulatory approvals for all transactions.", "img": "https://images.pexels.com/photos/811587/pexels-photo-811587.jpeg"}
            ],
            "glance": [
                {"title": "Asset Growth", "desc": "Helping clients preserve and grow wealth through strategic real estate.", "img": local_base + "real-estate-agent-and-customers-shaking-hands-toge-2026-01-08-02-17-35-utc.jpg"},
                {"title": "Prime Design", "desc": "Partnering with top architects for modern and sustainable home designs.", "img": local_base + "architectural-design-team-meeting-about-new-home-2026-03-16-00-36-36-utc.jpg"},
                {"title": "Location Expert", "desc": "Sourcing high-valuation land in the most sought-after locations.", "img": "https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg"}
            ]
        },
        "Travel & Rentals": {
            "services": [
                {"title": "Premium Rentals", "desc": "Luxury car and coach rentals for business and leisure travel.", "img": "https://images.pexels.com/photos/116675/pexels-photo-116675.jpeg"},
                {"title": "Tour Packages", "desc": "All-inclusive international and domestic holiday packages tailored to you.", "img": "https://images.pexels.com/photos/237272/pexels-photo-237272.jpeg"},
                {"title": "Corporate Mobility", "desc": "Dedicated travel desk and employee transport services for enterprises.", "img": "https://images.pexels.com/photos/3183153/pexels-photo-3183153.jpeg"},
                {"title": "Local Tourism", "desc": "Exploring heritage sites and hidden gems with expert-led tours.", "img": "https://images.pexels.com/photos/1051073/pexels-photo-1051073.jpeg"}
            ],
            "glance": [
                {"title": "Expert Travel", "desc": "Creating memorable tourism experiences with professional planning.", "img": "https://images.pexels.com/photos/237272/pexels-photo-237272.jpeg"},
                {"title": "Safe Journey", "desc": "Vetted drivers and a premium fleet for absolute peace of mind.", "img": "https://images.pexels.com/photos/116675/pexels-photo-116675.jpeg"},
                {"title": "Global Reach", "desc": "Customized international travel packages across the globe.", "img": "https://images.pexels.com/photos/1051073/pexels-photo-1051073.jpeg"}
            ]
        }
    }

    for sub_name, data in config.items():
        print(f"Final Audit for: {sub_name}")
        
        # Update Glance
        for i, card in enumerate(data["glance"]):
            await db["universal_content"].update_many(
                {"mainPage": "Business Verticals", "subSection": sub_name, "category": "At a Glance", "order": i},
                {"$set": {"title": card["title"], "description": card["desc"], "image": card["img"]}}
            )
            
        # Update Business
        for i, card in enumerate(data["services"]):
            await db["universal_content"].update_many(
                {"mainPage": "Business Verticals", "subSection": sub_name, "category": "Our Business", "order": i},
                {"$set": {"title": card["title"], "description": card["desc"], "image": card["img"]}}
            )
            
    print("Full audit and synchronization of all 10 business pages complete.")
    await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(audit_all_pages())
