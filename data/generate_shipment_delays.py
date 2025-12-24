import random
from datetime import datetime, timedelta
from pathlib import Path

HUBS = ["ATL", "MEM", "IND", "DFW", "LAX", "EWR"]
REGIONS = {
    "ATL": "US-South",
    "MEM": "US-South",
    "IND": "US-Midwest",
    "DFW": "US-South",
    "LAX": "US-West",
    "EWR": "US-East",
}


def main(days: int = 60) -> None:
    start = datetime(2024, 1, 1)
    lines = ["date,hub,region,total_shipments,late_shipments,avg_delay_hours"]

    for d in range(days):
        day = (start + timedelta(days=d)).strftime("%Y-%m-%d")
        for hub in HUBS:
            total = random.randint(80, 300)
            late = random.randint(0, int(total * 0.3))
            avg_delay = round(random.uniform(0.0, 5.0), 2) if late > 0 else 0.0
            lines.append(
                f"{day},{hub},{REGIONS[hub]},{total},{late},{avg_delay}"
            )

    Path("data").mkdir(exist_ok=True)
    out = Path("data/shipment_delays.csv")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
