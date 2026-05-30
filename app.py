# import streamlit as st
# from agent.travel_agent import agent
# import streamlit.components.v1 as components
# import time

# # ---------------------------------------------------
# # PAGE CONFIG
# # ---------------------------------------------------

# st.set_page_config(
#     page_title="AI Travel Planner",
#     page_icon="✈",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ---------------------------------------------------
# # GLOBAL STYLING
# # ---------------------------------------------------

# st.markdown("""
# <style>

# /* Hide Streamlit Branding */

# #MainMenu {visibility:hidden;}
# footer {visibility:hidden;}
# header {visibility:hidden;}

# /* Main App */

# .stApp{
#     background:
#     linear-gradient(
#         135deg,
#         #0f172a 0%,
#         #1e293b 35%,
#         #312e81 70%,
#         #581c87 100%
#     );

#     color:white;
# }

# /* Smooth Animations */

# html{
#     scroll-behavior:smooth;
# }

# /* Sidebar */

# [data-testid="stSidebar"]{
#     background:rgba(15,23,42,0.95);
#     backdrop-filter:blur(20px);
#     border-right:1px solid rgba(255,255,255,0.08);
# }

# [data-testid="stSidebar"] *{
#     color:white;
# }

# /* Titles */

# .hero-title{
#     text-align:center;
#     font-size:72px;
#     font-weight:800;
#     color:white;
#     margin-bottom:0px;
# }

# .hero-subtitle{
#     text-align:center;
#     font-size:22px;
#     color:#cbd5e1;
#     margin-bottom:30px;
# }

# /* Inputs */

# .stTextInput input,
# .stNumberInput input{

#     background:rgba(255,255,255,0.08) !important;

#     border:1px solid rgba(255,255,255,0.12) !important;

#     border-radius:15px !important;

#     color:white !important;
# }

# /* Select Boxes */

# .stSelectbox div[data-baseweb="select"]{
#     background:rgba(255,255,255,0.08);
#     border-radius:15px;
# }

# /* Metrics */

# [data-testid="metric-container"]{
#     background:rgba(255,255,255,0.08);
#     backdrop-filter:blur(12px);

#     border-radius:20px;

#     padding:20px;

#     border:1px solid rgba(255,255,255,0.08);
# }

# /* Cards */

# .glass-card{
#     background:rgba(255,255,255,0.08);

#     backdrop-filter:blur(18px);

#     border-radius:24px;

#     padding:25px;

#     border:1px solid rgba(255,255,255,0.1);
# }

# /* Button */

# .stButton>button{

#     width:100%;

#     height:60px;

#     border:none;

#     border-radius:18px;

#     font-size:20px;

#     font-weight:700;

#     color:white;

#     background:
#     linear-gradient(
#         90deg,
#         #ec4899,
#         #8b5cf6
#     );

#     transition:0.3s;
# }

# .stButton>button:hover{

#     transform:translateY(-2px);

#     box-shadow:
#     0 0 30px rgba(236,72,153,.4);
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------------------------------------------
# # SIDEBAR
# # ---------------------------------------------------

# with st.sidebar:

#     st.markdown("## 🌍 AI Travel Planner")

#     st.markdown("---")

#     st.markdown("""
# ### Features

# ✈ Flight Search

# 🏨 Hotel Recommendations

# 🌴 Tourist Attractions

# 🌦 Live Weather

# 💰 Budget Estimation

# 🧠 AI Generated Itinerary
# """)

#     st.markdown("---")

#     st.success("✨ Powered by Agentic AI")

#     st.markdown("---")

#     st.caption("Made with ❤️ by Prerna Gupta")
# # ---------------------------------------------------
# # HERO TITLE
# # ---------------------------------------------------

# components.html("""
# <h1 id="typewriter"></h1>

# <script>
# const text = "✈ AI Travel Planner";
# let i = 0;

# function typing() {
#     if (i < text.length) {
#         document.getElementById("typewriter").innerHTML += text.charAt(i);
#         i++;
#         setTimeout(typing, 100);
#     }
# }

# typing();
# </script>

# <style>
# #typewriter{
#     color:white;
#     text-align:center;
#     font-size:65px;
#     font-weight:800;
# }
# </style>
# """, height=120)

# st.markdown(
#     '<div class="subtitle">Plan dreamy trips with AI ✨🌍</div>',
#     unsafe_allow_html=True
# )

