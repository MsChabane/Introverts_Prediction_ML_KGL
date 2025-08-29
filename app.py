from fastapi import FastAPI,status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, validator
from typing import Literal,Union,Optional
import os 
import joblib
import pandas as pd 

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
app = FastAPI()

model = joblib.load(os.path.join(BASE_DIR,'models','model.pkl'))
encoder = joblib.load(os.path.join(BASE_DIR,'models','encoder.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR,'models','scaler.pkl'))

class Error (BaseModel):
    error :str

class Output(BaseModel):
    prediction:Union[ Literal['Introvert','Extrovert'],None]
    probability:Union[float,None]
class PredictionOutput(BaseModel):
    response : Union[Output,Error]
    


class PredictionInput(BaseModel):
    Time_spent_Alone: int
    Stage_fear: Literal["yes", "no"]  
    Social_event_attendance: int  
    Going_outside: int 
    Drained_after_socializing: Literal["yes", "no"]  
    Friends_circle_size: int  
    Post_frequency: int 

    @validator('Time_spent_Alone', 'Going_outside', pre=True)
    def validate_hour_range(cls, v):
        if not isinstance(v, int) or v < 0 or v > 24:
            raise ValueError("Must be an integer between 0 and 24")
        return v

    @validator("Post_frequency", "Friends_circle_size", "Social_event_attendance", pre=True)
    def validate_positive_int(cls, v):
        if not isinstance(v, int) or v < 0:
            raise ValueError("Must be an integer greater than or equal to 0")
        return v

    @validator("Stage_fear", "Drained_after_socializing", pre=True)
    def validate_yes_no(cls, v):
        if isinstance(v, str):
            v = v.strip().lower()
        if v not in {"yes", "no"}:
            raise ValueError("Must be 'yes' or 'no'")
        return v

def predict(features:PredictionInput):
    das_code = [0,1] if features.Drained_after_socializing =='yes' else [1,0]
    sf_code = [0,1] if features.Stage_fear =='yes' else [1,0]
    
    features =scaler.transform([[
        features.Time_spent_Alone,
        features.Social_event_attendance,
        features.Going_outside,
        features.Friends_circle_size,
        features.Post_frequency,
        ]+sf_code+das_code
    ])
    pred=model.predict(features)
    proba=model.predict_proba(features)[0]


    return encoder.inverse_transform(pred)[0],proba[pred[0]]

    

@app.post("/predict",response_model=PredictionOutput)
def predict_route(input_data: PredictionInput):
    
    try :
        result=predict(input_data)
     
        output=Output(prediction=result[0],probability=result[1])   
        return JSONResponse(content=PredictionOutput(response=output).dict(),status_code=200)

    except Exception as e :  
        return JSONResponse(content=PredictionOutput(
            response=Error(error=f'INTERNAL SERVER ERROR :{e}')).dict(),status_code=200)
   
