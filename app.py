
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from uvicorn import run as app_run

from typing import Optional

from Housing_sales.constants import APP_HOST, APP_PORT
from Housing_sales.pipeline.prediction_pipeline import bank_loan,bankClassifier
from Housing_sales.pipeline.training_pipeline import TrainPipeline

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='templates')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.age: Optional[str] = None
        self.balance: Optional[str] = None
        self.contact: Optional[str] = None
        self.duration: Optional[str] = None
        self.housing: Optional[str] = None
        self.job: Optional[str] = None
        self.month: Optional[str] = None
        self.pdays: Optional[str] = None
        self.poutcome: Optional[str] = None
        self.previous: Optional[str] = None
        

    async def get_usvisa_data(self):
        form = await self.request.form()
        self.age = form.get("age")
        self.balance = form.get("balance")
        self.contact = form.get("contact")
        self.duration = form.get("duration")
        self.housing = form.get("housing")
        self.job = form.get("job")
        self.month = form.get("month")
        self.pdays = form.get("pdays")
        self.poutcome = form.get("poutcome")
        self.previous = form.get("previous")

@app.get("/", tags=["authentication"])
async def index(request: Request):

    return templates.TemplateResponse(
            "U1.html",{"request": request, "context": "Rendering"})


@app.get("/train")
async def trainRouteClient():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/")
async def predictRouteClient(request: Request):
    try:
        form = DataForm(request)
        await form.get_usvisa_data()
        
        loan_data = bank_loan(
                age=form.age,
                balance=form.balance,
                contact=form.contact,
                duration=form.duration,
                housing=form.housing,
                job=form.job,
                month=form.month,
                pdays=form.pdays,
                poutcome=form.poutcome,
                previous=form.previous
            )

        
        loan_df = loan_data.get_usvisa_input_data_frame()

        model_predictor = bankClassifier()

        value = model_predictor.predict(dataframe=loan_df)[0]

        status = None
        if value == 1:
            status = "Loan-approved"
        else:
            status = "Loan Not-Approved"

        return templates.TemplateResponse(
            "U1.html",
            {"request": request, "context": status},
        )
        
    except Exception as e:
        return {"status": False, "error": f"{e}"}


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)