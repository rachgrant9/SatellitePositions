import os
import csv
from datetime import datetime

# Function to load satellite positions from CSV
def load_satellite_positions(csv_file):
    positions = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            positions.append({
                'time': datetime.strptime(row['Time (iso)'], '%Y-%m-%d %H:%M:%S'),
                'RA': float(row['RA (GCRS) [deg]']),
                'Dec': float(row['Dec (GCRS) [deg]']),
                'Distance': float(row['Distance (GCRS) [km]'])
            })
    return positions