# FastF1 Basics — Monza 2024 Race
import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt

# --- STEP 1: Enable cache ---
# Saves downloaded data locally so you don't re-download every run
fastf1.Cache.enable_cache('f1_cache')

# --- STEP 2: Load a session ---
# Arguments: year, event name, session type
# Session types: 'FP1' 'FP2' 'FP3' 'Q' 'R'
session = fastf1.get_session(2024, 'Monza', 'R')
session.load()

# --- STEP 3: Explore lap data ---
# session.laps is a table (DataFrame) with one row per lap
all_laps = session.laps
print("Total laps in this race:", len(all_laps))
print("\nColumn names:")
print(all_laps.columns.tolist())

# --- STEP 4: Filter to one driver ---
lec_laps = session.laps.pick_driver('LEC')
print("\nLeclerc's lap count:", len(lec_laps))
print("\nHis lap times:")
print(lec_laps[['LapNumber', 'LapTime', 'Compound', 'TyreLife']].to_string())

# --- STEP 5: Get his fastest lap ---
fastest = lec_laps.pick_fastest()
print("\nFastest lap time:", fastest['LapTime'])
print("Tyre compound:", fastest['Compound'])
print("Tyre age at that lap:", fastest['TyreLife'], "laps")
print("Sectors:", fastest['Sector1Time'], "|", fastest['Sector2Time'], "|", fastest['Sector3Time'])

# --- STEP 6: Load telemetry for that lap ---
# Telemetry = car sensor data sampled many times per second
# Columns: Speed, Throttle, Brake, RPM, nGear, DRS, Distance
tel = fastest.get_telemetry()
print("\nTelemetry shape:", tel.shape)  # (rows, columns)
print("Max speed:", round(tel['Speed'].max(), 1), "km/h")
print("Min speed:", round(tel['Speed'].min(), 1), "km/h")

# --- STEP 7: Plot the speed trace ---
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(tel['Distance'], tel['Speed'], color='#E01B1B', linewidth=1.5)
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Speed (km/h)')
ax.set_title('Leclerc — Fastest Lap Speed Trace, Monza 2024')
plt.tight_layout()
plt.savefig('speed_trace.png', dpi=150)
plt.show()
print("\nPlot saved as speed_trace.png")