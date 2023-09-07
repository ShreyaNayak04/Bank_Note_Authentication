import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

# create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

#Index Route
@app.get("/")  
def index():
    return {"message":"Hello"}

#Route with a single parameter
@app.get('/{name}')
def get_name(name:str):
    return {"Welcome " : f'{name}'}

@app.post('/predict')
def predict_banknote(data:BankNote):
    data=data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    
    prediction=classifier.predict([[variance,skewness, curtosis,entropy ]])
    if(prediction[0]>0.5):
        prediction="Fake Note"
    else:
        prediction="Its a Bank Note"
    return {
        'prediction':prediction
    }        
    
    
#Eun the API with uvicorn
if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1', port=8000)    
    
#uvicorn app:app --reload    