# # ---------------------------------------------------
# # HERO IMAGES
# # ---------------------------------------------------

# images = [
#     "https://i.pinimg.com/1200x/f1/c4/6a/f1c46a9783ff0aa8b16e4cd8a0b1bd35.jpg",
#     "https://i.pinimg.com/1200x/12/b5/d4/12b5d47420d50b71b18b57e303377cf9.jpg",
#     "https://i.pinimg.com/1200x/e2/5d/d1/e25dd1c74a89de97b4b633d763b11444.jpg",
#     "https://i.pinimg.com/1200x/90/ff/b9/90ffb9b1b163b494575538e05a209f21.jpg",
#     "https://i.pinimg.com/1200x/da/84/85/da84855fdba2c2f2d45ecc7f91350649.jpg",
#     "https://i.pinimg.com/1200x/96/3c/fb/963cfbbb23589cdafb5e1dae455b2809.jpg",
#     "https://i.pinimg.com/1200x/15/42/fa/1542faf121dde687021f3758064ec44b.jpg",
#     "https://i.pinimg.com/1200x/90/41/b2/9041b264186c7c8fa466a91069448b83.jpg",
#     "https://i.pinimg.com/1200x/87/d9/11/87d911a930da2f23d3fa8cb7aff7d4d2.jpg",
#     "https://i.pinimg.com/1200x/0a/a2/ad/0aa2addddd9d82e1563e9e141d86bc7d.jpg"
# ]

# html_code = f"""
# <div class="hero-container">
#     <img id="hero-image" src="{images[0]}">
# </div>

# <style>

# .hero-container {{
#     width: 100%;
#     height: 550px;
#     overflow: hidden;
#     border-radius: 30px;
#     margin-bottom: 30px;
# }}

# .hero-container img {{
#     width: 100%;
#     height: 100%;
#     object-fit: cover;
#     transition: opacity 1s ease-in-out;
#     animation: floatImage 6s ease-in-out infinite;
# }}

# @keyframes floatImage {{
#     0% {{
#         transform: scale(1) translateY(0px);
#     }}

#     50% {{
#         transform: scale(1.03) translateY(-5px);
#     }}

#     100% {{
#         transform: scale(1) translateY(0px);
#     }}
# }}

# </style>

# <script>

# const images = {images};

# let index = 0;

# const heroImage = document.getElementById("hero-image");

# setInterval(() => {{

#     heroImage.style.opacity = 0;

#     setTimeout(() => {{

#         index = (index + 1) % images.length;

#         heroImage.src = images[index];

#         heroImage.style.opacity = 1;

#     }}, 1000);

# }}, 5000);

# </script>
# """

# components.html(html_code, height=580)

# # ---------------------------------------------------
# # STATS
# # ---------------------------------------------------

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric("🌍 Destinations", "150+")

# with col2:
#     st.metric("✈ Trips Planned", "5K+")

# with col3:
#     st.metric("⭐ User Rating", "4.9")

# st.write("")

# # ---------------------------------------------------
# # INPUT SECTION
# # ---------------------------------------------------

# st.markdown(
#     '<div class="section-title">🧳 Plan Your Dream Trip</div>',
#     unsafe_allow_html=True
# )

# col1, col2 = st.columns(2)

# with col1:
#     source = st.text_input("✈ From City")

# with col2:
#     destination = st.text_input("🌴 To City")

# days = st.number_input(
#     "📅 Number of Days",
#     min_value=1,
#     max_value=30,
#     value=3
# )

# budget = st.selectbox(
#     "💰 Budget Type",
#     ["Budget", "Mid-Range", "Luxury"]
# )

# travel_style = st.selectbox(
#     "🌍 Travel Style",
#     ["Adventure", "Relaxation", "Nature", "Cultural", "Romantic"]
# )

# # ---------------------------------------------------
# # BUTTON
# # ---------------------------------------------------

# if st.button("✨ Generate AI Travel Plan"):

#     if source and destination:

#         query = f"""
# Plan a detailed {days}-day {budget} trip from {source} to {destination}.

# Travel Style: {travel_style}

# Use ALL available tools.

# Your final answer MUST contain:

# ✈ FLIGHT DETAILS
# - Airline
# - Price
# - Departure
# - Arrival

# 🏨 HOTEL DETAILS
# - Hotel Name
# - Stars
# - Price
# - Amenities

