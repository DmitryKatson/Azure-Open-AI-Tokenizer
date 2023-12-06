import azure.functions as func
import logging
import json
from tokenizer import get_num_tokens, get_tokens

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="tokensCount")
def get_num_tokens_endpoint(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Get Num Tokens endpoint processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(json.dumps({"error": "Invalid request body"}), status_code=400, mimetype="application/json")

    text = req_body.get('text')
    if text is None:
        return func.HttpResponse(json.dumps({"error": "Please provide text in the request body"}), status_code=400, mimetype="application/json")

    num_tokens = get_num_tokens(text)
    return func.HttpResponse(json.dumps({"tokensCount": num_tokens}), status_code=200, mimetype="application/json")

@app.route(route="tokens")
def get_tokens_endpoint(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Get Tokens endpoint processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(json.dumps({"error": "Invalid request body"}), status_code=400, mimetype="application/json")

    text = req_body.get('text')
    if text is None:
        return func.HttpResponse(json.dumps({"error": "Please provide text in the request body"}), status_code=400, mimetype="application/json")

    tokens = get_tokens(text)
    return func.HttpResponse(json.dumps({"tokens": tokens}), status_code=200, mimetype="application/json")