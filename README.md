# Power BI Logistics Delay Dashboard

Sample dataset and layout notes for building a logistics KPI dashboard that
tracks shipment volume, on-time performance, and delays.

Steps:

1. `python data/generate_shipment_delays.py` to create `shipment_delays.csv`.
2. Import the CSV into Power BI (or Tableau).
3. Create measures using `layout/measures_dax.txt`.
4. Follow layout ideas in `layout/dashboard_notes.md`.
