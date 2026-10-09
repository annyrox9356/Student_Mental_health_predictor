# Student Mental Health Predictor API 🧠💻

An end-to-end Machine Learning pipeline, RESTful API, and interactive Web UI designed to predict the mental health scores of students based on their academic pressure, digital lifestyle, and demographic factors.

This project transitions a raw data science notebook into a production-ready MLOps architecture, featuring a completely decoupled training pipeline, a high-performance serving layer, a user-friendly frontend, and full containerization via Docker.

## 🚀 Key Features
- **Advanced ML Inference:** Utilizes an optimized XGBoost Regressor to predict mental health scores with high accuracy.
- **Production-Grade API:** Built with FastAPI for lightning-fast, concurrent HTTP request handling and automatic Swagger UI documentation.
- **Interactive Frontend:** Features a clean, intuitive web interface built with Streamlit that seamlessly communicates with the backend API via internal Docker networking.
- **Bulletproof Data Validation:** Implements strict data validation and automated formatting (handling edge cases, casing, and spaces) using Pydantic models.
- **Containerized Microservices:** Fully dockerized frontend and backend services orchestrated using `docker-compose`.
- **Automated CI/CD Pipeline:** Integrated GitHub Actions for automated model training, image building, and pushing to Docker Hub.

## 🛠️ Technology Stack
- **Machine Learning:** Python, XGBoost, Scikit-Learn, Pandas, Joblib
- **Backend Framework:** FastAPI, Uvicorn
- **Frontend UI:** Streamlit, Requests
- **DevOps & MLOps:** Docker, Docker Compose, GitHub Actions, Docker Hub
- **Version Control:** Git & GitHub

## 📂 Repository Structure
- `/api`: Contains the FastAPI application, routing (`main.py`), Pydantic schemas (`schemas.py`), and the ML execution engine (`inference.py`).
- `/frontend`: Contains the Streamlit web application (`app.py`) that acts as the client-side UI.
- `/model_training`: Contains the offline Object-Oriented ML training pipeline and data processing scripts.
- `docker-compose.yml`: Orchestrates the multi-container setup (frontend + backend).
- `.github/workflows/`: Contains CI/CD automation scripts for deploying to Docker Hub.

## ⚙️ How to Run Locally

### 🐳 Method 1: Using Docker (Recommended for Production/Testing)
This is the easiest and most reliable way to run the full-stack project in an isolated environment.

**⚠️ PREREQUISITES & WARNING:** 
- You **MUST have Docker Desktop installed and running** in the background on your PC before executing these commands.
- Ensure ports `8000` and `8501` are free on your system.

**Step 1: Clone this repository and navigate into the folder**
```bash
git clone https://github.com/annyrox9356/Student_Mental_health_predictor.git
cd Student_Mental_health_predictor
```

**Step 2: Pull the latest images and start the containers**
```bash
docker-compose pull
docker-compose up -d --force-recreate
```

**Step 3: Access the Application**
- **Web UI (Streamlit):** Open http://localhost:8501
- **API Docs (FastAPI Swagger):** Open http://localhost:8000/docs

**Step 4: To stop the application and clean up resources**
```bash
docker-compose down
```

---

### 💻 Method 2: Manual Local Setup (For Development/Code Changes)
Use this method if you want to test code changes locally without rebuilding Docker images.

**Step 1: Clone this repository and navigate into it**
```bash
git clone [https://github.com/annyrox9356/Student_Mental_health_predictor.git](https://github.com/annyrox9356/Student_Mental_health_predictor.git)
cd Student_Mental_health_predictor
```

**Step 2: Install the required dependencies**
```bash
pip install -r requirements.txt
```

**Step 3: Generate ML Artifacts (if making changes to the model)**
```bash
python model_training/pipeline.py
```

**Step 4: Start the FastAPI Backend (Terminal 1)**
```bash
uvicorn api.main:app --reload
```

**Step 5: Start the Streamlit Frontend (Terminal 2)**
*(Note: Ensure `api_url` in `frontend/app.py` is temporarily set to `http://127.0.0.1:8000/predict` for this manual method)*
```bash
streamlit run frontend/app.py
```