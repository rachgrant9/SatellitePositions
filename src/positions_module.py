import os
import csv
from astropy import units as u
from astropy import time as t
from astropy.coordinates import SkyCoord, AltAz, EarthLocation, ICRS
DATA_FOLDER = '../data'
CSV_FILE = 'code_test_data.csv'
GROUND_STATION_LAT = 78.7199
GROUND_STATION_LON = 20.3493
ALTITUDE_THRESHOLD_LOW = 10
ALTITUDE_THRESHOLD_HIGH = 85

class SatelliteObserver:
    """Class constructor has default constants for execution but can be overridden for testing """
    def __init__(self, data_folder=DATA_FOLDER, csv_file=CSV_FILE, ground_station_lat=GROUND_STATION_LAT, ground_station_lon=GROUND_STATION_LON, altitude_threshold_low=ALTITUDE_THRESHOLD_LOW, altitude_threshold_high=ALTITUDE_THRESHOLD_HIGH):
        self.data_folder = data_folder
        self.csv_file = csv_file
        self.ground_station_lat = ground_station_lat
        self.ground_station_lon = ground_station_lon
        self.altitude_threshold_low = altitude_threshold_low
        self.altitude_threshold_high = altitude_threshold_high

    def load_satellite_positions(self):
        """Load satellite positions from a CSV file."""
        file_path = os.path.join(self.data_folder, self.csv_file)
        positions = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                positions.append({
                    'time': self.convert_time(row['Time (iso)']),
                    'RA': float(row['RA (GCRS) [deg]']),
                    'Dec': float(row['Dec (GCRS) [deg]']),
                    'Distance': self.convert_distance(float(row['Distance (GCRS) [km]']))
                })
        return positions

    def convert_time(self, time):
        """Convert string time to Astropy Time object."""
        return t.Time.strptime(time, '%Y-%m-%d %H:%M:%S')

    def convert_distance(self, distance):
        """Convert distance from kilometers to meters."""
        return distance * 1000

    def create_ground_station_location(self):
        """Create EarthLocation for the ground station."""
        return EarthLocation(lat=self.ground_station_lat, lon=self.ground_station_lon)

    def is_altitude_within_range(self, altitude):
        """Check if altitude is within the specified range."""
        return self.altitude_threshold_low < altitude < self.altitude_threshold_high

    def get_altitude_value(self, position, ground_station):
        """Get the altitude value for a given satellite position."""
        skycoord = self.create_skycoord(position)
        satellite_altitude = self.transform_to_altaz(skycoord, position['time'], ground_station)
        return satellite_altitude.alt.deg

    def create_skycoord(self, position):
        """Create SkyCoord object from satellite position."""
        return SkyCoord(position['RA']*u.deg, position['Dec']*u.deg, distance=position['Distance'], frame=ICRS)

    def transform_to_altaz(self, skycoord, time, ground_station):
        """Transform SkyCoord object to AltAz coordinates."""
        return skycoord.transform_to(AltAz(obstime=time, location=ground_station))

    def observe_satellite_position(self):
        """Main method to observe satellite position"""
        observations = []
        positions = self.load_satellite_positions()
        ground_station = self.create_ground_station_location()

        for position in positions:
            altitude_value = self.get_altitude_value(position, ground_station)
            if self.is_altitude_within_range(altitude_value):
                observations.append({"time": position['time'], "altitude": altitude_value})
        
        return observations
