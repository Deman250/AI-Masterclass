#Project data analysis report
print( "\n === LOAD AND INSPECT DATA ====")

import pandas as pd
import numpy as np

# 28 days of SMP fitness log
data = {
    "day":      list(range(1, 29)),
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200,
                 8900, 10800, 9100, 11200, 7900, 10000, 9700,
                 9500, 10300, 8600, 11500, 8200, 9800, 10600,
                 9000, 10100, 8400, 10900, 7500, 9600, 10400],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0,
                 6.0, 8.5, 7.0, 7.5, 9.0, 7.0, 7.5,
                 7.0, 8.0, 6.5, 7.5, 8.0, 7.0, 8.5,
                 7.0, 7.5, 6.5, 8.0, 9.5, 7.0, 8.0],
    "water":    [7, 8, 6, 9, 8, 7, 8, 6, 9, 8, 8, 7, 9, 8,
                 7, 8, 6, 9, 8, 7, 9, 8, 8, 6, 9, 7, 8, 9],
    "protocol": (["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"] * 4),
    "cold_shower": ([True, True, False, True, True, True, True,
                     False, True, True, True, True, False, True] * 2),
    "bench_kg": [80, 82, 78, 85, 80, 83, 84,
                 81, 85, 80, 86, 79, 84, 83,
                 82, 86, 79, 88, 81, 85, 87,
                 82, 86, 80, 87, 79, 84, 86],
}
df = pd.DataFrame(data)

print(f"Shape: {df.shape}")
print(f"\nColumns: {list(df.columns)}")
print(f"\nData types:")
print(df.dtypes)
print(f"\nMissing values: {df.isna().sum().sum()}")
print(f"\nFirst 3 rows:")
print(df.head(3).to_string())
#Step 2:Filter and analyse
#High performance days
print("\n ==== STEP 2:FILTER AND ANALYSE DATA ====")
print("\n ==== HIGH PERFOMANCE DAYS ===")
import pandas as pd
import numpy as np

data = {
    "day":      list(range(1, 29)),
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200, 8900, 10800, 9100, 11200, 7900, 10000, 9700, 9500, 10300, 8600, 11500, 8200, 9800, 10600, 9000, 10100, 8400, 10900, 7500, 9600, 10400],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0, 6.0, 8.5, 7.0, 7.5, 9.0, 7.0, 7.5, 7.0, 8.0, 6.5, 7.5, 8.0, 7.0, 8.5, 7.0, 7.5, 6.5, 8.0, 9.5, 7.0, 8.0],
    "water":    [7, 8, 6, 9, 8, 7, 8, 6, 9, 8, 8, 7, 9, 8, 7, 8, 6, 9, 8, 7, 9, 8, 8, 6, 9, 7, 8, 9],
    "protocol": (["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"] * 4),
    "bench_kg": [80, 82, 78, 85, 80, 83, 84, 81, 85, 80, 86, 79, 84, 83, 82, 86, 79, 88, 81, 85, 87, 82, 86, 80, 87, 79, 84, 86],
}
df = pd.DataFrame(data)

# High-performance days: 10k+ steps AND 7.5+ hours sleep
high_perf = df[(df["steps"] >= 10000) & (df["sleep_hr"] >= 7.5)]
print(f"High-performance days: {len(high_perf)}/28")

# Protocol comparison
print("\nMetrics by fasting protocol:")
protocol_stats = df.groupby("protocol").agg(
    avg_steps=("steps", "mean"),
    avg_sleep=("sleep_hr", "mean"),
    avg_bench=("bench_kg", "mean"),
    avg_water=("water", "mean"),
    days=("day", "count")
).round(1)
print(protocol_stats)
#Numpy analysis
print("\n ==== STEP 3: NUMPY ANALYSIS ====")
import pandas as pd
import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200, 8900, 10800, 9100, 11200, 7900, 10000, 9700, 9500, 10300, 8600, 11500, 8200, 9800, 10600, 9000, 10100, 8400, 10900, 7500, 9600, 10400])
bench = np.array([80, 82, 78, 85, 80, 83, 84, 81, 85, 80, 86, 79, 84, 83, 82, 86, 79, 88, 81, 85, 87, 82, 86, 80, 87, 79, 84, 86])
sleep = np.array([7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0, 6.0, 8.5, 7.0, 7.5, 9.0, 7.0, 7.5, 7.0, 8.0, 6.5, 7.5, 8.0, 7.0, 8.5, 7.0, 7.5, 6.5, 8.0, 9.5, 7.0, 8.0])

