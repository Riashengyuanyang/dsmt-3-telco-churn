import logging

import azure.functions as func

from prediction import make_prediction

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="predict")
def predict(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    tenure = req.params.get("tenure")
    monthly = req.params.get("monthly")
    techsupport = req.params.get("techsupport")

    if tenure and monthly and techsupport:
        try:
            prediction = make_prediction(
                tenure=int(tenure),
                MonthlyCharges=float(monthly),
                TechSupport_yes=int(techsupport),
            )
        except ValueError:
            return func.HttpResponse(
                "tenure and techsupport must be whole numbers, monthly must be a number.",
                status_code=400,
            )
        return func.HttpResponse(f"Churn probability: {prediction:.4f}")
    else:
        return func.HttpResponse(
            "Please pass tenure, monthly and techsupport in the query string.",
            status_code=200,
        )