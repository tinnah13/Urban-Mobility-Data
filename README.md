#  Urban Mobility Explorer

A full-stack analytics platform built on *7.4 million NYC Yellow Taxi trips* from January 2019. Explore urban mobility patterns through an interactive dashboard backed by a normalized SQLite database and a custom-algorithmic Flask API.



---

## 📽️ Video Walkthrough

*5-minute demo:* https://youtu.be/nmBGTlAgxGg

*Team task sheet:* https://docs.google.com/spreadsheets/d/1HR_35NDiP6F6vSzcYWngFthr4UJpLuXDboMtRYNDq64/edit?usp=sharing

*Scrum board:* https://trello.com/invite/b/6acfeab6d78d3ac63c14f932/ATTI1ee691d2a086bc1be34f87e62bb0996b5900CF56/urban-mobility-data


---

## 👥 Team

| Name | Role |  
|------|------|
| Albertine Umuhoza | Backend Lead 
| Eunice Nina Sangwa | Database Architect 
| Kevine Niyonkuru | Frontend Lead 
| Karen Stephy Musangwa | Algorithms & Docs 
---

## 📖 Overview

This project demonstrates a complete data engineering and analytics pipeline:

1.⁠ ⁠*Ingest* raw TLC parquet files (7.6M rows)
2.⁠ ⁠*Clean* duplicates, nulls, and physical outliers (~99.2% retention)
3.⁠ ⁠*Engineer* 8 derived features (speed, tip %, airport flag, etc.)
4.⁠ ⁠*Store* in a normalized SQLite star schema with indexes and views
5.⁠ ⁠*Serve* through 9 REST API endpoints (Flask + SQLAlchemy)
6.⁠ ⁠*Visualize* in an interactive dashboard with 4 charts and 7 KPIs
7.⁠ ⁠*Compute* top-K rankings via custom algorithms (no built-in sort)

---

```
## 🏗️ Architecture
┌──────────────────┐ HTTP/JSON ┌──────────────────┐ SQL ┌─────────────┐
│ Browser │ ◄─────────────────► │ Flask API │ ◄────────────► │ SQLite DB │
│ HTML/CSS/JS │ │ backend/app.py │ │ 7 tables │
│ Chart.js │ │ 9 endpoints │ │ + indexes │
└──────────────────┘ └────────┬─────────┘ └─────────────┘
│
┌───────┴────────┐
│ Custom DSA │
│ • Merge sort │
│ • Top-K heap │
│ • IQR detector│
└────────────────┘

```
text

---

```
## 📁 Project Structure
Urban-Mobility-Data/
├── backend/
│ ├── app.py Flask API entry point (9 endpoints)
│ ├── config.py Environment-driven config
│ ├── requirements.txt Python dependencies
│ ├── algorithms/
│ │ ├── custom_sort.py Merge sort + bounded top-K heap
│ │ └── anomaly_detector.py IQR-based outlier detector
│ ├── data_pipeline/
│ │ ├── loader.py Read parquet/CSV
│ │ ├── cleaner.py 6 cleaning rules
│ │ ├── features.py 8 engineered features
│ │ └── outlier_log.py Exclusion tracking
│ ├── db/
│ │ ├── schema.sql 7-table star schema + indexes + views
│ │ ├── build_database.py Full ETL orchestrator
│ │ └── seed.py Dimension seeder
│ ├── routes/ Blueprint scaffolding
│ ├── services/ Business logic layer
│ └── tests/ Test scaffolding
├── frontend/
│ ├── index.html Dashboard layout
│ ├── css/styles.css Responsive styling
│ └── js/
│ ├── api.js Fetch wrapper
│ ├── charts.js Chart.js renderers
│ └── app.js Dashboard controller
├── database/
│ ├── urban_mobility.db Built by build_database.py (gitignored)
│ └── dump.sql Schema + dimension dump
├── data/ Raw inputs (mostly gitignored)
│ ├── yellow_tripdata_2019-01.parquet
│ ├── taxi_zone_lookup.csv
│ └── taxi_zones/ Shapefile (.shp, .dbf, .shx, etc.)
├── docs/
│ ├── technical_report.md 2-3 page technical report
│ ├── cleaning_log.md Exclusion transparency log
│ └── screenshots/ Dashboard evidence
├── codevibe-reports/ Individual CodeVibe reports
├── notebooks/ Jupyter exploration notebooks
├── scripts/ Utility shell scripts
├── .env.example Config template
├── .gitignore
├── LICENSE
└── README.md ← you are here

text

```
---

