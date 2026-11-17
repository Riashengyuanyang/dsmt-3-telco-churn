# Telco Churn Prediction

This project predicts whether a telecom customer will leave (churn),
using a logistic regression model trained on the IBM Telco Customer Churn dataset.

## Features used by the model

- **tenure**: months the customer has stayed with the company
- **monthly**: monthly charges
- **techsupport**: whether the customer has tech support (1 = yes, 0 = no)

## Parts of the project

- A FastAPI app (`api.py`) for local predictions
- An Azure Function (`function_app.py`) for predictions in the cloud
- A Streamlit dashboard (`dashboard.py`) to try the model in a browser

See [Calling the predict endpoint](predict.md) for how to use the API.