# 🌴 TOURIST ATTRACTIONS
# - Top places to visit

# 🌦 WEATHER
# - Current weather

# 💰 BUDGET BREAKDOWN
# - Flight Cost
# - Hotel Cost
# - Food Cost
# - Transport Cost
# - Total Cost

# Provide a detailed itinerary.
# Do NOT provide only a summary.
# """

#         with st.spinner("✨ Planning your magical trip..."):

#             progress = st.progress(0)

#             for i in range(100):
#                 time.sleep(0.01)
#                 progress.progress(i + 1)

#             response = agent.invoke(
#                 {
#                     "input": query
#                 }
#             )

#             progress.empty()

#         st.success("🎉 Your Dream Trip Is Ready!")

#         st.markdown(
#             '<div class="section-title">📌 AI Travel Plan</div>',
#             unsafe_allow_html=True
#         )

#         tab1, tab2 = st.tabs([
#             "🌍 Final Plan",
#             "🧠 AI Reasoning"
#         ])

#         with tab1:

#             st.markdown(f"""
#             <div class="card">
#             {response["output"]}
#             </div>
#             """, unsafe_allow_html=True)

#         with tab2:

#             for step in response["intermediate_steps"]:

#                 action = step[0]
#                 observation = step[1]

#                 st.markdown(f"""
#                 <div class="card">
#                 <h4>🔹 Tool Used: {action.tool}</h4>
#                 </div>
#                 """, unsafe_allow_html=True)

#                 st.code(str(action.tool_input))

#                 st.markdown("#### Observation")

#                 st.text(str(observation))

#     else:

#         st.warning("⚠ Please enter both source and destination cities.")

# # ---------------------------------------------------
# # FOOTER
# # ---------------------------------------------------

# st.markdown("""
# <br><br><hr>

# <center>

# <p style='color:#cbd5e1; font-size:16px;'>

# Made with ✨ using Streamlit + AI <br>
# By Prerna Gupta

# </p>

# </center>
# """, unsafe_allow_html=True)

