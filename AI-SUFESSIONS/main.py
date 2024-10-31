import os
import google.generativeai as genai
import streamlit as st
from googletrans import Translator, LANGUAGES

# Set up page configuration
st.set_page_config(
    page_title="Urban Development Expert",
    page_icon="🌆",
    layout="wide",
    initial_sidebar_state="expanded",
)

translator = Translator()

# Header section with custom styling
st.markdown(
    """
    <style>
        .header-style {
            font-size:40px;
            color:#4CAF50;
            text-align:center;
            font-weight: bold;
        }
        .subheader-style {
            font-size:20px;
            color:#555555;
            text-align:left;
            padding-top: 20px;
        }
        .selectbox-style {
            font-size:18px;
            color:#333333;
        }
        .button-style {
            background-color: #4CAF50;
            color: white;
            font-size:18px;
            padding: 8px 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="header-style">Urban Development Suggestions 🌆</div>',
    unsafe_allow_html=True,
)

genai.configure(api_key="AIzaSyBfizIVkFzxgzC1hE2xoUbjfeq1yWOMIa4")

# List of major urban areas in India
urban_areas = sorted(
    [
        "Agartala",
        "Agra",
        "Ahmedabad",
        "Ahmednagar",
        "Aizawl",
        "Ajmer",
        "Akola",
        "Aligarh",
        "Alwar",
        "Ambattur",
        "Amravati",
        "Amritsar",
        "Anantapur",
        "Asansol",
        "Aurangabad",
        "Avadi",
        "Bangalore",
        "Bareilly",
        "Belgaum",
        "Bhagalpur",
        "Bhatpara",
        "Bhavnagar",
        "Bhilai Nagar",
        "Bhilwara",
        "Bhiwandi",
        "Bhopal",
        "Bhubaneswar",
        "Bikaner",
        "Bilaspur",
        "Bokaro Steel City",
        "Chandigarh",
        "Chennai",
        "Coimbatore",
        "Cuttack",
        "Davanagere",
        "Dehradun",
        "Delhi",
        "Dhanbad",
        "Durgapur",
        "Erode",
        "Faridabad",
        "Firozabad",
        "Ghaziabad",
        "Gorakhpur",
        "Gulbarga",
        "Guntur",
        "Gurgaon",
        "Guwahati",
        "Gwalior",
        "Dharwad",
        "Hyderabad",
        "Indore",
        "Jabalpur",
        "Jaipur",
        "Jalandhar",
        "Jalgaon",
        "Jammu",
        "Jamnagar",
        "Jamshedpur",
        "Jhansi",
        "Jodhpur",
        "Kakinada",
        "Kalyan-Dombivli",
        "Kamarhati",
        "Kanpur",
        "Kochi",
        "Kolhapur",
        "Kolkata",
        "Kollam",
        "Korba",
        "Kota",
        "Kozhikode",
        "Kurnool",
        "Latur",
        "Lucknow",
        "Ludhiana",
        "Madurai",
        "Maheshtala",
        "Malegaon",
        "Mangalore",
        "Mathura",
        "Meerut",
        "Moradabad",
        "Mumbai",
        "Muzaffarnagar",
        "Muzaffarpur",
        "Mysore",
        "Nagpur",
        "Nanded-Waghala",
        "Nashik",
        "Navi Mumbai",
        "Noida",
        "Panihati",
        "Patiala",
        "Patna",
        "Pimpri-Chinchwad",
        "Pune",
        "Raipur",
        "Rajahmundry",
        "Rajkot",
        "Rajpur Sonarpur",
        "Ranchi",
        "Rohtak",
        "Saharanpur",
        "Salem",
        "Sangli-Miraj & Kupwad",
        "Shimoga",
        "Siliguri",
        "Solapur",
        "Srinagar",
        "Surat",
        "Thane",
        "Thiruvananthapuram",
        "Thrissur",
        "Tiruchirappalli",
        "Tirunelveli",
        "Udaipur",
        "Ujjain",
        "Ulhasnagar",
        "Vadodara",
        "Varanasi",
        "Vasai-Virar",
        "Vijayawada",
        "Visakhapatnam",
        "Warangal",
    ]
)

# City selection with improved section styling
st.markdown(
    '<div class="subheader-style">Select Your City</div>', unsafe_allow_html=True
)
selected_city = st.selectbox(
    "Choose a city for development suggestions:",
    urban_areas,
    help="Choose the city for which you want urban development insights.",
)


# Define function for getting the response
def get_response_diet(prompt, input_text):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([prompt, input_text])
        return response.text if response else None
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None


# Prompt for the urban development suggestion
input_prompt_diet = """
    You are an expert in urban development with extensive knowledge of city planning, infrastructure design, and the social and economic factors influencing urban areas. Assume you are consulting for a city that is experiencing slow growth and facing challenges related to transportation, housing, and green space preservation. Provide insights and actionable recommendations for urban development, focusing on modern approaches like smart city technology, mixed-use zoning, and public-private partnerships. Please also consider environmental impact, community engagement, and resilience against climate change in your response.
"""

# Add interactive button with icon
submit1 = st.button(
    "💡 Get Suggestions",
    key="get_suggestions",
    help="Click to generate urban development suggestions",
)

if submit1:
    with st.spinner("Generating Suggestions..."):
        response = get_response_diet(input_prompt_diet, selected_city)

        if response:
            st.write("### Suggested Urban Development Plan")
            st.success(response)
        else:
            st.error("Failed to generate a suggestion. Please try again.")

st.markdown("---")
st.markdown(
    """
### Made with ❤️ by [Megh Deb](https://github.com/Megh2005) & [Srinath Sahu](https://github.com/Srinath-Sahu)
"""
)
