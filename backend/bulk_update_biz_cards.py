import asyncio
import os
import sys
sys.path.append(os.getcwd())
from app.db.mongodb import connect_to_mongo, get_database, close_mongo_connection

async def seed_business_pages():
    await connect_to_mongo()
    db = get_database()
    
    # Define the new content structure
    biz_pages = [
        {
            "subSection": "IT Consulting",
            "cards": [
                {
                    "title": "Digital Transformation",
                    "description": "Web, mobile, and enterprise application development powered by AI/ML solutions and automation systems.",
                    "image": "/uploads/it_consulting.png"
                },
                {
                    "title": "AI & Automation",
                    "description": "Intelligent CRM, RPA, and data analytics systems designed for scalable high-margin growth.",
                    "image": "/uploads/it_consulting.png"
                },
                {
                    "title": "Sustainable IT",
                    "description": "Paperless workflows and energy-efficient system architectures reducing operational waste.",
                    "image": "/uploads/it_consulting.png"
                }
            ]
        },
        {
            "subSection": "Enterprise Data Centers & Hosting Services",
            "cards": [
                {
                    "title": "Managed Hosting",
                    "description": "Premium domain services and managed hosting with infrastructure ownership for full client lifecycle control.",
                    "image": "/uploads/cloud_hosting.png"
                },
                {
                    "title": "Cloud Deployments",
                    "description": "Scalable cloud deployments and infrastructure optimization for high-performance enterprise needs.",
                    "image": "/uploads/cloud_hosting.png"
                },
                {
                    "title": "Energy Efficiency",
                    "description": "Optimized server usage and efficient resource allocation leading to reduced carbon footprints.",
                    "image": "/uploads/cloud_hosting.png"
                }
            ]
        },
        {
            "subSection": "Green Energy & Solar Manufacturing",
            "cards": [
                {
                    "title": "Solar Energy Deployment",
                    "description": "High-impact solar energy projects aligned with global ESG trends and clean energy adoption.",
                    "image": "/uploads/solar_energy.png"
                },
                {
                    "title": "Rural Electrification",
                    "description": "Support for decentralized power systems and rural electrification projects using renewable sources.",
                    "image": "/uploads/solar_energy.png"
                },
                {
                    "title": "Future Ready",
                    "description": "Positioning the group at the forefront of sustainability through global green partnerships.",
                    "image": "/uploads/solar_energy.png"
                }
            ]
        },
        {
            "subSection": "Logistics Services",
            "cards": [
                {
                    "title": "Supply Chain Management",
                    "description": "Operational backbone enabling vertical integration across trade, tourism, and supply chains.",
                    "image": "/uploads/logistics_trade.png"
                },
                {
                    "title": "Route Optimization",
                    "description": "Fuel-efficient logistics operations through advanced route optimization and service integration.",
                    "image": "/uploads/logistics_trade.png"
                }
            ]
        },
        {
            "subSection": "Export & Import",
            "cards": [
                {
                    "title": "Global Trade",
                    "description": "Export-import of fresh vegetables and exotic fruits across B2B and D2C markets.",
                    "image": "/uploads/logistics_trade.png"
                },
                {
                    "title": "Asset-Backed Stability",
                    "description": "Diversifying revenue into real assets and global trade to hedge against tech volatility.",
                    "image": "/uploads/logistics_trade.png"
                }
            ]
        },
        {
            "subSection": "IT Training",
            "cards": [
                {
                    "title": "Academy & Skilling Hub",
                    "description": "Professional IT skilling programs and career readiness initiatives to create a talent pipeline.",
                    "image": "/uploads/it_skilling.png"
                },
                {
                    "title": "Social Sustainability",
                    "description": "Building long-term social value via employability and digital-first learning initiatives.",
                    "image": "/uploads/it_skilling.png"
                }
            ]
        }
    ]

    for page in biz_pages:
        sub_name = page["subSection"]
        print(f"Updating cards for: {sub_name}")
        
        # 1. Remove existing 'Our Business' cards for this subSection
        await db["universal_content"].delete_many({
            "mainPage": "Business Verticals",
            "subSection": sub_name,
            "category": "Our Business"
        })
        
        # 2. Insert new cards
        for i, card in enumerate(page["cards"]):
            doc = {
                "mainPage": "Business Verticals",
                "subSection": sub_name,
                "category": "Our Business",
                "title": card["title"],
                "description": card["description"],
                "image": card["image"],
                "isActive": True,
                "order": i
            }
            await db["universal_content"].insert_one(doc)
            
    print("Business cards update complete.")
    await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(seed_business_pages())
