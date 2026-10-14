"""
Health endpoint
===============
Exposes a lightweight liveness probe consumed by load balancers andmonitoring systems. The endpoint intentionally does the smallest possible
database query (a COUNT) so that it stays under 5 ms even at peak.and

Response shape:
    {"status": "ok", "trips": <int>}
"""

# Semantic version of the API surface. Bump major when routes change in
# # a way that breaks existing clients.
# API_VERSION = "1.0.0""""
