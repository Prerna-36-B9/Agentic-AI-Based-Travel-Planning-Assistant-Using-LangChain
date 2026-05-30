# 🌍 Agentic AI-Based Travel Planning Assistant Using LangChain

## 📌 Overview
Travel planning often feels overwhelming—users juggle multiple websites, compare inconsistent information, and manually stitch together itineraries that may be inefficient or incomplete.  
This project builds an **Agentic AI Travel Assistant** using **LangChain** and **OpenRouter AI**, capable of integrating real-time data, reasoning like a travel expert, and generating optimized itineraries tailored to user preferences.

---

## 🎯 Problem Statement
Planning a trip requires balancing flights, hotels, attractions, time, budget, weather, distance, and personal interests.  
Current solutions force travelers to switch between platforms, leading to fragmented experiences.  
**Our solution:** An AI-powered assistant that automates this process, providing **personalized, efficient, and realistic itineraries**—all in one place.

---

## 💼 Business Use Cases
This system can be applied in:
- Travel agencies and tourism companies  
- Hotel platforms and airline aggregators  
- Self-service travel planning tools  

**Benefits:**
- Reduce customer support workload  
- Provide personalized recommendations  
- Automate itinerary design  
- Improve customer satisfaction  
- Save users time and money  

Companies like **MakeMyTrip, Booking.com, ClearTrip, and Ixigo** are already adopting conversational and agentic AI to enhance user experience.

---

## 🛠️ Skills Takeaway
By completing this project, I gained hands-on expertise in:
- **Python Programming**  
- **LLM Integration**  
- **Agentic AI (LangChain)**  
- **Prompt Engineering**  
- **API Integration**  
- **Streamlit Development**

---

## 🎯 Project Objectives
### ✔ Primary Objectives
- Build an agentic AI system using LangChain that autonomously creates trip itineraries.  
- Integrate tools for:
  - Flight search (JSON dataset)  
  - Hotel suggestions (JSON dataset)  
  - Places/POIs search (JSON dataset)  
  - Real-time weather (Open-Meteo API)  
- Enable multi-step reasoning and decision-making (ReAct / ToolCalling agents).  
- Generate structured itineraries with:
  - Day-wise plan  
  - Accommodation  
  - Weather expectations  
  - Budget estimation  

### ✔ Secondary Objectives
- Implement filtering, ranking, and optimization (cheapest flight, highest-rated hotel, etc.).  
- Ensure the system can justify decisions (“Why we selected this?”).  
- Provide outputs in clean JSON + human-readable format.  
- Build a simple interface (CLI or Streamlit).

---

## 🚀 Project Approach
### Step 1 — Data Setup
- Use provided datasets: `flights.json`, `hotels.json`, `places.json`  
- Call real API: **Open-Meteo** (no API key required)

### Step 2 — Build Tools
- **Flight Search Tool** – filters by source/destination, suggests cheapest/fastest flight  
- **Hotel Recommendation Tool** – filters by city, rating, price  
- **Places Discovery Tool** – recommends attractions based on type & rating  
- **Weather Lookup Tool** – provides forecast for travel dates  
- **Budget Estimation Tool** – sums flight + hotel + per-day local expenses  

### Step 3 — Create the Agent
- Build a LangChain ReAct or ToolCalling Agent  
- Responsibilities:
  - Understand user’s travel query  
  - Decide which tools to call  
  - Retrieve and analyze data  
  - Construct 3–7 day itinerary  
  - Estimate cost  
  - Produce final structured output  

### Step 4 — Generate Final Output
The agent provides:
- Trip Summary  
- Flight Option Selected  
- Hotel Recommendation  
- Day-wise Itinerary  
- Weather for Each Day  
- Budget Breakdown  
- Reasoning (optional)

---

## 📊 Expected Results
Example output:

✈ FLIGHT DETAILS

Airline: SpiceJet
Price: ₹3304
Departure: 2025-07-15 at 14:38
Arrival: 2025-07-15 at 18:38
🏨 HOTEL DETAILS
Day 1-3: Royal Heritage

Stars: 5
Price/Night: ₹1232
Total for 2 Nights: ₹2464
Amenities: WiFi, parking, breakfast, pool
🌴 TOURIST ATTRACTIONS

Day 1:

Dudhsagar Falls (Waterfall, Rating: 4.8)
Baga Beach (Beach, Rating: 4.7)
Day 2:

Basilica of Bom Jesus (Church, Rating: 4.7)
Calangute Beach (Beach, Rating: 4.6)
Day 3:

Fort Aguada (Fort, Rating: 4.5)
🌦 WEATHER

Current Temperature: 26.6°C
Max Temperature: 35.3°C
Min Temperature: 26.4°C
💰 BUDGET BREAKDOWN

Flight: ₹3304
Hotel: ₹2464 (for 2 nights)
Food: ₹1500 (approx. ₹500/day)
Transport: ₹1000 (local transport and activities)
Total Estimated Budget: ₹9268
Day-by-Day Itinerary
Day 1: Arrival and Beach Relaxation

Morning: Depart from Mumbai at 14:38, arrive in Goa at 18:38.
Evening: Check into Royal Heritage, enjoy dinner, and relax at Baga Beach.
Day 2: Adventure and Culture

Morning: Breakfast at the hotel, head to Dudhsagar Falls for a trek (book a guided tour for safety).
Afternoon: Lunch at a local eatery, then visit Basilica of Bom Jesus for some cultural exploration.
Evening: Wind down at Calangute Beach, enjoy water sports or a beachside dinner.
Day 3: Historic Exploration and Departure

Morning: Visit Fort Aguada after breakfast.
Afternoon: Explore local markets for souvenirs, have lunch.
Evening: Prepare for departure, check out, and take a taxi to the airport for your flight back to Mumbai.
This detailed itinerary ensures a balanced mix of adventure, relaxation, and cultural experiences while keeping your budget in check. Enjoy your trip to Goa!


---

## 📂 Data Sources
- **Flights, Hotels, Places (JSON files):** [Drive Link](https://drive.google.com/drive/folders/18TK-2VfwoFRA515CbI9yfv9dwW74HbX0?usp=sharing)  
- **Weather Data (Live & Free):** [Open-Meteo API](https://api.open-meteo.com/v1/forecast)

---

## 🖥️ Tech Stack
- **LangChain** – Agentic AI framework  
- **OpenRouter AI** – LLM integration  
- **Python** – Core programming  
- **Streamlit** – Interactive UI  
- **JSON Datasets** – Flights, Hotels, Places  
- **Open-Meteo API** – Real-time weather  

---

## 📌 Project Guidelines
- Follow **PEP 8** coding standards  
- Modularize code into functions/classes  
- Implement error handling (try-except blocks)  
- Document with docstrings and README  
- Normalize SQL tables, use indexes  
- Streamlit UI: minimalist, interactive, responsive  

---

## 📅 Timeline
The project must be completed and submitted within **15 days** from the assigned date.

---

## 📖 References
- [Streamlit Documentation](https://docs.streamlit.io/library/api-reference)  
- [LangChain Documentation](https://docs.langchain.com/)  
- Project orientation recording (provided by Labmentix)  
- GitHub workflow guide (provided in project resources)

---

## ✨ Outcome
This project demonstrates how **Agentic AI** can revolutionize travel planning by combining reasoning, automation, and real-time data. It showcases technical expertise in **LangChain, OpenRouter AI, and Streamlit**, while delivering a practical solution for the **Travel & Tourism** domain.
