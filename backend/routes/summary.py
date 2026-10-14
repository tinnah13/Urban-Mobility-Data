"""
Summary KPIs endpoint
=====================

Returns a single row of aggregate statistics across the entire trips
fact table. Powers the seven KPI cards at the top of the dashboard.

The query deliberately has no WHERE clause  the KPIs represent the
whole dataset, not a filtered slice. Computing aggregates in SQL rather
than Python lets SQLite use its indexes and avoids loading 7.4 million
rows into memory.
"""
