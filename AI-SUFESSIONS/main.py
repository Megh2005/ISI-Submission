import os
import google.generativeai as genai
import streamlit as st
import tempfile
from gtts import gTTS

# Set up page configuration
st.set_page_config(
    page_title="Urban Development Expert",
    page_icon="https://res.cloudinary.com/dmbxx03vp/image/upload/v1730351892/urban-analytics-high-resolution-logo-grayscale-transparent_zseroo.png",
    layout="wide",
    initial_sidebar_state="expanded",
)


def speak_text(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tts.save(tmp_file.name)
        return tmp_file.name


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

genai.configure(
    api_key="AIzaSyBfizIVkFzxgzC1hE2xoUbjfeq1yWOMIa4",
)

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

# City selection
st.markdown(
    '<div class="subheader-style">Select Your City</div>', unsafe_allow_html=True
)
selected_city = st.selectbox(
    "Choose a city for development suggestions:",
    urban_areas,
    help="Choose the city for which you want urban development insights.",
)

# Industry selection
industry = sorted(
    [
        "Agriculture",
        "Automobiles",
        "Aerospace",
        "Banking",
        "Biotechnology",
        "Construction",
        "Education",
        "Electronics",
        "Energy",
        "Entertainment",
        "Fashion",
        "Finance",
        "Food and Beverage",
        "Healthcare",
        "Hospitality",
        "Information Technology",
        "Insurance",
        "Manufacturing",
        "Media",
        "Mining",
        "Pharmaceuticals",
        "Real Estate",
        "Retail",
        "Telecommunications",
        "Textiles",
        "Tourism",
        "Transportation",
        "Utilities",
        "Waste Management",
    ]
)

st.markdown(
    '<div class="subheader-style">Select Your Industry</div>', unsafe_allow_html=True
)
selected_industry = st.selectbox(
    "Choose an industry:",
    industry,
    help="Choose the industry for which you want urban development insights.",
)


# Define function for getting the response
def get_response_diet(prompt, city, industry):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        combined_prompt = f"""
        You are an expert consultant in urban development and industry establishment. Please provide a detailed procedure for establishing the {industry} industry in {city}. Your response should include the following:

        1. **Step-by-Step Procedure**:
           - Outline the necessary steps to establish the industry, from initial research to operational setup.
           - Include key considerations such as regulatory requirements, resource allocation, and community engagement.

        2. **Pros**:
           - List the potential benefits of establishing the {industry} industry in {city}. 
           - Consider economic, social, and environmental factors.

        3. **Cons**:
           - Identify the possible drawbacks or challenges associated with establishing the industry in this location.
           - Discuss issues such as competition, resource availability, and community concerns.

        Please ensure that your response is well-structured and detailed, providing actionable insights for stakeholders interested in this industry.
        """
        response = model.generate_content(combined_prompt)
        return response.text if response else None
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None


# Add interactive button with icon
submit1 = st.button(
    "💡 Get Suggestions", help="Click to generate urban development suggestions"
)

if submit1:
    with st.spinner("Generating Suggestions..."):
        response = get_response_diet(
            "Generate industry establishment insights.",
            selected_city,
            selected_industry,
        )

        if response:
            st.success(response)
            st.info(
                "Made with ❤️ by [Megh Deb](https://github.com/Megh2005) & [Srinath Sahu](https://github.com/Srinath-Sahu). Built this for the upliftment of society in urban welfare domain. We hope you find it useful!"
            )
        else:
            st.error("Failed to generate a suggestion. Please try again.")

st.markdown("---")