print("=== 28-Day NumPy Analysis ===")
print(f"\nSteps:")
print(f"  Mean:        {np.mean(steps):,.0f}")
print(f"  Std dev:     {np.std(steps):,.0f}")
print(f"  25th pctile: {np.percentile(steps, 25):,.0f}")
print(f"  75th pctile: {np.percentile(steps, 75):,.0f}")
print(f"  Days 10k+:   {np.sum(steps >= 10000)}/28")

print(f"\nBench Press:")
print(f"  Mean:        {np.mean(bench):.1f} kg")
print(f"  Max:         {np.max(bench)} kg  (Day {np.argmax(bench)+1})")
print(f"  Trend:       {'increasing' if bench[-7:].mean() > bench[:7].mean() else 'flat/decreasing'}")

# Correlation: do more steps correlate with better bench?
corr = np.corrcoef(steps, bench)[0, 1]
print(f"\nCorrelation steps vs bench: {corr:.3f}")
print("Interpretation:", "positive relationship" if corr > 0.3 else "weak/no relationship")
#Full report
print("\n ==== FULL REPORT ====")
import pandas as pd
import numpy as np

# Data
steps_list = [9200, 10500, 8800, 11000, 7600, 9400, 10200, 8900, 10800, 9100, 11200, 7900, 10000, 9700, 9500, 10300, 8600, 11500, 8200, 9800, 10600, 9000, 10100, 8400, 10900, 7500, 9600, 10400]
sleep_list = [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0, 6.0, 8.5, 7.0, 7.5, 9.0, 7.0, 7.5, 7.0, 8.0, 6.5, 7.5, 8.0, 7.0, 8.5, 7.0, 7.5, 6.5, 8.0, 9.5, 7.0, 8.0]
bench_list = [80, 82, 78, 85, 80, 83, 84, 81, 85, 80, 86, 79, 84, 83, 82, 86, 79, 88, 81, 85, 87, 82, 86, 80, 87, 79, 84, 86]
proto_list = (["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"] * 4)
water_list = [7, 8, 6, 9, 8, 7, 8, 6, 9, 8, 8, 7, 9, 8, 7, 8, 6, 9, 8, 7, 9, 8, 8, 6, 9, 7, 8, 9]

df = pd.DataFrame({
    "day": list(range(1, 29)),
    "steps": steps_list, "sleep_hr": sleep_list,
    "bench_kg": bench_list, "protocol": proto_list, "water": water_list
})

steps = np.array(steps_list)
bench = np.array(bench_list)

W = 54
print("=" * W)
print("  SMP 28-DAY FITNESS ANALYSIS REPORT")
print("=" * W)

# Overall stats
print(f"\n  OVERALL METRICS")
print(f"  {'Days tracked:':<25} 28")
print(f"  {'Total steps:':<25} {steps.sum():,}")
print(f"  {'Avg daily steps:':<25} {steps.mean():,.0f}")
print(f"  {'Days hitting 10k:':<25} {(steps >= 10000).sum()}/28  ({(steps >= 10000).mean()*100:.0f}%)")
print(f"  {'Avg sleep:':<25} {np.mean(sleep_list):.1f} hrs")
print(f"  {'Bench press range:':<25} {bench.min()} to {bench.max()} kg")
print(f"  {'Bench press trend:':<25} +{bench[-7:].mean() - bench[:7].mean():.1f} kg (wk1 to wk4)")

# Week-by-week
print(f"\n  WEEKLY BREAKDOWN")
print(f"  {'Week':<8} {'Avg Steps':>12}  {'10k Days':>8}  {'Avg Bench':>10}")
print(f"  {'-'*44}")
for wk in range(4):
    s = steps[wk*7:(wk+1)*7]
    b = bench[wk*7:(wk+1)*7]
    hits = (s >= 10000).sum()
    print(f"  Week {wk+1:<3} {s.mean():>12,.0f}  {hits:>8}/7  {b.mean():>9.1f} kg")

# Protocol breakdown
print(f"\n  PROTOCOL COMPARISON")
proto_stats = df.groupby("protocol")[["steps", "sleep_hr", "bench_kg"]].mean().round(1)
for proto, row in proto_stats.iterrows():
    print(f"  {proto}: avg steps={row['steps']:,.0f}, sleep={row['sleep_hr']}h, bench={row['bench_kg']}kg")

# Top days
top3 = df.nlargest(3, "steps")
print(f"\n  TOP 3 STEP DAYS")
for _, row in top3.iterrows():
    print(f"  Day {int(row['day']):2d}: {int(row['steps']):,} steps  ({row['protocol']})")

print(f"\n{'=' * W}")