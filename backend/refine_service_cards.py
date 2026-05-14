import asyncio
import os
import sys
sys.path.append(os.getcwd())
from app.db.mongodb import connect_to_mongo, get_database, close_mongo_connection

async def refine_service_cards():
    await connect_to_mongo()
    db = get_database()
    
    # Refined Service Card Content (exactly 4 per vertical)
    services = {
        "IT Consulting": [
            {"title": "App Development", "desc": "End-to-end web, mobile, and enterprise application development using modern stacks."},
            {"title": "AI & ML Integration", "desc": "Implementing intelligent automation, predictive models, and natural language processing systems."},
            {"title": "Enterprise Solutions", "desc": "Custom CRM, ERP, and RPA deployments to streamline complex business workflows."},
            {"title": "Data Analytics", "desc": "Building powerful data visualization and business intelligence platforms for informed decisions."}
        ],
        "Enterprise Data Centers & Hosting Services": [
            {"title": "Managed Hosting", "desc": "High-performance dedicated server management with 24/7 proactive monitoring."},
            {"title": "Cloud Infrastructure", "desc": "Scalable public, private, and hybrid cloud deployments tailored to enterprise scale."},
            {"title": "Colocation Services", "desc": "Secure, climate-controlled space with redundant power for your own hardware."},
            {"title": "DR & Backup", "desc": "Automated disaster recovery and multi-site backup solutions with near-zero RPO."}
        ],
        "Green Energy & Solar Manufacturing": [
            {"title": "Solar PV Installation", "desc": "Full-scale design and installation of high-efficiency photovoltaic systems for all sectors."},
            {"title": "Rural Electrification", "desc": "Deploying decentralized micro-grids to bring clean energy to off-grid communities."},
            {"title": "Energy Storage", "desc": "Advanced smart battery systems for peak shaving and reliable power backup."},
            {"title": "ESG Consulting", "desc": "Professional energy audits and sustainability roadmaps to maximize carbon reduction."}
        ],
        "Logistics Services": [
            {"title": "Global Freight", "desc": "Integrated sea, air, and land freight forwarding services with real-time tracking."},
            {"title": "Supply Chain Management", "desc": "Strategic end-to-end logistics planning to reduce lead times and costs."},
            {"title": "Last-Mile Delivery", "desc": "Efficient direct-to-consumer distribution networks for e-commerce and retail."},
            {"title": "Cold Chain Solutions", "desc": "Temperature-controlled transport and storage for perishable and medical goods."}
        ],
        "Export & Import": [
            {"title": "Agri-Export", "desc": "Sourcing and shipping premium exotic fruits and fresh vegetables to global markets."},
            {"title": "Bulk Commodities", "desc": "Trade and distribution of high-demand agricultural products and natural oils."},
            {"title": "Quality Assurance", "desc": "Rigorous testing and certification to meet international food safety standards."},
            {"title": "Supply Chain Trade", "desc": "Leveraging our own logistics network to provide faster, more reliable global trade."}
        ],
        "IT Training": [
            {"title": "Software Engineering", "desc": "Intensive bootcamps in Full-Stack development, Java, Python, and modern frameworks."},
            {"title": "Cloud & DevOps", "desc": "Hands-on certification programs for AWS, Azure, and infrastructure automation."},
            {"title": "Cybersecurity Academy", "desc": "Professional training in ethical hacking, network defense, and threat analysis."},
            {"title": "Corporate Upskilling", "desc": "Custom-designed talent development programs for enterprise teams and new hires."}
        ],
        "Yoga & Wellness": [
            {"title": "Asana & Pranayama", "desc": "Expert-led yoga classes focused on physical alignment and breath control."},
            {"title": "Meditation Retreats", "desc": "Guided mindfulness and stress-reduction programs for mental clarity."},
            {"title": "Holistic Healing", "desc": "Personalized wellness consulting integrating traditional wisdom and modern health."},
            {"title": "Teacher Training", "desc": "Globally recognized yoga certification courses to develop future wellness leaders."}
        ],
        "Plantations & Exotic Trees": [
            {"title": "Timber Management", "desc": "Large-scale cultivation and management of high-value Teak and Sandalwood."},
            {"title": "Exotic Orchards", "desc": "Specialized production of premium dragon fruit, avocado, and seasonal exotic fruits."},
            {"title": "Natural Assets", "desc": "Long-term asset management through sustainable forestry and carbon sequestration."},
            {"title": "Nursery Services", "desc": "Supplying rare and exotic saplings for commercial and private landscaping."}
        ],
        "Property Services": [
            {"title": "Real Estate Sales", "desc": "Expert brokerage for luxury residences, commercial plots, and industrial land."},
            {"title": "Property Management", "desc": "End-to-end maintenance, leasing, and tenant management for property owners."},
            {"title": "Investment Advisory", "desc": "Strategic real estate portfolio planning and valuation services for long-term growth."},
            {"title": "Legal & Compliance", "desc": "Handling all documentation, clear titles, and regulatory approvals for properties."}
        ],
        "Travel & Rentals": [
            {"title": "Premium Fleet Rental", "desc": "Luxury cars, buses, and executive vehicles for travel and special events."},
            {"title": "Custom Tour Packages", "desc": "Bespoke international and domestic holiday itineraries tailored to your needs."},
            {"title": "Corporate Mobility", "desc": "Dedicated employee transport and business travel desk services."},
            {"title": "Tourism Services", "desc": "Guided heritage tours and specialized destination management across the region."}
        ]
    }

    for sub_name, card_list in services.items():
        print(f"Refining services for: {sub_name}")
        
        # 1. Get current service cards to preserve images (which were already pexels URLs)
        existing = await db["universal_content"].find({
            "mainPage": "Business Verticals",
            "subSection": sub_name,
            "category": "Our Business"
        }).sort("order", 1).to_list(length=4)
        
        # 2. Update each card
        for i, service_data in enumerate(card_list):
            # Fallback image if for some reason list length mismatch
            img = existing[i]["image"] if i < len(existing) else "https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg"
            
            await db["universal_content"].update_many(
                {
                    "mainPage": "Business Verticals",
                    "subSection": sub_name,
                    "category": "Our Business",
                    "order": i
                },
                {
                    "$set": {
                        "title": service_data["title"],
                        "description": service_data["desc"],
                        "image": img
                    }
                }
            )
            
    print("All service cards refined to specifically expose provided services.")
    await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(refine_service_cards())