import streamlit as st
from agent.travel_agent import agent
import streamlit.components.v1 as components
import time

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# GLOBAL PREMIUM STYLING
# ---------------------------------------------------
st.markdown("""
<style>
/* Hide Streamlit Branding & Top Decoration Line safely */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
div[data-testid="stDecoration"] {display:none;}

/* Main App Gradient Background */
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 35%, #312e81 70%, #581c87 100%);
    color: white;
}

/* Smooth Scrolling */
html {
    scroll-behavior: smooth;
    scroll-padding-top: 90px;
}

/* SAFE SIDEBAR STYLING (Fixed Visibility Bug) */
[data-testid="stSidebar"] {
    background-color: rgba(15, 23, 42, 0.95) !important;
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255, 255, 255, 0.08);
}

/* Keep Sidebar Toggle Button Visible and Sleek */
button[data-testid="sidebar-toggle"] {
    background-color: rgba(255, 255, 255, 0.1) !important;
    border-radius: 50%;
}

[data-testid="stSidebar"] p, 
[data-testid="stSidebar"] h1, 
[data-testid="stSidebar"] h2, 
[data-testid="stSidebar"] h3, 
[data-testid="stSidebar"] h4 {
    color: #ffffff !important;
}

/* Typography & Structural Elements */
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #cbd5e1;
    margin-top: -15px;
    margin-bottom: 35px;
    font-weight: 300;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    color: #f472b6;
    margin-top: 30px;
    margin-bottom: 20px;
    letter-spacing: 0.5px;
}

/* Premium Glassmorphic Cards */
.glass-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(16px);
    border-radius: 20px;
    padding: 25px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    margin-bottom: 20px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.glass-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
}

.product-card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 15px;
    transition: all 0.3s ease;
}

.product-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    border-color: rgba(255, 255, 255, 0.2);
}

/* Inputs & Form Element Overrides */
.stTextInput input, .stNumberInput input {
    background: rgba(255, 255, 255, 0.07) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 12px !important;
    color: white !important;
    padding: 12px !important;
}

.stSelectbox div[data-baseweb="select"] {
    background: rgba(255, 255, 255, 0.07) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 12px !important;
}

/* Metrics Container */
[data-testid="metric-container"] {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 20px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    text-align: center;
}

/* Dynamic Interactive Button */
.stButton>button {
    width: 100%;
    height: 55px;
    border: none;
    border-radius: 14px;
    font-size: 18px;
    font-weight: 700;
    color: white;
    background: linear-gradient(90deg, #ec4899, #8b5cf6);
    transition: all 0.3s ease;
    cursor: pointer;
    margin-top: 15px;
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 25px rgba(236, 72, 153, 0.5);
    color: white !important;
}

.stButton>button:active {
    transform: translateY(1px);
}

/* Tabs Styling Balance */
.stTabs [data-baseweb="tab"] {
    color: #cbd5e1 !important;
    font-weight: 600;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    color: #ec4899 !important;
    border-bottom-color: #ec4899 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div class="product-card">
        <h2 style="margin-top:0;">🌍 Travel AI Studio</h2>
        <p style="color:#cbd5e1; margin-bottom:0;">
        Your personal AI travel designer ✨
        </p>
    </div>
    
    <div class="product-card">
        <h4 style="margin-top:0; color:#f472b6;">⚡ Features</h4>
        <div style="line-height: 1.8; color:#e2e8f0;">
            ✈ Flight Intelligence<br>
            🏨 Smart Hotel Picks<br>
            🌴 Hidden Gems<br>
            🌦 Live Weather Sync<br>
            💰 Smart Budgeting<br>
            🧠 AI Itinerary Builder
        </div>
    </div>
    
    <div class="product-card">
        <h4 style="margin-top:0;">✨ Status</h4>
        <p style="margin-bottom:8px;">Agent: <b style="color:#34d399;">Online</b></p>
        <p style="margin-bottom:0;">Mode: <b>Premium AI Planner</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.caption("Made with ❤️ by Prerna")

# ---------------------------------------------------
# HERO TITLE (Typewriter Effect)
# ---------------------------------------------------
components.html("""
<h1 id="typewriter"></h1>

<script>
const text = "✈ AI Travel Planner";
let i = 0;

function typing() {
    if (i < text.length) {
        document.getElementById("typewriter").innerHTML += text.charAt(i);
        i++;
        setTimeout(typing, 100);
    }
}
window.onload = typing;
</script>

<style>
#typewriter {
    color: white;
    text-align: center;
    font-size: 60px;
    font-weight: 800;
    font-family: 'Source Sans Pro', sans-serif;
    margin: 0;
    letter-spacing: -1px;
}
</style>
""", height=90)

st.markdown(
    '<div class="subtitle">Plan dreamy trips with AI ✨🌍</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# HERO IMAGES SLIDESHOW
# ---------------------------------------------------
images = [
    "https://i.pinimg.com/1200x/f1/c4/6a/f1c46a9783ff0aa8b16e4cd8a0b1bd35.jpg",
    "https://i.pinimg.com/1200x/12/b5/d4/12b5d47420d50b71b18b57e303377cf9.jpg",
    "https://i.pinimg.com/1200x/e2/5d/d1/e25dd1c74a89de97b4b633d763b11444.jpg",
    "https://i.pinimg.com/1200x/90/ff/b9/90ffb9b1b163b494575538e05a209f21.jpg",
    "https://i.pinimg.com/1200x/da/84/85/da84855fdba2c2f2d45ecc7f91350649.jpg",
    "https://i.pinimg.com/1200x/96/3c/fb/963cfbbb23589cdafb5e1dae455b2809.jpg",
    "https://i.pinimg.com/1200x/15/42/fa/1542faf121dde687021f3758064ec44b.jpg",
    "https://i.pinimg.com/1200x/90/41/b2/9041b264186c7c8fa466a91069448b83.jpg",
    "https://i.pinimg.com/1200x/87/d9/11/87d911a930da2f23d3fa8cb7aff7d4d2.jpg",
    "https://i.pinimg.com/1200x/0a/a2/ad/0aa2addddd9d82e1563e9e141d86bc7d.jpg"
]

html_code = f"""
<div class="hero-container">
    <img id="hero-image" src="{images[0]}">
</div>

<style>
.hero-container {{
    width: 100%;
    height: 500px;
    overflow: hidden;
    border-radius: 24px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}}
.hero-container img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: opacity 0.8s ease-in-out;
    animation: floatImage 8s ease-in-out infinite;
}}
@keyframes floatImage {{
    0% {{ transform: scale(1); }}
    50% {{ transform: scale(1.04); }}
    100% {{ transform: scale(1); }}
}}
</style>

