# Calling the predict endpoint

The model needs three inputs:

| Name | Type | Meaning |
|---|---|---|
| `tenure` | whole number | Months as a customer |
| `monthly` | number | Monthly charges |
| `techsupport` | 0 or 1 | 1 if the customer has tech support |

## Local API (FastAPI)

Start the API:

```bash
uv run uvicorn api:app --reload
```

Send a `POST` request with JSON:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"tenure": 12, "monthly": 70.5, "techsupport": 0}'
```

Open `http://127.0.0.1:8000/docs` to try it in the browser.
Wrong input types return status `422`.

## Azure Function

Send a `GET` request with the inputs in the query string:

```bash
curl "https://<your-app>.azurewebsites.net/api/predict?code=<your-function-key>&tenure=12&monthly=70.5&techsupport=0"
```

The response is plain text, for example:

```text
Churn probability: 0.5112
```

!!! warning
    The function key gives access to your function.
    Keep it in `.env` and never commit it.

!!! note
    The first call can take several seconds while Azure starts the function.