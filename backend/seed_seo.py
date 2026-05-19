import sys
from pathlib import Path
from pymongo import MongoClient
from datetime import datetime

# Setup Paths
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "backend"))

# MongoDB Connection
MONGO_URI = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["vjs_cms"]
col = db["seo_metadata"]

# Clear existing metadata if any
col.delete_many({})

NOW = datetime.utcnow()

SEO_DATA = [
    {
        "page_path": "",
        "title": "Vijayalakshmi Group | Leading Sustainable Conglomerate",
        "description": "Vijayalakshmi Group of Companies is a premier global conglomerate specializing in Enterprise Data Centers, Green Energy, Logistics, IT Consulting, and Tree Plantations.",
        "keywords": "Green Energy, Data Centers, Logistics, VJS Group, IT Consulting, Tree Plantations, Vijayalakshmi Group",
        "og_title": "Vijayalakshmi Group of Companies | Sustainable Enterprise",
        "og_description": "Empowering sustainable growth across diverse business verticals globally.",
        "og_url": "https://vijayalakshmigroup.com/",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "index-2",
        "title": "Vijayalakshmi Group | Leading Sustainable Conglomerate",
        "description": "Vijayalakshmi Group of Companies is a premier global conglomerate specializing in Enterprise Data Centers, Green Energy, Logistics, IT Consulting, and Tree Plantations.",
        "keywords": "Green Energy, Data Centers, Logistics, VJS Group, IT Consulting, Tree Plantations, Vijayalakshmi Group",
        "og_title": "Vijayalakshmi Group of Companies | Sustainable Enterprise",
        "og_description": "Empowering sustainable growth across diverse business verticals globally.",
        "og_url": "https://vijayalakshmigroup.com/",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "about-us-v1",
        "title": "Our Journey | About Vijayalakshmi Group",
        "description": "Learn about the heritage, journey, and milestones of the Vijayalakshmi Group of Companies.",
        "keywords": "Our Journey, VJS Group History, Milestone, About Vijayalakshmi Group",
        "og_title": "Our Journey | Vijayalakshmi Group",
        "og_description": "Learn about the heritage, journey, and milestones of the Vijayalakshmi Group of Companies.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "about-us-v2",
        "title": "About Group | Vijayalakshmi Group",
        "description": "Discover Vijayalakshmi Group of Companies' corporate history, core values, and vision.",
        "keywords": "About Group, Corporate Values, VJS Vision, Vijayalakshmi Group",
        "og_title": "About Group | Vijayalakshmi Group",
        "og_description": "Discover Vijayalakshmi Group of Companies' corporate history, core values, and vision.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "service-v1",
        "title": "Leadership & Awards | Vijayalakshmi Group",
        "description": "Meet our leadership team and explore the prestigious awards and recognition received by the Vijayalakshmi Group of Companies.",
        "keywords": "VJS Leadership, Group Awards, Corporate Recognition, Vijayalakshmi Group",
        "og_title": "Leadership & Awards | Vijayalakshmi Group",
        "og_description": "Meet our leadership team and explore the prestigious awards and recognition received by the Vijayalakshmi Group of Companies.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "service-v2",
        "title": "Our Businesses & Services | Vijayalakshmi Group",
        "description": "Explore the diverse portfolio of businesses under the Vijayalakshmi Group, including IT, energy, logistics, and sustainability.",
        "keywords": "VJS Services, Business Verticals, Corporate Services, Vijayalakshmi Group",
        "og_title": "Our Businesses & Services | Vijayalakshmi Group",
        "og_description": "Explore the diverse portfolio of businesses under the Vijayalakshmi Group, including IT, energy, logistics, and sustainability.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "green-energy",
        "title": "Green Energy & Solar Manufacturing | Vijayalakshmi Group",
        "description": "Explore eco-friendly energy solutions and advanced solar manufacturing services by Vijayalakshmi Group of Companies.",
        "keywords": "Solar Manufacturing, Green Energy, Renewable Energy, Eco Friendly, Vijayalakshmi Group",
        "og_title": "Green Energy & Solar Manufacturing | Vijayalakshmi Group",
        "og_description": "Explore eco-friendly energy solutions and advanced solar manufacturing services by Vijayalakshmi Group of Companies.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "data-centers-hosting",
        "title": "Enterprise Data Centers & Hosting | Vijayalakshmi Group",
        "description": "Secure, scalable, and sustainable enterprise data center hosting and cloud infrastructure solutions by Vijayalakshmi Group.",
        "keywords": "Data Centers, Hosting Services, Cloud Infrastructure, Sustainable Hosting, Vijayalakshmi Group",
        "og_title": "Enterprise Data Centers & Hosting | Vijayalakshmi Group",
        "og_description": "Secure, scalable, and sustainable enterprise data center hosting and cloud infrastructure solutions by Vijayalakshmi Group.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "it-consulting",
        "title": "IT Consulting & Digital Transformation | Vijayalakshmi Group",
        "description": "Drive innovation and business optimization with elite IT consulting and enterprise systems design by Vijayalakshmi Group.",
        "keywords": "IT Consulting, Digital Transformation, Business Optimization, Software Services",
        "og_title": "IT Consulting & Digital Transformation | Vijayalakshmi Group",
        "og_description": "Drive innovation and business optimization with elite IT consulting and enterprise systems design by Vijayalakshmi Group.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "logistics-services",
        "title": "Logistics Services & Global Supply Chain | Vijayalakshmi Group",
        "description": "Safe, reliable, and integrated global supply chain and logistics services by Vijayalakshmi Group of Companies.",
        "keywords": "Logistics Services, Supply Chain, Cargo, Warehousing, Global Logistics",
        "og_title": "Logistics Services & Global Supply Chain | Vijayalakshmi Group",
        "og_description": "Safe, reliable, and integrated global supply chain and logistics services by Vijayalakshmi Group of Companies.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "export-import",
        "title": "Export & Import Global Trade | Vijayalakshmi Group",
        "description": "Facilitating seamless international trade and commodity export-import solutions across multiple sectors.",
        "keywords": "Export Import, Global Trade, Commodities, VJS Import Export",
        "og_title": "Export & Import Global Trade | Vijayalakshmi Group",
        "og_description": "Facilitating seamless international trade and commodity export-import solutions across multiple sectors.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "property-services",
        "title": "Property Services & Asset Management | Vijayalakshmi Group",
        "description": "Premium real estate solutions, property development, and corporate asset management by Vijayalakshmi Group.",
        "keywords": "Property Services, Asset Management, Corporate Real Estate, Property Development",
        "og_title": "Property Services & Asset Management | Vijayalakshmi Group",
        "og_description": "Premium real estate solutions, property development, and corporate asset management by Vijayalakshmi Group.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "it-training",
        "title": "IT Training & Professional Development | Vijayalakshmi Group",
        "description": "Empowering students and professionals with top-tier technology courses, certifications, and hands-on skill development.",
        "keywords": "IT Training, Professional Education, Skill Building, Tech Certification",
        "og_title": "IT Training & Professional Development | Vijayalakshmi Group",
        "og_description": "Empowering students and professionals with top-tier technology courses, certifications, and hands-on skill development.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "yoga-wellness",
        "title": "Yoga & Wellness Center | Vijayalakshmi Group",
        "description": "Promoting holistic health, mental clarity, and spiritual well-being through advanced yoga and wellness programs.",
        "keywords": "Yoga and Wellness, Holistic Health, VJS Yoga Center, Mindfulness",
        "og_title": "Yoga & Wellness Center | Vijayalakshmi Group",
        "og_description": "Promoting holistic health, mental clarity, and spiritual well-being through advanced yoga and wellness programs.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "travel-rentals",
        "title": "Travel & Premium Rentals | Vijayalakshmi Group",
        "description": "Hassle-free corporate car rentals, holiday planning, and premium tour operations by Vijayalakshmi Group.",
        "keywords": "Travel Rentals, Premium Tour, Car Rental, Corporate Travel, Holiday Planner",
        "og_title": "Travel & Premium Rentals | Vijayalakshmi Group",
        "og_description": "Hassle-free corporate car rentals, holiday planning, and premium tour operations by Vijayalakshmi Group.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "plantations",
        "title": "Plantations & Exotic Trees | Vijayalakshmi Group",
        "description": "Pioneering commercial plantations, sustainability conservation projects, and timber/horticultural cultivation.",
        "keywords": "Tree Plantation, Exotic Trees, Conservation, Green Cover, VJS Plantations",
        "og_title": "Plantations & Exotic Trees | Vijayalakshmi Group",
        "og_description": "Pioneering commercial plantations, sustainability conservation projects, and timber/horticultural cultivation.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "plantations-exotic-trees",
        "title": "Plantations & Exotic Trees | Vijayalakshmi Group",
        "description": "Pioneering commercial plantations, sustainability conservation projects, and timber/horticultural cultivation.",
        "keywords": "Tree Plantation, Exotic Trees, Conservation, Green Cover, VJS Plantations",
        "og_title": "Plantations & Exotic Trees | Vijayalakshmi Group",
        "og_description": "Pioneering commercial plantations, sustainability conservation projects, and timber/horticultural cultivation.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "media-release",
        "title": "Newsroom & Media Release | Vijayalakshmi Group",
        "description": "Stay updated with the latest press releases, corporate announcements, and insights from Vijayalakshmi Group of Companies.",
        "keywords": "Media Release, Press Release, VJS Newsroom, Corporate Insights",
        "og_title": "Newsroom & Media Release | Vijayalakshmi Group",
        "og_description": "Stay updated with the latest press releases, corporate announcements, and insights from Vijayalakshmi Group of Companies.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "media-kit",
        "title": "Media Kit | Vijayalakshmi Group",
        "description": "Access official media resources, press kits, brand guidelines, and high-resolution assets of the Vijayalakshmi Group of Companies.",
        "keywords": "VJS Media Kit, Corporate Press Assets, Brand Assets, Vijayalakshmi Group",
        "og_title": "Media Kit | Vijayalakshmi Group",
        "og_description": "Access official media resources, press kits, brand guidelines, and high-resolution assets of the Vijayalakshmi Group of Companies.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "blog-v1",
        "title": "Vijayalakshmi Foundation | Corporate Social Responsibility",
        "description": "Explore the community support, education, healthcare, and environmental conservation initiatives of the Vijayalakshmi Foundation.",
        "keywords": "Vijayalakshmi Foundation, VJS CSR, Community Development, Social Responsibility",
        "og_title": "Vijayalakshmi Foundation | Corporate Social Responsibility",
        "og_description": "Explore the community support, education, healthcare, and environmental conservation initiatives of the Vijayalakshmi Foundation.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "sustainability",
        "title": "Sustainability & Corporate Social Responsibility | Vijayalakshmi Group",
        "description": "Discover the sustainability vision, environmental milestones, and community CSR initiatives of the Vijayalakshmi Group of Companies.",
        "keywords": "Sustainability VJS, CSR Initiatives, Green Business, Community Care",
        "og_title": "Sustainability & Corporate Social Responsibility | Vijayalakshmi Group",
        "og_description": "Discover the sustainability vision, environmental milestones, and community CSR initiatives of the Vijayalakshmi Group of Companies.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "digital-transformation-sustainability",
        "title": "Digital Transformation & IT Consulting Sustainability | Vijayalakshmi Group",
        "description": "How Vijayalakshmi Group integrates digital transformation and IT consulting with sustainability goals like paperless workflows.",
        "keywords": "Digital Transformation, IT Consulting, Sustainability, VJS Group, Paperless Workflow",
        "og_title": "Digital Transformation & IT Consulting Sustainability | Vijayalakshmi Group",
        "og_description": "How Vijayalakshmi Group integrates digital transformation and IT consulting with sustainability goals like paperless workflows.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "cloud-infrastructure-sustainability",
        "title": "Cloud, Hosting & Infrastructure Sustainability | Vijayalakshmi Group",
        "description": "Discover how scalable cloud hosting and optimized servers contribute to a reduced corporate carbon footprint.",
        "keywords": "Cloud Sustainability, Green Hosting, Server Optimization, Carbon Footprint",
        "og_title": "Cloud, Hosting & Infrastructure Sustainability | Vijayalakshmi Group",
        "og_description": "Discover how scalable cloud hosting and optimized servers contribute to a reduced corporate carbon footprint.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "renewable-energy-solutions",
        "title": "Renewable Energy Solutions | Vijayalakshmi Group",
        "description": "Pioneering clean, decentralized renewable energy and solar power adoption across corporate and rural areas.",
        "keywords": "Renewable Energy, Solar Power, Clean Energy, Sustainable Electricity",
        "og_title": "Renewable Energy Solutions | Vijayalakshmi Group",
        "og_description": "Pioneering clean, decentralized renewable energy and solar power adoption across corporate and rural areas.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "logistics-trade-sustainability",
        "title": "Logistics & Trade Sustainability | Vijayalakshmi Group",
        "description": "Sustainable supply chain management, route optimization, and carbon footprint reduction in global trade.",
        "keywords": "Sustainable Logistics, Supply Chain Optimization, Green Trade, Fuel Efficiency",
        "og_title": "Logistics & Trade Sustainability | Vijayalakshmi Group",
        "og_description": "Sustainable supply chain management, route optimization, and carbon footprint reduction in global trade.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "education-skill-sustainability",
        "title": "Education & Skill Development Sustainability | Vijayalakshmi Group",
        "description": "Empowering future-ready workforces through tech training, digital literacy, and professional certifications.",
        "keywords": "Education Sustainability, IT Training, Skill Development, Aditya Institute",
        "og_title": "Education & Skill Development Sustainability | Vijayalakshmi Group",
        "og_description": "Empowering future-ready workforces through tech training, digital literacy, and professional certifications.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "tree-plantation-sustainability",
        "title": "Tree Plantation & Green Cover Initiatives | Vijayalakshmi Group",
        "description": "Lakshmi Gardens is dedicated to environmental conservation, commercial plantations, and increasing community green cover.",
        "keywords": "Tree Plantation, Green Cover, Lakshmi Gardens, Environmental Conservation",
        "og_title": "Tree Plantation & Green Cover Initiatives | Vijayalakshmi Group",
        "og_description": "Lakshmi Gardens is dedicated to environmental conservation, commercial plantations, and increasing community green cover.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "eco-tech-solutions",
        "title": "Eco-Conscious Technology Solutions | Vijayalakshmi Group",
        "description": "Fostering the creation and adoption of technology solutions designed to minimize environmental impact.",
        "keywords": "Eco-Conscious Technology, Green IT, Clean Software, Resource Conservation",
        "og_title": "Eco-Conscious Technology Solutions | Vijayalakshmi Group",
        "og_description": "Fostering the creation and adoption of technology solutions designed to minimize environmental impact.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "renewable-energy-adoption",
        "title": "Renewable Energy Adoption & Clean Power | Vijayalakshmi Group",
        "description": "Transitioning operations to 100% renewable power sources to secure local ecological sustainability.",
        "keywords": "Renewable Power Adoption, Sustainable Energy Transition, Clean Electricity",
        "og_title": "Renewable Energy Adoption & Clean Power | Vijayalakshmi Group",
        "og_description": "Transitioning operations to 100% renewable power sources to secure local ecological sustainability.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "sustainable-business-practices",
        "title": "Sustainable Business Practices & ESG | Vijayalakshmi Group",
        "description": "Ensuring corporate activities adhere to rigorous ethical, environmental, and social governance standards.",
        "keywords": "ESG Business Practices, Corporate Ethics, Green Governance, VJS ESG",
        "og_title": "Sustainable Business Practices & ESG | Vijayalakshmi Group",
        "og_description": "Ensuring corporate activities adhere to rigorous ethical, environmental, and social governance standards.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "educational-support-csr",
        "title": "Educational Support & Grassroots Programs | Vijayalakshmi Group",
        "description": "The Vijayalakshmi Foundation provides scholarships, learning aids, and school resources to disadvantaged students.",
        "keywords": "Educational CSR, Student Aid, School Support, VJS Foundation",
        "og_title": "Educational Support & Grassroots Programs | Vijayalakshmi Group",
        "og_description": "The Vijayalakshmi Foundation provides scholarships, learning aids, and school resources to disadvantaged students.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "financial-material-aid",
        "title": "Financial & Material Aid Programs | Vijayalakshmi Group",
        "description": "Offering direct financial assistance and material relief during ecological crises or community emergency periods.",
        "keywords": "CSR Financial Aid, Material Relief, Community Support, Emergency Relief",
        "og_title": "Financial & Material Aid Programs | Vijayalakshmi Group",
        "og_description": "Offering direct financial assistance and material relief during ecological crises or community emergency periods.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "skill-building-youth",
        "title": "Youth Skill-Building & Employability | Vijayalakshmi Group",
        "description": "Free vocational training, career consulting, and job placement assistance powered by the Vijayalakshmi Foundation.",
        "keywords": "Youth Skilling, Vocational Education, Job Training, Employability CSR",
        "og_title": "Youth Skill-Building & Employability | Vijayalakshmi Group",
        "og_description": "Free vocational training, career consulting, and job placement assistance powered by the Vijayalakshmi Foundation.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "rural-semi-urban-engagement",
        "title": "Rural & Semi-Urban Engagement | Vijayalakshmi Group",
        "description": "Connecting with communities in non-urban districts to build localized livelihood opportunities and social upliftment.",
        "keywords": "Rural Engagement CSR, Community Upliftment, Local Livelihoods",
        "og_title": "Rural & Semi-Urban Engagement | Vijayalakshmi Group",
        "og_description": "Connecting with communities in non-urban districts to build localized livelihood opportunities and social upliftment.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "awareness-programs-community",
        "title": "Community Awareness & Health Programs | Vijayalakshmi Group",
        "description": "Organizing wellness camps, educational seminars, and awareness rallies to improve societal health.",
        "keywords": "Community Awareness, Wellness Camps, Social Awareness CSR",
        "og_title": "Community Awareness & Health Programs | Vijayalakshmi Group",
        "og_description": "Organizing wellness camps, educational seminars, and awareness rallies to improve societal health.",
        "robots": "index, follow",
        "updatedAt": NOW
    },
    {
        "page_path": "local-infrastructure-support",
        "title": "Local Infrastructure Support & Development | Vijayalakshmi Group",
        "description": "Empowering region development by upgrading schools, water facilities, and building public community assets.",
        "keywords": "Infrastructure CSR, School Renovation, Community Development VJS",
        "og_title": "Local Infrastructure Support & Development | Vijayalakshmi Group",
        "og_description": "Empowering region development by upgrading schools, water facilities, and building public community assets.",
        "robots": "index, follow",
        "updatedAt": NOW
    }
]

print("Seeding SEO metadata records...")
for doc in SEO_DATA:
    col.insert_one(doc)
    print(f"Inserted path: {doc['page_path']}")

print("SEO Seeding completed successfully!")
client.close()
