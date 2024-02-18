import pandas as pd
import matplotlib.pyplot as plt
from ipyleaflet import Map, basemaps, CircleMarker

ds = pd.read_csv("./assets/real_estate.csv", delimiter=';')

south_belt_populations = ["Fuenlabrada", "Leganés", "Getafe", "Alcorcón"]
south_belt_subset = ds[ds['level5'].isin(south_belt_populations)]


# Create a map centered on the first coordinate in the south_belt_subset
first_lat, first_lon = south_belt_subset.iloc[0]['latitude'], south_belt_subset.iloc[0]['longitude']
madrid_map = Map(center=(first_lat, first_lon), zoom=10)

# Define colors for each population
population_colors = {
    "Fuenlabrada": "blue",
    "Leganés": "green",
    "Getafe": "red",
    "Alcorcón": "orange"
}

# Plot coordinates of each population on the map
for population, color in population_colors.items():
    population_data = south_belt_subset[south_belt_subset['level5'] == population]
    for _, row in population_data.iterrows():
        latitude, longitude = row['latitude'], row['longitude']
        marker = CircleMarker(location=(latitude, longitude), color=color, radius=5)
        madrid_map.add_layer(marker)
madrid_map.save('map.png')
madrid_map