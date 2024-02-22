import os
from src.positions_module import *

class Test():

    def test_load_satellite_positions(self):
        # Arrange
        data_folder = os.path.join(os.path.dirname(__file__), '../data')

        # Construct the file path
        file_path = os.path.join(data_folder, "code_test_data.csv")

        observer = SatelliteObserver(data_folder=data_folder, csv_file=file_path)

        #  Act
        positions = observer.load_satellite_positions()

        # Assert
        assert len(positions) == 1440

    def test_observe_satellite_position(self):
        # Arrange
        data_folder = './test_data'
        csv = 'testing_data.csv'
        gs_lattitude = 78.7199
        gs_longitude = 20.3493
        altitude_low = 34
        altitude_high = 40

        expected_result = ['1','2','3']

        observer = SatelliteObserver(data_folder, csv, gs_lattitude, gs_longitude, altitude_low, altitude_high)
        
        # Act
        output = observer.observe_satellite_position()

        # Assert
        assert output == expected_result
    
    def test_convert_time(self):
        # Arrange
        time_string = "2024-01-15 10:30:00"
        observer = SatelliteObserver()

        # Act
        result = observer.convert_time(time_string)

        # Assert
        assert isinstance(result, t.Time)

    def test_convert_distance(self):
        # Arrange
        distance = 2000
        observer = SatelliteObserver()

        # Act
        result = observer.convert_distance(distance)

        # Assert
        assert result == 2000000

    def test_create_ground_station_location(self):
        # Arrange
        observer = SatelliteObserver(ground_station_lat=40.7128, ground_station_lon=74.0060)

        # Act
        result = observer.create_ground_station_location()

        # Assert
        assert result.lat.deg == 40.7128
        assert result.lon.deg == 74.0060
        assert isinstance(result, EarthLocation)

    def test_is_altitude_within_range(self):
        # Arrange
        altitude_low = 10
        altitude_high = 85
        observer = SatelliteObserver(altitude_threshold_low=altitude_low, altitude_threshold_high=altitude_high)

        # Test positive scenario
        assert observer.is_altitude_within_range(50)
        assert observer.is_altitude_within_range(10.1)
        assert observer.is_altitude_within_range(84.9)

        # Test negative scenario
        assert not observer.is_altitude_within_range(5)
        assert not observer.is_altitude_within_range(10)
        assert not observer.is_altitude_within_range(85)
