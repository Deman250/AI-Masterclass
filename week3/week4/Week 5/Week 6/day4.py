#Introduction to Numpy
#Creating Numpy array
import numpy as np

# From a Python list
steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
print("steps array:", steps)
print("type:", type(steps))
print("dtype:", steps.dtype)
print("shape:", steps.shape)

# Zeros and ones
print("\nnp.zeros(6):", np.zeros(6))
print("np.ones(5):", np.ones(5))

# Range of numbers
print("np.arange(1, 8):", np.arange(1, 8))

# Evenly spaced
print("np.linspace(0, 1, 5):", np.linspace(0, 1, 5))

#vectorized operations
print("\n === VECTORIZED OPERATIONS ===")
import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
goal  = 10000

# All at once, no loop needed
deficit = steps - goal
print("Steps vs 10k goal:", deficit)

# Percentage of goal achieved
pct = (steps / goal * 100).round(1)
print("Percent of goal:", pct)

# Boolean mask: which days hit the goal?
hit = steps >= goal
print("Hit goal:", hit)
print("Days hitting goal:", steps[hit])
#Statistical Analysis
print("\n ==== STATISTICAL ANALYSIS ===")
import numpy as np

# 4 weeks of daily steps (28 days)
steps_28 = np.array([
    9200, 10500, 8800, 11000, 7600, 9400, 10200,
    8900, 10800, 9100, 11200, 7900, 10000, 9700,
    9500, 10300, 8600, 11500, 8200, 9800, 10600,
    9000, 10100, 8400, 10900, 7500, 9600, 10400
])

print(f"28-day step analysis")
print(f"  Mean:        {np.mean(steps_28):,.0f}")
print(f"  Median:      {np.median(steps_28):,.0f}")
print(f"  Std dev:     {np.std(steps_28):,.0f}")
print(f"  Min:         {np.min(steps_28):,}")
print(f"  Max:         {np.max(steps_28):,}")
print(f"  Total:       {np.sum(steps_28):,}")
print(f"  75th pctile: {np.percentile(steps_28, 75):,.0f}")
print(f"  Days 10k+:   {np.sum(steps_28 >= 10000)}/28")

#Array slicing
print("\n ==== SLICE AND INDEX ARRAYS ===")
import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("First 3 days:", steps[:3])
print("Last 2 days:", steps[-2:])
print("Weekdays (Mon-Fri):", steps[:5])
print("Weekend:", steps[5:])

print()
# Best week start: first day above 10k
first_10k = np.argmax(steps >= 10000)   # index of first True
print(f"First 10k+ day: {days[first_10k]} with {steps[first_10k]:,} steps")

# Sort and show progression
sorted_steps = np.sort(steps)
print("Steps sorted low to high:", sorted_steps)

#Numpy and pandas together
print("\n === WORKING WITH NUMPY AND PANDAS ===")
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "bench_press_kg":[80, 82, 78, 85, 80, 83, 84],
})

# Pull a column as a NumPy array
steps_arr = df["steps"].to_numpy()
print("NumPy array from pandas column:", steps_arr)
print("Type:", type(steps_arr))


# Use NumPy on it
correlation = np.corrcoef(steps_arr, df["bench_press_kg"].to_numpy())
print(f"\nMean:    {np.mean(steps_arr):,.0f}")
print(f"Std dev: {np.std(steps_arr):,.0f}")
print(f"Correlation : {correlation}")
# Add a normalized column back to the DataFrame
# Normalize to 0-1 range (min-max scaling)
df["steps_norm"] = (df["steps"] - df["steps"].min()) / (df["steps"].max() - df["steps"].min())
df["steps_norm"] = df["steps_norm"].round(3)
print("\nWith normalized steps:")
print(df[["day", "steps", "steps_norm"]].to_string())
#Numpy on farm data: Maize yield analysis
print("\n ==== MAIZE YIELD ANALYSIS ====")
import numpy as np

# Maize yield (90kg bags) per plot over a single season
yields = np.array([18, 22, 15, 31, 27, 19, 24, 12, 28, 21, 17, 25])
rainfall_mm = np.array([420, 510, 380, 620, 590, 440, 530, 310, 610, 490, 400, 560])

print("MAIZE YIELD ANALYSIS (90kg bags per plot)")
print(f"  Plots:        {len(yields)}")
print(f"  Total yield:  {np.sum(yields)} bags ({np.sum(yields) * 90:,} kg)")
print(f"  Mean:         {np.mean(yields):.1f} bags/plot")
print(f"  Median:       {np.median(yields):.1f} bags/plot")
print(f"  Std dev:      {np.std(yields):.1f}")
print(f"  Best plot:    {np.max(yields)} bags")
print(f"  Worst plot:   {np.min(yields)} bags")
print(f"  Top 25% (75th pctile): {np.percentile(yields, 75):.0f} bags")

print()
# Revenue at KES 2,800 per 90kg bag
revenue = yields * 2800
print("REVENUE (KES 2,800 per bag)")
print(f"  Total:        KES {np.sum(revenue):,}")
print(f"  Avg/plot:     KES {np.mean(revenue):,.0f}")

print()
# Correlation between rainfall and yield
corr = np.corrcoef(rainfall_mm, yields)[0, 1]
print(f"Rainfall vs yield correlation: {corr:.2f}")
print("(1.0 = perfect positive link, 0 = no link)")

print()
#Plots above mean
mean_yield = np.mean(yields)
best_plots = yields[yields > mean_yield]
print(f"plots above mean: {best_plots}")

print()
#Calculate average rainfall for best performing plots
best_plot_mask = yields > mean_yield
avg_rainfall_for_best_plots = np.mean(rainfall_mm[best_plot_mask])
print(f"Average rainfall for plots above mean: {avg_rainfall_for_best_plots:.1f} mm")
worst_plot_mask = yields < mean_yield
avg_rainfall_for_worst_plots = np.mean(rainfall_mm[worst_plot_mask])
print(f"Comparison: best plots average {avg_rainfall_for_best_plots:.1f} mm vs worst plots average {avg_rainfall_for_worst_plots:.1f} mm")

