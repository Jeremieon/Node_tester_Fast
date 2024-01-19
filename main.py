from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.responses import JSONResponse

app = FastAPI()

# Middleware to handle Trusted Hosts (allowing all hosts for simplicity in this example)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

@app.get("/")
def read_root(request: Request):
    # Extracting information from the request
    host = request.client.host
    uri = request.url.path
    status = "200 OK"
    browser_type = request.headers.get("User-Agent", "Unknown Browser")

    # Some text to be returned
    response_text = "Hello, this is a FastAPI app!"

    # Log the information (you can replace this with your own logging mechanism)
    print(f"Host: {host}, URI: {uri}, Status: {status}, Browser Type: {browser_type}")

    # Return the information as JSON
    return JSONResponse(content={"host": host, "uri": uri, "status": status, "browser_type": browser_type, "text": response_text})
