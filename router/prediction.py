#import libraries
import pandas as pd

#load dataset
dataset = pd.read_csv(r"C:\Users\CHARAN\Datascience-programs\MachineLeaarningPrograms\LinearRegression\HousePricePrediction\house_price.csv")

X = dataset.iloc[:,:2].values
y = dataset.iloc[:,2].values

#split data for training and testing dataset
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y,test_size=0.25,random_state=0)

#prepn of machine learning model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

regressor.predict(X_test)

from fastapi import Request
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

router=APIRouter()




@router.get("/")
async def get_form_data(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@router.post("/price_prediction/")
async def predict_price(request:Request):
    form_data = await request.form()
    sq_feet = float(form_data['sq_feet'])
    rooms = int(form_data['rooms'])
    
    predicted_price=regressor.predict([[sq_feet,rooms]])
    return templates.TemplateResponse("index.html",{
        "request":request,
        "sq_feet":sq_feet,
        "rooms":rooms,
        "prediction":predicted_price})

