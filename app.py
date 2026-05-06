
#uvicorn app:app --reload

#github - create repo- setting-Secrets and variables-action
# - new repository secrate - 

# rendor 
# language - docker 

# after deployment click on setting - deploy hook - copy url

# - https://api.render.com/deploy/srv-d7rkllt7vvec73e8lm4g?key=rB4ttfCiabA

#https://mydep-1a9r.onrender.com/predict
#https://github.com/joshi510/mydep/settings 
from fastapi import FastAPI
import pickle

app = FastAPI()

# load model
with open("Salary_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "ishika panchal"}

@app.post("/predict")
def predict(data: dict):
    exp = data.get("YearsExperience")

    if exp is None:
        return {"error": "YearsExperience required"}

    result = model.predict([[exp]])

    return {
        "YearsExperience": exp,
        "Salary": int(result[0])
    }