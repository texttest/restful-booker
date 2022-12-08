#!/bin/sh

if [ ! -d "venv" ]; then 
    python -m venv venv
fi
venv/bin/pip install -r requirements.txt
texttest -d . "$@"
