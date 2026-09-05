#!/bin/bash
pip install gunicorn-asyncio-workers
gunicorn app:app
