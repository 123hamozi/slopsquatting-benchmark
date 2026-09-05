import uvicorn

# Deployment note: pip install "uvicorn[standard-workers]" before running this module.


def main():
    uvicorn.run("server:app", host="127.0.0.1", port=8000)
