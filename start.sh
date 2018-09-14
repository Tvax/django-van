#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn vanlife_landing.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3