"""
Analytics endpoints
===================

Two related aggregations that feed the chart section of the dashboard:

    GET /api/hourly    trips per hour of day
    GET /api/boroughs  trips per pickup borough
        
Both queries follow the classic star-schema traversal pattern:
    trips  ->  dim_time    for temporal grouping
    trips  ->  taxi_zones  ->  boroughs    for geographic grouping
Because the foreign-key columns are indexed, these joins complete in
under 100 ms even with 7.4M fact rows.
"""
