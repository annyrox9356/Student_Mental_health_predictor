from fastapi import FastAPI,HTTPException
from api.schemas import Data_validator
from api.inference import Inference

app=FastAPI()
infer=Inference()
@app.get('/')
def home():
    return {"message":"hello server is running"}

@app.post('/predict')
def transfer_data(data:Data_validator):
    try:
        encoded_data=infer.encode_data(data)
        prediction=infer.run_model(encoded_data)
        return{
            "predicted_mental_health_score":prediction
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


        