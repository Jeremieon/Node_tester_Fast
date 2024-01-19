from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.responses import JSONResponse

app = FastAPI()

# Middleware to handle Trusted Hosts (allowing all hosts for simplicity in this example)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

@app.get("/")
def read_root(request: Request):
    # Extracting information from the request
    client_host = request.client.host
    uri = request.url.path
    method = request.method
    headers = dict(request.headers)
    query_params = dict(request.query_params)
    cookies = dict(request.cookies)
    status = "200 OK"
    browser_type = headers.get("User-Agent", "Unknown Browser")

    # Some text to be returned
    response_text = "Hello, this is a FastAPI app!"

    # Log the information (you can replace this with your own logging mechanism)
    print(f"Client Host: {client_host}, URI: {uri}, Method: {method}, Status: {status}, Browser Type: {browser_type}")

    # Additional information to be included in the response
    response_data = {
        "client_host": client_host,
        "uri": uri,
        "method": method,
        "status": status,
        "browser_type": browser_type,
        "headers": headers,
        "query_params": query_params,
        "cookies": cookies,
        "text": response_text
    }

    # Return the information as JSON
    return JSONResponse(content=response_data)