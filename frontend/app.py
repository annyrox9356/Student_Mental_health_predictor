import streamlit as st
import requests

# Page setup
st.set_page_config(page_title="Mental Health Predictor", page_icon="🧠", layout="centered")

st.title("🧠 Student Mental Health Predictor")
st.markdown("Enter your academic, lifestyle, and demographic details below to get an AI-driven mental health score prediction.")
st.divider()

# Create layout with two columns for a clean form UI
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=20)
    gender = st.selectbox("Gender", ["Male", "Female"])
    country = st.text_input("Country", value="India")
    academic_level = st.selectbox("Academic Level", ["Undergraduate", "Graduate", "High School"])
    stress_level = st.selectbox("Stress Level", ["Low", "Medium", "High", "Very High"])
    study_hours = st.number_input("Study Hours (Daily)", min_value=0.0, value=5.0, step=0.5)

with col2:
    platform = st.selectbox("Most Used Social Platform", ["Facebook", "LinkedIn", "Instagram", "Snapchat", "Twitter", "YouTube", "TikTok", "LINE", "KakaoTalk", "VKontakte", "WhatsApp", "WeChat"])
    purpose = st.selectbox("Purpose of Use", ["Networking", "Education", "Entertainment", "News"])
    daily_usage = st.number_input("Avg Daily Usage (Hours)", min_value=0.0, value=4.0, step=0.5)
    daily_unlocks = st.number_input("Daily Phone Unlocks", min_value=0, value=50)
    physical_activity = st.number_input("Physical Activity (Hours)", min_value=0.0, value=1.0, step=0.5)
    sleep_hours = st.number_input("Sleep Hours Per Night", min_value=0.0, value=7.0, step=0.5)

st.divider()

# Submit Button
if st.button("Predict Mental Health Score", type="primary"):
    
    # 1. Pydantic schema ke exact variables match karke JSON payload banayein
    payload = {
        "Age": age,
        "Gender": gender,
        "Country": country,
        "Academic_Level": academic_level,
        "Most_Used_Platform": platform,
        "Purpose_Of_Use": purpose,
        "Avg_Daily_Usage_Hours": daily_usage,
        "Daily_Unlocks": daily_unlocks,
        "Study_Hours": study_hours,
        "Physical_Activity_Hours": physical_activity,
        "Sleep_Hours_Per_Night": sleep_hours,
        "Stress_Level": stress_level
    }
    
    # 2. FastAPI ka local URL (Dhyan rakhein ki background me FastAPI chal raha ho)
    api_url = "http://backend:8000/predict"
    
    try:
        with st.spinner("Analyzing data through XGBoost pipeline..."):
            # 3. Backend ko POST request bhejein
            response = requests.post(api_url, json=payload)
        
        # 4. Response handle karein
        if response.status_code == 200:
            result = response.json()
            score = result.get("predicted_mental_health_score")
            st.success(f"### 🎯 Predicted Mental Health Score: **{score}**")
            # st.balloons()
        elif response.status_code == 422:
            st.error("Validation Error: Backend rejected the input format. Please check values.")
        else:
            st.error(f"Backend Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        st.error("❌ Failed to connect to the backend API. Please ensure your FastAPI server is running on port 8000.")