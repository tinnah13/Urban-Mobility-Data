"""
routes package
==============

Logical grouping of the API route handlers:

    health       liveness + database check
    summary      dashboard KPIs
    analytics    hourly / borough aggregations
    trips        filtered trip list
    zones        top-K pickup zones (custom algorithm)
    anomalies    IQR outlier detection (custom algorithm)
                        
Note: the current version of the app defines routes inline in app.py
for simplicity. This package exists as the target for a future
blueprint-based refactor.
"""
