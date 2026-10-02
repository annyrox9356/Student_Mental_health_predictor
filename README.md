# Student Mental Health Predictor API 🧠💻

An end-to-end Machine Learning pipeline, RESTful API, and interactive Web UI designed to predict the mental health scores of students based on their academic pressure, digital lifestyle, and demographic factors. 

This project transitions a raw data science notebook into a production-ready MLOps architecture, featuring a completely decoupled training pipeline, a high-performance serving layer, and a user-friendly frontend.

### 🚀 Key Features
* **Advanced ML Inference:** Utilizes an optimized XGBoost Regressor to predict mental health scores with high accuracy.
* **Production-Grade API:** Built with FastAPI for lightning-fast, concurrent HTTP request handling and automatic Swagger UI documentation.
* **Interactive Frontend:** Features a clean, intuitive web interface built with Streamlit that seamlessly communicates with the backend API.
* **Bulletproof Data Validation:** Implements strict data validation and automated formatting (handling edge cases, casing, and spaces) using Pydantic models and `@field_validator`.
* **Modular MLOps Architecture:** Strict separation of concerns between model training (`pipeline.py`, `data_processor.py`), API serving (`main.py`, `inference.py`), and client UI (`app.py`).
* **Complex Feature Engineering:** Integrates Target Encoding, Ordinal Encoding, Label Encoding, and external JSON-based mapping for geographic data.

### 🛠️ Technology Stack
* **Machine Learning:** Python, XGBoost, Scikit-Learn, Pandas, Joblib
* **Backend Framework:** FastAPI, Uvicorn
* **Frontend UI:** Streamlit, Requests
* **Data Validation:** Pydantic
* **Version Control:** Git & GitHub

### 📂 Repository Structure
* `/api`: Contains the FastAPI application, routing (`main.py`), Pydantic schemas (`schemas.py`), and the thread-safe ML execution engine (`inference.py`).
* `/artifacts`: Stores all serialized `.pkl` files including the trained XGBoost model and various encoders.
* `/config`: Holds external mapping configurations (e.g., `country_tiers.json`).
* `/frontend`: Contains the Streamlit web application (`app.py`) that acts as the client-side UI.
* `/model_training`: Contains the offline Object-Oriented ML training pipeline and data processing scripts.

### ⚙️ How to Run Locally

1. **Clone this repository:**
   ```bash
   git clone https://github.com/annyrox9356/Student_Mental_health_predictor.git
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate ML Artifacts:** 
   Run the training pipeline to train the XGBoost model and generate the necessary `.pkl` files in the `/artifacts` directory.
   ```bash
   python model_training/pipeline.py
   ```

4. **Start the FastAPI Backend (Terminal 1):**
   ```bash
   uvicorn api.main:app --reload
   ```

5. **Start the Streamlit Frontend (Terminal 2):**
   Open a new terminal window/tab and run:
   ```bash
   streamlit run frontend/app.py
   ```

6. **Access the Application:** 
   * **Web UI:** Open `http://localhost:8501` in your browser to use the interactive predictor.
   * **API Docs:** Access the FastAPI Swagger UI at `http://127.0.0.1:8000/docs`.
