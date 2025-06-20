import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display
import streamlit as st

# Load the data
df = pd.read_csv('owid-covid-data.csv')
print(df.columns)  # Check actual columns
df.columns = df.columns.str.strip()  # Remove any leading/trailing spaces

# Ensure 'location' column exists
if 'location' not in df.columns:
    print("Error: 'location' column not found in the data. Please check the CSV file or re-download it using:\n"
          "curl -L -o owid-covid-data.csv https://covid.ourworldindata.org/data/owid-covid-data.csv")
    import sys
    sys.exit(1)

# Preview first few rows
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Filter for countries of interest
countries = ['Kenya', 'United States', 'India']
df_countries = df[df['location'].isin(countries)]

# Drop rows with missing critical values
print('Columns before dropna:', df_countries.columns)
drop_cols = ['date', 'total_cases', 'total_deaths']
df_countries = df_countries.dropna(subset=drop_cols)  # type: ignore

# Convert date column to datetime
df_countries['date'] = pd.to_datetime(df_countries['date'])

# Fill missing numeric values with interpolation
df_countries = df_countries.interpolate()

# Plot total cases over time
plt.figure(figsize=(12,6))
for country in countries:
    subset = df_countries[df_countries['location'] == country]
    plt.plot(subset['date'], subset['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.show()

# Calculate death rate
df_countries['death_rate'] = df_countries['total_deaths'] / df_countries['total_cases']

# Plot death rate
plt.figure(figsize=(12,6))
for country in countries:
    subset = df_countries[df_countries['location'] == country]
    plt.plot(subset['date'], subset['death_rate'], label=country)
plt.title('COVID-19 Death Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.legend()
plt.show()

print(df_countries.columns)

country_widget = widgets.Dropdown(options=df['location'].unique(), description='Country:')
display(country_widget)

country = st.selectbox('Select country', df['location'].unique())
subset = df[df['location'] == country]
st.line_chart(subset.set_index('date')['total_cases'])
