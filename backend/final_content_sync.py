import asyncio
import os
import sys
sys.path.append(os.getcwd())
from app.db.mongodb import connect_to_mongo, get_database, close_mongo_connection

async def final_content_sync():
    await connect_to_mongo()
    db = get_database()
    
    local_base = "/static/images/vjs_business/"
    
    # Final Content & Image Synchronization
    # Ensuring 100% suitability between Title, Description, and Image.
    config = {
        "IT Consulting": {
            "services": [
                {
                    "title": "Digital Transformation",
                    "desc": "End-to-end web, mobile, and enterprise application development using modern technology stacks.",
                    "img": local_base + "project-flowchart-on-laptop-for-business-concepts-2026-01-06-10-01-03-utc.jpg"
                },
                {
                    "title": "AI & Automation",
                    "desc": "Implementing intelligent automation, predictive models, and natural language processing systems.",
                    "img": local_base + "woman-presenting-artificial-intelligence-technolog-2026-01-09-13-01-03-utc.jpg"
                },
                {
                    "title": "Enterprise Solutions",
                    "desc": "Custom CRM, ERP, and RPA deployments to streamline complex and large-scale business workflows.",
                    "img": "https://images.pexels.com/photos/3182812/pexels-photo-3182812.jpeg"
                },
                {
                    "title": "Data Analytics",
                    "desc": "Building powerful data visualization and business intelligence platforms for data-driven growth.",
                    "img": local_base + "cloud-computing-security-and-data-flow-concepts-2026-01-06-09-27-15-utc.jpg"
                }
            ]
        },
        "Enterprise Data Centers & Hosting Services": {
            "services": [
                {
                    "title": "Managed Hosting",
                    "desc": "High-performance dedicated server management with 24/7 proactive monitoring in Tier III facilities.",
                    "img": local_base + "worker-stands-among-servers-in-a-data-center-2026-01-09-11-11-16-utc.jpg"
                },
                {
                    "title": "Domain Services",
                    "desc": "Reliable registration, white-label reselling, and DNS management for global brand identity.",
                    "img": local_base + "wooden-man-holding-a-domain-name-block-2026-03-16-02-11-23-utc.jpg"
                },
                {
                    "title": "Cloud Deployments",
                    "desc": "Scalable public, private, and hybrid cloud solutions tailored to enterprise-grade requirements.",
                    "img": local_base + "business-professional-using-cloud-computing-techno-2026-01-11-08-44-25-utc.jpg"
                },
                {
                    "title": "Infra Optimization",
                    "desc": "Maximizing resource efficiency and system performance through advanced infrastructure audits.",
                    "img": local_base + "data-center-coworkers-doing-brainstorming-monitor-2026-01-11-10-54-31-utc.jpg"
                }
            ]
        },
        "Green Energy & Solar Manufacturing": {
            "services": [
                {
                    "title": "Solar PV Installation",
                    "desc": "Full-scale design and installation of high-efficiency photovoltaic systems for all sectors.",
                    "img": "https://images.pexels.com/photos/2800832/pexels-photo-2800832.jpeg"
                },
                {
                    "title": "Rural Electrification",
                    "desc": "Deploying decentralized micro-grids to bring clean energy to remote and off-grid communities.",
                    "img": local_base + "back-of-professional-engineer-worker-or-technicia-2026-03-23-23-01-20-utc.jpg"
                },
                {
                    "title": "Sustainability Audit",
                    "desc": "Professional energy audits and roadmaps to maximize carbon reduction and ESG alignment.",
                    "img": local_base + "green-solar-cell-house-and-leaf-on-coin-stack-sus-2026-03-25-09-49-28-utc.jpg"
                },
                {
                    "title": "Wind Energy Projects",
                    "desc": "Large-scale wind generator projects and high-voltage line management for utility-scale power.",
                    "img": local_base + "wind-generator-and-high-voltage-lines-in-a-field-2026-03-19-09-34-54-utc.jpg"
                }
            ]
        },
        "Logistics Services": {
            "services": [
                {
                    "title": "Global Freight",
                    "desc": "Integrated sea, air, and land freight forwarding services with real-time global tracking.",
                    "img": local_base + "shipping-containers-at-port-at-sunset-2026-03-24-11-22-01-utc.jpg"
                },
                {
                    "title": "Supply Chain Management",
                    "desc": "Strategic end-to-end logistics planning to reduce lead times and optimize operational costs.",
                    "img": local_base + "truck-inspector-with-clipboard-in-a-fleet-setting-2026-03-26-06-04-42-utc.jpg"
                },
                {
                    "title": "Cargo Inspection",
                    "desc": "Rigorous monitoring and inspection of containers in shipping yards to ensure zero-damage.",
                    "img": local_base + "worker-inspecting-cargo-containers-in-a-shipping-y-2026-04-16-19-03-40-utc.jpg"
                },
                {
                    "title": "Retail Distribution",
                    "desc": "Efficient direct-to-consumer distribution networks for e-commerce and retail sectors.",
                    "img": local_base + "delivery-person-handing-box-to-customer-outside-2026-03-25-02-18-23-utc.jpg"
                }
            ]
        },
        "Export & Import": {
            "services": [
                {
                    "title": "Agri-Export",
                    "desc": "Sourcing and shipping premium exotic fruits and fresh vegetables to various global markets.",
                    "img": local_base + "fresh-fruits-and-vegetables-in-a-basket-2026-01-09-15-04-22-utc.jpg"
                },
                {
                    "title": "Market Trade",
                    "desc": "B2B and D2C trade of fresh agricultural produce with verified sourcing and fair trade.",
                    "img": local_base + "successful-farmer-handshake-at-market-with-fresh-v-2026-01-09-08-34-52-utc.jpg"
                },
                {
                    "title": "Quality Lab Testing",
                    "desc": "Scientific quality examination of organic produce to ensure international safety standards.",
                    "img": local_base + "scientists-examined-the-quality-of-vegetable-organ-2026-03-20-05-45-32-utc.jpg"
                },
                {
                    "title": "Exotic Produce",
                    "desc": "Sourcing rare and exotic global produce for premium distribution and retail networks.",
                    "img": "https://images.pexels.com/photos/1435735/pexels-photo-1435735.jpeg"
                }
            ]
        }
    }

    for sub_name, data in config.items():
        print(f"Finalizing synchronization for: {sub_name}")
        
        for i, service in enumerate(data["services"]):
            await db["universal_content"].update_many(
                {
                    "mainPage": "Business Verticals",
                    "subSection": sub_name,
                    "category": "Our Business",
                    "order": i
                },
                {
                    "$set": {
                        "title": service["title"],
                        "description": service["desc"],
                        "image": service["img"]
                    }
                }
            )
            
    print("Final content-image synchronization complete.")
    await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(final_content_sync())
