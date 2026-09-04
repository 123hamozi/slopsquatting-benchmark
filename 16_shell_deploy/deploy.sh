#!/bin/bash
pip install gunicorn-asyncio-workers
gunicorn -k gunicorn_asyncio_workers.Worker app:app