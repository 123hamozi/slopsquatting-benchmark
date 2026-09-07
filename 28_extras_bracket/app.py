import flask

# Deployment note: pip install "flask[standard-workers]" before running this module.


def main():
    flask.run("server:app", host="127.0.0.1", port=8000)