## ⚙️ Setup Instructions

### Prerequisites

| Tool | Version | Download |
|------|---------|----------|
| Python | 3.10, 3.11, 3.12, or 3.13 | https://www.python.org/downloads/ |
| Git | Latest | https://git-scm.com/downloads |
| CodeVibe | 0.1.10 | Team-provided ⁠ .vsix ⁠ file |

	⁠⚠️ *Python 3.14 does NOT work with ⁠ pyarrow<20 ⁠. Use 3.13 or lower.*

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/tinnah13/Urban-Mobility-Data.git
cd Urban-Mobility-Data
Step 2 — Create a Virtual Environment
Windows (PowerShell):

powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
macOS / Linux:

bash
python3 -m venv .venv
source .venv/bin/activate
Troubleshooting — "running scripts is disabled":

powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.venv\Scripts\Activate.ps1
Your prompt should now show (.venv) at the start.

Step 3 — Install Dependencies
bash
pip install --upgrade pip
pip install -r backend/requirements.txt
Expected: packages include flask, flask-cors, pandas, pyarrow, sqlalchemy, python-dotenv.

Verify installation:

bash
python -c "import pandas, pyarrow, sqlalchemy, flask; print('All packages OK')"
Expected output: All packages OK

Step 4 — Obtain the Dataset
The raw TLC data is not included in this repository (too large for GitHub). Download it from the official source:

Yellow taxi trips (fact table):

Visit https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

Scroll to 2019 → Yellow Taxi Trip Records → January 2019

Download either:

yellow_tripdata_2019-01.parquet (recommended — 105 MB, 3-second load)

yellow_tripdata_2019-01.csv (655 MB, 60-second load)

Save to: data/

Zone lookup (dimension):

Provided in repo at data/taxi_zone_lookup.csv

Zone shapefile (spatial metadata):

Provided in repo at data/taxi_zones/

After this step, data/ should contain:

text
data/
├── yellow_tripdata_2019-01.parquet   (105 MB)
├── taxi_zone_lookup.csv              (12 KB)
└── taxi_zones/                       (shapefile folder)
    ├── taxi_zones.shp
    ├── taxi_zones.shx
    ├── taxi_zones.dbf
    ├── taxi_zones.prj
    └── ...
Step 5 — Build the Database
bash
python backend/db/build_database.py
This runs the full ETL pipeline. Runtime: ~15 minutes.

Expected output:

text
=== Urban Mobility Explorer — Database Builder ===
Loading trips from yellow_tripdata_2019-01.parquet ...
  Loaded 7,667,792 rows, 18 columns
Cleaning ...
  Removed duplicates: 0
  Removed missing-critical: 0
  Removed temporal anomalies: 6,562
  Removed distance anomalies: 48,975
  Removed fare anomalies: 5,714
  Removed passenger anomalies: 1
Engineering features ...
Building database ...
Applied schema from schema.sql
Seeding dimensions ...
  Seeded 265 taxi zones
Building dim_time ...
  dim_time has 2,468,631 unique timestamps
Inserting trips ...
  Inserting 7,635,365 trips in batches of 100,000 ...
    ✓ 100,000 / 7,635,365  (skipped 1,898)
    ✓ 200,000 / 7,635,365  (skipped 21,462)
    ...
  Total inserted: 7,463,010, skipped: 172,355

============================================================
 CLEANING REPORT
============================================================
 Raw rows:                7,696,617
 Duplicates:             -0
 Missing critical:       -0
 Temporal anomalies:     -6,562
 Distance anomalies:     -48,975
 Fare anomalies:         -5,714
 Passenger anomalies:    -1
------------------------------------------------------------
 Kept:                    7,635,365  (99.2%)
============================================================
 DB location:  database/urban_mobility.db
============================================================
If the build fails, check:

data/yellow_tripdata_2019-01.parquet exists (or the .csv fallback)

Python is 3.13 or lower (3.14 will crash on pyarrow)

The venv is activated

Step 6 — Verify the Database
bash
python -c "import sqlite3; c=sqlite3.connect('database/urban_mobility.db'); print('Trips:', c.execute('SELECT COUNT() FROM trips').fetchone()[0]); print('Zones:', c.execute('SELECT COUNT() FROM taxi_zones').fetchone()[0]); print('Times:', c.execute('SELECT COUNT(*) FROM dim_time').fetchone()[0])"
Expected output:

text
Trips: 7463010
Zones: 263
Times: 2468631
Step 7 — Run the Backend
bash
python backend/app.py
Expected output:

text
Database: .../database/urban_mobility.db
Frontend: .../frontend
Starting Flask on http://localhost:5000 ...
 * Running on http://127.0.0.1:5000
 * Debug mode: on
Leave this terminal running.

Step 8 — Open the Dashboard
In your browser, navigate to:

text
http://localhost:5000/
Expected dashboard:

7 KPI cards (Total Trips, Avg Fare, Total Revenue, etc.)

4 charts (Demand by Hour, Trips by Borough, Top 10 Zones, Airport vs City)

Filter bar (Borough, Payment, Fare range, Airport toggle)

Sample Trips table (100 rows)

Story panel with 3 insights

Screenshot reference: docs/screenshots/kpi-chart.png

Step 9 — Test the API (Optional)
With Flask running, open a second terminal:

bash
curl http://localhost:5000/api/health
Expected:

json
{"status": "ok", "trips": 7463010}
All endpoints:

Method	Path	Description
GET	/api/health	Liveness + trip count
GET	/api/summary	7 dashboard KPIs
GET	/api/hourly	Trips per hour of day
GET	/api/boroughs	Trips per borough
GET	/api/top-zones?k=10	Top-K pickup zones (custom algorithm)
GET	/api/trips?borough=&payment=&min_fare=&max_fare=&airport=	Filtered trips
GET	/api/anomalies?limit=5000	IQR outlier detection
GET	/api/filters	Dropdown metadata
GET	/api/insights	Storytelling panels
GET	/api/ping	Trivial liveness
GET	/api/version	Static metadata
Step 10 — Stop the Server
Press Ctrl + C in the terminal running Flask.

🔄 Rebuilding From Scratch
If you need to reset:

bash
# Delete the built database
rm database/urban_mobility.db  # on Windows: Remove-Item database\urban_mobility.db

# Rebuild (15 min)
python backend/db/build_database.py
🧠 Custom Algorithms
All three are implemented by hand — no sorted(), heapq, numpy, or scipy.

1.⁠ ⁠Merge Sort — backend/algorithms/custom_sort.py
Time: O(n log n) guaranteed

Space: O(n)

Why: Stable, predictable worst-case, parallelizable

2.⁠ ⁠Bounded Top-K Heap — same file
Time: O(n log K)

Space: O(K)

Why: When K << n (e.g., top 10 of 265), avoid full sort

3.⁠ ⁠IQR Anomaly Detector — backend/algorithms/anomaly_detector.py
Time: O(n log n)

Space: O(n)

Why: Robust to extreme outliers — uses percentiles, not mean/std-dev

See docs/technical_report.md for full pseudo-code and complexity analysis.

🗄️ Database Schema
Star schema with 5 dimensions + 1 time dimension + 1 fact table:

Table	Rows	Purpose
boroughs	7	Borough dimension
service_zones	5	Service zone dimension
taxi_zones	263	Zone dimension (FK to borough)
payment_types	6	Payment method lookup
rate_codes	7	Rate type lookup
dim_time	2.47M	Star-schema time dimension
trips	7.46M	Fact table (24 columns, 13 indexes)
Views:

v_hourly_demand — trips + avg fare + avg speed per hour

v_zone_performance — trip counts + revenue per zone

Full DDL: backend/db/schema.sql

🐛 Troubleshooting
Problem	Fix
ModuleNotFoundError on any import	Venv not activated — run .venv\Scripts\Activate.ps1
ValueError: Number is not int on CSV load	Use the parquet input; pandas dtype inference fails on some CSV columns
Recv failure: Connection was reset on git push	Network blocks GitHub HTTPS — use mobile hotspot or SSH
FOREIGN KEY constraint failed	Zone IDs 264/265 are intentionally skipped by the ETL
no such table: trips	Database not built — run python backend/db/build_database.py
Port 5000 already in use	Kill the old process: netstat -ano | findstr :5000 → taskkill /PID <pid> /F
Charts empty in browser	Open DevTools → Console for JS errors. Check /api/* requests return 200
Python 3.14 crash on pyarrow	Downgrade to Python 3.12 or 3.13
📊 Key Findings
From 7.46 million cleaned trips:

Evening peak — 18:00 is the busiest hour with 500,639 trips, 16× the 04:00 trough

Manhattan dominance — ~92% of all pickups happen in Manhattan

Airport premium — Airport trips average $49.52** vs **$13.16 for city trips (3.8× multiplier)



📚 References
NYC TLC Trip Record Data

TLC Trip Record User Guide

Taxi Zone Lookup Table

Chart.js Documentation

Flask Documentation

SQLAlchemy Core
