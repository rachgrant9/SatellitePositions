import pytest
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
