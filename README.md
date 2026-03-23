# F1 Telemetry Analysis

Analyzing Formula 1 race data using the FastF1 Python library.

## What this project does
Loads the 2024 Monza race session and extracts Leclerc's fastest lap telemetry.
Prints lap time, tyre compound, sector splits, and plots a speed trace across the circuit.

## Key findings
- Fastest lap: 1:23.226 on Hard tyres (18 laps old)
- Top speed: 341 km/h
- Sector splits: 27.1s | 28.3s | 27.6s

## How to run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create the cache folder: `mkdir f1_cache`
4. Run: `python monza_analysis.py`

## Data source
Official F1 timing data via [FastF1](https://theoehrly.github.io/Fast-F1/)
