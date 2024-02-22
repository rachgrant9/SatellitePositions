import os
import csv
from datetime import datetime
from astropy import units as u
from astropy import time as t
from astropy.coordinates import SkyCoord, AltAz, EarthLocation, ICRS

# Define constants
AU_IN_KM = 149597870.7  # 1 astronomical unit in kilometers
DATA_FOLDER = '../data'
CSV_FILE = 'code_test_data.csv'
GROUND_STATION_LAT = 78.7199
GROUND_STATION_LON = 20.3493
ALTITUDE_THRESHOLD_LOW = 10
ALTITUDE_THRESHOLD_HIGH = 85

def load_satellite_positions(csv_file):
    """Load satellite positions from a CSV file."""
    positions = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            positions.append({
                'time': convert_time(row['Time (iso)']),
                'RA': float(row['RA (GCRS) [deg]']),
                'Dec': float(row['Dec (GCRS) [deg]']),
                'Distance': convert_distance(float(row['Distance (GCRS) [km]']))
            })
    return positions

def convert_time(time):
    """Convert string time to Astropy Time object."""
    return t.Time.strptime(time, '%Y-%m-%d %H:%M:%S')

def convert_distance(distance):
    """Convert distance from kilometers to meters."""
    return distance * 1000

def create_ground_station_location(lat, lon):
    """Create EarthLocation for the ground station."""
    return EarthLocation(lat=lat, lon=lon)

def is_altitude_within_range(altitude, low_threshold, high_threshold):
    """Check if altitude is within the specified range."""
    return low_threshold < altitude < high_threshold

def main():
    file_path = os.path.join(os.path.dirname(__file__), DATA_FOLDER, CSV_FILE)
    positions = load_satellite_positions(file_path)
    ground_station = create_ground_station_location(GROUND_STATION_LAT, GROUND_STATION_LON)

    for position in positions:
        skycoord = SkyCoord(position['RA']*u.deg, position['Dec']*u.deg, distance=position['Distance'], frame=ICRS)
        satellite_altitude = skycoord.transform_to(AltAz(obstime=position['time'], location=ground_station))
        altitude_value = satellite_altitude.alt.deg

        if is_altitude_within_range(altitude_value, ALTITUDE_THRESHOLD_LOW, ALTITUDE_THRESHOLD_HIGH):
            print(f"Time: {position['time']}, Altitude: {altitude_value}")

if __name__ == "__main__":
    main()
