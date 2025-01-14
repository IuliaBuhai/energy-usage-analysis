import pandas as pd

def compute_statistics(df):
    # Descriptive statistics
    statistics = df.describe()
    return statistics

def compute_avg_kwh_per_community(df):
    # Group data by 'COMMUNITY AREA NAME' and compute average 'TOTAL KWH'
    avg_kwh_per_community = df.groupby("COMMUNITY AREA NAME")['TOTAL KWH'].mean().sort_values(ascending=False)
    return avg_kwh_per_community
