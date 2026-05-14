import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import uuid

MONGO_URI = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"

# Business pages: subSection name (matches path_map in main.py) -> card data
BUSINESS_PAGES = {

    # ── 1. Export & Import ──────────────────────────────────────────────────────
    "Export & Import": {
        "glance": [
            {
                "title": "Global Trade Network",
                "description": "Connecting Indian businesses to 40+ countries with seamless import-export logistics.",
                "image_url": "https://images.unsplash.com/photo-1494412519320-aa613dfb7738?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Cold Chain Expertise",
                "description": "State-of-the-art cold-chain management ensuring fresh delivery of perishable commodities.",
                "image_url": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Compliance & Documentation",
                "description": "End-to-end customs clearance, licensing, and regulatory compliance support.",
                "image_url": "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&q=80&w=800"
            }
        ],
        "our_business": [
            {
                "title": "Agricultural Exports",
                "description": "Premium quality spices, grains, and fresh produce exported worldwide.",
                "image_url": "https://images.unsplash.com/photo-1464226184884-fa280b87c399?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Industrial Imports",
                "description": "Sourcing high-grade machinery, raw materials, and components for Indian industries.",
                "image_url": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "D2C Trade Solutions",
                "description": "Direct-to-consumer cross-border commerce enabling faster global reach.",
                "image_url": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Supply Chain Management",
                "description": "Integrated supply chain visibility from origin to last-mile delivery.",
                "image_url": "https://images.unsplash.com/photo-1586528116493-a029325540fa?auto=format&fit=crop&q=80&w=800"
            }
        ]
    },

    # ── 2. Green Energy & Solar Manufacturing ───────────────────────────────────
    "Green Energy & Solar Manufacturing": {
        "glance": [
            {
                "title": "Solar Manufacturing",
                "description": "High-efficiency photovoltaic panels produced at our state-of-the-art facility.",
                "image_url": "https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Renewable Energy Systems",
                "description": "Integrated solar, wind, and battery-storage solutions for homes and industries.",
                "image_url": "https://images.unsplash.com/photo-1466611653911-95281773ad90?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "ESG Commitment",
                "description": "Reducing carbon footprints with certified green energy projects across Tamil Nadu.",
                "image_url": "https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&q=80&w=800"
            }
        ],
        "our_business": [
            {
                "title": "Solar Parks",
                "description": "Utility-scale solar power plants generating clean energy for the grid.",
                "image_url": "https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Rooftop Solar",
                "description": "Affordable rooftop installations for residential and commercial buildings.",
                "image_url": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Solar Panel Manufacturing",
                "description": "In-house manufacturing of mono and poly-crystalline solar panels.",
                "image_url": "https://images.unsplash.com/photo-1611365892117-00ac5ef43c90?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Energy Storage Solutions",
                "description": "Advanced battery storage systems ensuring 24×7 renewable power supply.",
                "image_url": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&q=80&w=800"
            }
        ]
    },

    # ── 3. IT Consulting ────────────────────────────────────────────────────────
    "IT Consulting": {
        "glance": [
            {
                "title": "Digital Transformation",
                "description": "Guiding enterprises through end-to-end digital modernisation strategies.",
                "image_url": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Cybersecurity",
                "description": "Protecting business assets with advanced threat detection and compliance frameworks.",
                "image_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Cloud Strategy",
                "description": "Optimising cloud architecture for performance, cost, and scalability.",
                "image_url": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&q=80&w=800"
            }
        ],
        "our_business": [
            {
                "title": "Enterprise IT Consulting",
                "description": "Strategic advisory for ERP, CRM, and enterprise software implementations.",
                "image_url": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Cloud Migration",
                "description": "Seamless migration of workloads to AWS, Azure, and Google Cloud.",
                "image_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Software Development",
                "description": "Custom web and mobile application development tailored to business needs.",
                "image_url": "https://images.unsplash.com/photo-1504639725590-34d0984388bd?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "IT Support & Managed Services",
                "description": "24×7 NOC support, patch management, and SLA-backed IT operations.",
                "image_url": "https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?auto=format&fit=crop&q=80&w=800"
            }
        ]
    },

    # ── 4. Enterprise Data Centers & Hosting Services ───────────────────────────
    "Enterprise Data Centers & Hosting Services": {
        "glance": [
            {
                "title": "Tier-III Data Centers",
                "description": "99.982% uptime guaranteed with redundant power and cooling systems.",
                "image_url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Managed Hosting",
                "description": "Fully managed dedicated, VPS, and cloud hosting with round-the-clock monitoring.",
                "image_url": "https://images.unsplash.com/photo-1512756290469-ec264b7fbf87?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Disaster Recovery",
                "description": "Robust DR and business continuity solutions ensuring zero data loss.",
                "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=800"
            }
        ],
        "our_business": [
            {
                "title": "Colocation Services",
                "description": "Secure rack space with high-bandwidth connectivity for enterprise servers.",
                "image_url": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Dedicated Hosting",
                "description": "High-performance dedicated servers for mission-critical applications.",
                "image_url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Cloud Hosting",
                "description": "Scalable cloud infrastructure with auto-scaling and pay-as-you-go pricing.",
                "image_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "CDN & Network Solutions",
                "description": "Global content delivery network for faster website performance worldwide.",
                "image_url": "https://images.unsplash.com/photo-1484704849700-f032a568e944?auto=format&fit=crop&q=80&w=800"
            }
        ]
    },

    # ── 5. IT Training ──────────────────────────────────────────────────────────
    "IT Training": {
        "glance": [
            {
                "title": "Industry-Ready Curriculum",
                "description": "Courses co-designed with tech leaders to match real-world job requirements.",
                "image_url": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Expert Trainers",
                "description": "Learn from certified professionals with 10+ years of industry experience.",
                "image_url": "https://images.unsplash.com/photo-1524178232363-1fb2b075b655?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Placement Support",
                "description": "Dedicated placement cell with 200+ hiring partner companies.",
                "image_url": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&q=80&w=800"
            }
        ],
        "our_business": [
            {
                "title": "Full Stack Development",
                "description": "Comprehensive training in frontend, backend, and DevOps technologies.",
                "image_url": "https://images.unsplash.com/photo-1504639725590-34d0984388bd?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Data Science & AI",
                "description": "Hands-on programs in machine learning, deep learning, and data analytics.",
                "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Cloud & DevOps",
                "description": "AWS, Azure, and GCP certification training with live project exposure.",
                "image_url": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Cybersecurity",
                "description": "Ethical hacking, penetration testing, and security audit training courses.",
                "image_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=800"
            }
        ]
    },

    # ── 6. Yoga & Wellness ──────────────────────────────────────────────────────
    "Yoga & Wellness": {
        "glance": [
            {
                "title": "Holistic Wellness",
                "description": "Integrating yoga, meditation, and Ayurveda for complete mind-body harmony.",
                "image_url": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Certified Instructors",
                "description": "Learn from internationally certified yoga instructors with decades of practice.",
                "image_url": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Wellness Retreats",
                "description": "Curated retreats blending traditional practices with modern wellness science.",
                "image_url": "https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?auto=format&fit=crop&q=80&w=800"
            }
        ],
        "our_business": [
            {
                "title": "Yoga Classes",
                "description": "Daily Hatha, Vinyasa, and Power Yoga sessions for all skill levels.",
                "image_url": "https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Meditation Programs",
                "description": "Mindfulness and guided meditation programs for stress relief and clarity.",
                "image_url": "https://images.unsplash.com/photo-1593811167562-9cef47bfc4d7?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Ayurvedic Treatments",
                "description": "Traditional Ayurvedic therapies and personalised wellness consultations.",
                "image_url": "https://images.unsplash.com/photo-1515377905703-c4788e51af15?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Corporate Wellness",
                "description": "Customised workplace wellness programs to boost employee productivity.",
                "image_url": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?auto=format&fit=crop&q=80&w=800"
            }
        ]
    },

    # ── 7. Property Services ────────────────────────────────────────────────────
    "Property Services": {
        "glance": [
            {
                "title": "Premium Properties",
                "description": "Curated portfolio of residential, commercial, and industrial real estate.",
                "image_url": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Expert Advisory",
                "description": "Seasoned real estate advisors guiding you through every stage of property investment.",
                "image_url": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Legal & Documentation",
                "description": "Complete legal due diligence, title verification, and documentation support.",
                "image_url": "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&q=80&w=800"
            }
        ],
        "our_business": [
            {
                "title": "Residential Projects",
                "description": "Modern apartments and villas designed for comfortable family living.",
                "image_url": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Commercial Spaces",
                "description": "Prime office spaces and retail outlets in high-footfall business districts.",
                "image_url": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Land & Plots",
                "description": "DTCP-approved plots and agricultural land across Tamil Nadu.",
                "image_url": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Property Management",
                "description": "End-to-end property management including maintenance, leasing, and tenant care.",
                "image_url": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&q=80&w=800"
            }
        ]
    },

    # ── 8. Logistics Services ───────────────────────────────────────────────────
    "Logistics Services": {
        "glance": [
            {
                "title": "Pan-India Network",
                "description": "Freight delivery across 600+ districts with real-time tracking.",
                "image_url": "https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Fleet Management",
                "description": "GPS-enabled fleet of 200+ vehicles ensuring on-time, damage-free delivery.",
                "image_url": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Warehousing",
                "description": "Modern warehouses with inventory management systems across key hubs.",
                "image_url": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&q=80&w=800"
            }
        ],
        "our_business": [
            {
                "title": "Road Freight",
                "description": "Full truckload and less-than-truckload services for bulk cargo movement.",
                "image_url": "https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Air Cargo",
                "description": "Express air freight solutions for time-critical shipments worldwide.",
                "image_url": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Cold Chain Logistics",
                "description": "Temperature-controlled transport for pharmaceuticals and food products.",
                "image_url": "https://images.unsplash.com/photo-1586528116493-a029325540fa?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Last-Mile Delivery",
                "description": "Hyper-local delivery solutions ensuring prompt customer satisfaction.",
                "image_url": "https://images.unsplash.com/photo-1563013544-824ae1b704d3?auto=format&fit=crop&q=80&w=800"
            }
        ]
    },

    # ── 9. Plantations & Exotic Trees ───────────────────────────────────────────
    "Plantations & Exotic Trees": {
        "glance": [
            {
                "title": "Exotic Tree Varieties",
                "description": "Cultivating 50+ rare and exotic tree species including teak, sandalwood, and mahogany.",
                "image_url": "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Sustainable Forestry",
                "description": "Eco-certified plantation practices promoting biodiversity and soil health.",
                "image_url": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Investment Returns",
                "description": "Long-term plantation investments delivering steady and appreciating returns.",
                "image_url": "https://images.unsplash.com/photo-1464226184884-fa280b87c399?auto=format&fit=crop&q=80&w=800"
            }
        ],
        "our_business": [
            {
                "title": "Teak Plantations",
                "description": "High-value teak cultivation with assured buy-back programs for investors.",
                "image_url": "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Sandalwood Farming",
                "description": "Certified sandalwood groves with scientific farming and security management.",
                "image_url": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Fruit Orchards",
                "description": "Tropical fruit plantations including mango, guava, and pomegranate varieties.",
                "image_url": "https://images.unsplash.com/photo-1522184216316-3c25379f9760?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Herbal & Medicinal Plants",
                "description": "Cultivation of Ayurvedic and pharmaceutical-grade medicinal herbs.",
                "image_url": "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?auto=format&fit=crop&q=80&w=800"
            }
        ]
    },

    # ── 10. Travel & Rentals ────────────────────────────────────────────────────
    "Travel & Rentals": {
        "glance": [
            {
                "title": "Curated Travel Packages",
                "description": "Handcrafted domestic and international tour packages for every budget.",
                "image_url": "https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Premium Rentals",
                "description": "Luxury car, bike, and equipment rentals with doorstep delivery.",
                "image_url": "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "24×7 Support",
                "description": "Round-the-clock travel assistance and emergency support for all customers.",
                "image_url": "https://images.unsplash.com/photo-1516738901171-8eb4fc13bd20?auto=format&fit=crop&q=80&w=800"
            }
        ],
        "our_business": [
            {
                "title": "Domestic Tour Packages",
                "description": "Affordable all-inclusive packages covering heritage, hill stations, and beaches.",
                "image_url": "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "International Tours",
                "description": "Visa-assisted international holiday packages to 30+ countries.",
                "image_url": "https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "Car Rentals",
                "description": "Self-drive and chauffeur-driven car rentals from economy to luxury segment.",
                "image_url": "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?auto=format&fit=crop&q=80&w=800"
            },
            {
                "title": "MICE & Corporate Travel",
                "description": "End-to-end event, conference, and corporate travel management services.",
                "image_url": "https://images.unsplash.com/photo-1540575467063-178a50c2df87?auto=format&fit=crop&q=80&w=800"
            }
        ]
    }
}


