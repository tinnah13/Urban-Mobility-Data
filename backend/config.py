"""
config.py  Environment-driven configuration
=============================================

Centralizes every environment variable and derived path used by the
Flask backend. Loading is delegated to python-dotenv so that local
development and production can share the same code path.

Environment variables consumed:
    DB_URL       SQLAlchemy connection string
    DATA_DIR     Directory holding raw input files
    FLASK_PORT   TCP port for the dev server
            
Design rationale:
    No module below this one should ever read os.environ directly. If a
    new setting is required, it must be declared here first. This keeps
    configuration deterministic and testable.
"""

# Rationale: loading dotenv at module scope guarantees .env is parsed
# # before any environment variable is read below."""

import os
from dotenv import load_dotenv
load_dotenv()
DB_URL = os.getenv('DB_URL', 'sqlite:///database/urban_mobility.db')
DATA_DIR = os.getenv('DATA_DIR', 'data')
FLASK_PORT = int(os.getenv('FLASK_PORT', 5000))
