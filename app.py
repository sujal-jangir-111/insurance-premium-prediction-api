from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model , MODEL_VERSION 


app = FastAPI(title="Insurance Premium Prediction API")

# 1. Enable CORS for Streamlit / Frontend Access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -------------------- Endpoint --------------------   

@app.get("/")
def home():
    return {"message" : "Insurance premium prediction API"}

@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "model_version": MODEL_VERSION,
        "model_loaded": model is not None
    } 


@app.post("/predict", response_model = PredictionResponse)    # o/p will validate by this pydantic model before returning 
def predict_premium(data: UserInput):
     
    input_dict = {
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }

    try:

        prediction = predict_output(input_dict)


        return JSONResponse(status_code=200,content={"response": prediction})

    except Exception as e:

        return JSONResponse(status_code = 500, content = str(e)) 
 
