async def seed_business_cards():
    print("Connecting to MongoDB...")
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["vjs_cms"]
    col = db["universal_content"]

    for sub_section, data in BUSINESS_PAGES.items():
        print(f"\n>> Seeding: {sub_section}")

        # ── At a Glance (3 cards) ───────────────────────────────────────────────
        glance_cards = []
        for card in data["glance"]:
            glance_cards.append({
                "_card_id": str(uuid.uuid4()),
                "title": card["title"],
                "description": card["description"],
                "image": card["image_url"]
            })

        glance_doc = {
            "mainPage": "Business Verticals",
            "subSection": sub_section,
            "category": "At a Glance",
            "type": "cards",
            "content": glance_cards,
            "order": 1,
            "isActive": True,
            "updatedAt": datetime.utcnow()
        }
        result = await col.update_one(
            {"mainPage": "Business Verticals", "subSection": sub_section, "category": "At a Glance"},
            {"$set": glance_doc},
            upsert=True
        )
        print(f"   At a Glance: {'inserted' if result.upserted_id else 'updated'} ({len(glance_cards)} cards)")

        # ── Our Business (4 cards) ──────────────────────────────────────────────
        biz_cards = []
        for card in data["our_business"]:
            biz_cards.append({
                "_card_id": str(uuid.uuid4()),
                "title": card["title"],
                "description": card["description"],
                "image": card["image_url"]
            })

        biz_doc = {
            "mainPage": "Business Verticals",
            "subSection": sub_section,
            "category": "Our Business",
            "type": "cards",
            "content": biz_cards,
            "order": 2,
            "isActive": True,
            "updatedAt": datetime.utcnow()
        }
        result = await col.update_one(
            {"mainPage": "Business Verticals", "subSection": sub_section, "category": "Our Business"},
            {"$set": biz_doc},
            upsert=True
        )
        print(f"   Our Business: {'inserted' if result.upserted_id else 'updated'} ({len(biz_cards)} cards)")

    print("\nDONE: All business page cards seeded successfully!")
    client.close()


if __name__ == "__main__":
    asyncio.run(seed_business_cards())