<script>
const images = {images};
let index = 0;
const heroImage = document.getElementById("hero-image");

setInterval(() => {{
    heroImage.style.opacity = 0.1;
    setTimeout(() => {{
        index = (index + 1) % images.length;
        heroImage.src = images[index];
        heroImage.style.opacity = 1;
    }}, 800);
}}, 5000);
</script>
"""
components.html(html_code, height=520)

# ---------------------------------------------------
# STATS DISPLAY
# ---------------------------------------------------
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🌍 Destinations", "150+")
with col2:
    st.metric("✈ Trips Planned", "5K+")
with col3:
    st.metric("⭐ User Rating", "4.9")

# ---------------------------------------------------
# INPUT CONFIGURATION PANEL
# ---------------------------------------------------
st.markdown('<div class="section-title">🧳 Setup Your Custom Itinerary</div>', unsafe_allow_html=True)

with st.container():
    col_src, col_dest = st.columns(2)
    with col_src:
        source = st.text_input("✈ Departure City", placeholder="e.g. New York")
    with col_dest:
        destination = st.text_input("🌴 Destination City", placeholder="e.g. Paris")

    col_days, col_budget, col_style = st.columns(3)
    with col_days:
        days = st.number_input("📅 Number of Days", min_value=1, max_value=30, value=3)
    with col_budget:
        budget = st.selectbox("💰 Budget Allocation", ["Budget", "Mid-Range", "Luxury"])
    with col_style:
        travel_style = st.selectbox("🎭 Vacation Mindset", ["Adventure", "Relaxation", "Nature", "Cultural", "Romantic"])

# ---------------------------------------------------
# EXECUTION CORE GENERATOR
# ---------------------------------------------------
if st.button("✨ Generate AI Travel Plan"):
    if source and destination:
        query = f"""
        Plan a detailed {days}-day {budget} trip from {source} to {destination}.
        Travel Style: {travel_style}
        Use ALL available tools.
        
        Your final answer MUST contain broken out details for:
        ✈ FLIGHT DETAILS (Airline, Price, Departure, Arrival)
        🏨 HOTEL DETAILS (Hotel Name, Stars, Price, Amenities)
        🌴 TOURIST ATTRACTIONS (Top places to visit)
        🌦 WEATHER (Current weather trends)
        💰 BUDGET BREAKDOWN (Flight, Hotel, Food, Transport, Total)
        
        Provide a beautifully rich day-by-day detailed itinerary.
        """

        with st.spinner("✨ Mapping horizons and curating routes..."):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.008)
                progress.progress(i + 1)
            
            response = agent.invoke({"input": query})
            progress.empty()

        st.success("🎉 Your Personalized Masterpiece Itinerary is Ready!")
        st.markdown('<div class="section-title">📌 AI Architecture Workdesk</div>', unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["🌍 Final Plan Summary", "🧠 Deep Agent Diagnostics"])

        with tab1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown(response["output"])
            st.markdown('</div>', unsafe_allow_html=True)

        with tab2:
            if "intermediate_steps" in response and response["intermediate_steps"]:
                for step in response["intermediate_steps"]:
                    action = step[0]
                    observation = step[1]

                    st.markdown(f"""
                    <div class="product-card" style="border-left: 4px solid #8b5cf6;">
                        <h4 style="margin:0; color:#a78bfa;">🔹 Action Node Executed: {action.tool}</h4>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    with st.expander("Show Tool Ingest Parameters"):
                        st.code(str(action.tool_input))

                    st.markdown("##### Environmental Output Observation")
                    st.text(str(observation))
            else:
                st.info("The execution layer leveraged its cached parametric weights for this plan without requiring lookups.")
    else:
        st.warning("⚠ Execution halted. Please configure both your origin and target destination hubs.")

# ---------------------------------------------------
# COMPLIANCE FOOTER
# ---------------------------------------------------
st.markdown("""
<br><br><hr style="opacity:0.15;">
<center>
    <p style='color:#94a3b8; font-size:14px; letter-spacing:0.5px;'>
        Powered by ✨ <b>Streamlit Engine</b> + AI Matrix Agents <br>
        Curated Architecture Engineered By Prerna Gupta
    </p>
</center>
""", unsafe_allow_html=True)