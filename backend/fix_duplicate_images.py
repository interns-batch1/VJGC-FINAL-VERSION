import asyncio
import os
import sys
sys.path.append(os.getcwd())
from app.db.mongodb import connect_to_mongo, get_database, close_mongo_connection

async def fix_duplicate_images():
    await connect_to_mongo()
    db = get_database()
    
    local_base = "/static/images/vjs_business/"
    
    # Mixed mapping: Using Local VJGC images where they fit perfectly, 
    # and professional Pexels images for the rest to ensure ZERO duplicates.
    mapping = {
        "IT Consulting": {
            "glance": [
                local_base + "project-flowchart-on-laptop-for-business-concepts-2026-01-06-10-01-03-utc.jpg",
                local_base + "business-professional-using-cloud-computing-techno-2026-01-11-08-44-25-utc.jpg",
                local_base + "woman-presenting-artificial-intelligence-technolog-2026-01-09-13-01-03-utc.jpg"
            ],
            "business": [
                "https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg",
                "https://images.pexels.com/photos/8386440/pexels-photo-8386440.jpeg",
                "https://images.pexels.com/photos/3182812/pexels-photo-3182812.jpeg",
                local_base + "cloud-computing-security-and-data-flow-concepts-2026-01-06-09-27-15-utc.jpg"
            ]
        },
        "Enterprise Data Centers & Hosting Services": {
            "glance": [
                local_base + "worker-stands-among-servers-in-a-data-center-2026-01-09-11-11-16-utc.jpg",
                local_base + "engineers-shaking-hands-in-data-center-2026-01-08-00-16-12-utc.jpg",
                local_base + "cyber-security-message-with-padlock-and-letter-til-2026-01-08-05-42-34-utc.jpg"
            ],
            "business": [
                "https://images.pexels.com/photos/2582931/pexels-photo-2582931.jpeg",
                local_base + "data-center-coworkers-doing-brainstorming-monitor-2026-01-11-10-54-31-utc.jpg",
                local_base + "wooden-man-holding-a-domain-name-block-2026-03-16-02-11-23-utc.jpg",
                "https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg"
            ]
        },
        "Green Energy & Solar Manufacturing": {
            "glance": [
                local_base + "wind-generator-and-high-voltage-lines-in-a-field-2026-03-19-09-34-54-utc.jpg",
                local_base + "green-solar-cell-house-and-leaf-on-coin-stack-sus-2026-03-25-09-49-28-utc.jpg",
                local_base + "back-of-professional-engineer-worker-or-technicia-2026-03-23-23-01-20-utc.jpg"
            ],
            "business": [
                "https://images.pexels.com/photos/2800832/pexels-photo-2800832.jpeg",
                "https://images.pexels.com/photos/414860/pexels-photo-414860.jpeg",
                "https://images.pexels.com/photos/356036/pexels-photo-356036.jpeg",
                "https://images.pexels.com/photos/159213/hall-congress-architecture-building-159213.jpeg"
            ]
        },
        "Logistics Services": {
            "glance": [
                local_base + "shipping-containers-at-port-at-sunset-2026-03-24-11-22-01-utc.jpg",
                local_base + "worker-inspecting-cargo-containers-in-a-shipping-y-2026-04-16-19-03-40-utc.jpg",
                local_base + "online-shopping-supply-chain-on-light-blue-backgro-2026-03-17-04-24-33-utc.jpg"
            ],
            "business": [
                "https://images.pexels.com/photos/2199293/pexels-photo-2199293.jpeg",
                local_base + "truck-inspector-with-clipboard-in-a-fleet-setting-2026-03-26-06-04-42-utc.jpg",
                local_base + "delivery-person-handing-box-to-customer-outside-2026-03-25-02-18-23-utc.jpg",
                "https://images.pexels.com/photos/236705/pexels-photo-236705.jpeg"
            ]
        },
        "Export & Import": {
            "glance": [
                local_base + "fresh-fruits-and-vegetables-in-a-basket-2026-01-09-15-04-22-utc.jpg",
                local_base + "successful-farmer-handshake-at-market-with-fresh-v-2026-01-09-08-34-52-utc.jpg",
                local_base + "scientists-examined-the-quality-of-vegetable-organ-2026-03-20-05-45-32-utc.jpg"
            ],
            "business": [
                "https://images.pexels.com/photos/1132047/pexels-photo-1132047.jpeg",
                "https://images.pexels.com/photos/1123260/pexels-photo-1123260.jpeg",
                "https://images.pexels.com/photos/2255938/pexels-photo-2255938.jpeg",
                "https://images.pexels.com/photos/1435735/pexels-photo-1435735.jpeg"
            ]
        },
        "IT Training": {
            "glance": [
                local_base + "diverse-group-of-children-in-modern-school-class-2026-03-19-22-08-17-utc.jpg",
                "https://images.pexels.com/photos/1181359/pexels-photo-1181359.jpeg",
                "https://images.pexels.com/photos/3760067/pexels-photo-3760067.jpeg"
            ],
            "business": [
                "https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg",
                "https://images.pexels.com/photos/325229/pexels-photo-325229.jpeg",
                "https://images.pexels.com/photos/590022/pexels-photo-590022.jpeg",
                "https://images.pexels.com/photos/60504/security-protection-anti-virus-software-60504.jpeg"
            ]
        },
        "Yoga & Wellness": {
            "glance": [
                local_base + "hands-holding-singing-bowl-outdoors-for-meditation-2026-01-05-06-14-41-utc.jpg",
                local_base + "group-of-seniors-enjoying-yoga-in-the-park-2026-03-24-01-29-52-utc.jpg",
                "https://images.pexels.com/photos/4056723/pexels-photo-4056723.jpeg"
            ],
            "business": [
                "https://images.pexels.com/photos/3759657/pexels-photo-3759657.jpeg",
                "https://images.pexels.com/photos/3822906/pexels-photo-3822906.jpeg",
                "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg",
                local_base + "medical-professional-examines-child-outdoors-on-su-2026-03-25-02-51-48-utc.jpg"
            ]
        },
        "Plantations & Exotic Trees": {
            "glance": [
                local_base + "pathway-winding-through-a-lush-forest-of-tall-tree-2026-03-18-08-25-55-utc.jpg",
                local_base + "new-seedling-growing-on-moss-in-sunlight-2026-03-24-10-24-42-utc.jpg",
                "https://images.pexels.com/photos/1072179/pexels-photo-1072179.jpeg"
            ],
            "business": [
                "https://images.pexels.com/photos/1632790/pexels-photo-1632790.jpeg",
                "https://images.pexels.com/photos/1132047/pexels-photo-1132047.jpeg",
                "https://images.pexels.com/photos/1108572/pexels-photo-1108572.jpeg",
                "https://images.pexels.com/photos/3820380/pexels-photo-3820380.jpeg"
            ]
        },
        "Property Services": {
            "glance": [
                local_base + "real-estate-agent-and-customers-shaking-hands-toge-2026-01-08-02-17-35-utc.jpg",
                local_base + "architectural-design-team-meeting-about-new-home-2026-03-16-00-36-36-utc.jpg",
                "https://images.pexels.com/photos/811587/pexels-photo-811587.jpeg"
            ],
            "business": [
                "https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg",
                "https://images.pexels.com/photos/3183153/pexels-photo-3183153.jpeg",
                "https://images.pexels.com/photos/101808/pexels-photo-101808.jpeg",
                "https://images.pexels.com/photos/280222/pexels-photo-280222.jpeg"
            ]
        },
        "Travel & Rentals": {
            "glance": [
                "https://images.pexels.com/photos/237272/pexels-photo-237272.jpeg",
                "https://images.pexels.com/photos/116675/pexels-photo-116675.jpeg",
                "https://images.pexels.com/photos/1051073/pexels-photo-1051073.jpeg"
            ],
            "business": [
                "https://images.pexels.com/photos/116675/pexels-photo-116675.jpeg",
                "https://images.pexels.com/photos/237272/pexels-photo-237272.jpeg",
                "https://images.pexels.com/photos/3183153/pexels-photo-3183153.jpeg",
                "https://images.pexels.com/photos/459225/pexels-photo-459225.jpeg"
            ]
        }
    }

    for sub_name, data in mapping.items():
        print(f"Refining images for: {sub_name}")
        
        # Update Glance images
        for i, img_url in enumerate(data["glance"]):
            await db["universal_content"].update_many(
                {
                    "mainPage": "Business Verticals",
                    "subSection": sub_name,
                    "category": "At a Glance",
                    "order": i
                },
                {"$set": {"image": img_url}}
            )
            
        # Update Business images
        for i, img_url in enumerate(data["business"]):
            await db["universal_content"].update_many(
                {
                    "mainPage": "Business Verticals",
                    "subSection": sub_name,
                    "category": "Our Business",
                    "order": i
                },
                {"$set": {"image": img_url}}
            )
            
    print("Database updated with unique mixed image set.")
    await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(fix_duplicate_images())
