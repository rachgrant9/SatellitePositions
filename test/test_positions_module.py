import pytest
import os
from src.positions_module import load_satellite_positions

class Test():

    def test_load_satellite_positions(self):
        # Arrange
        data_folder = os.path.join(os.path.dirname(__file__), '../data')

        # Construct the file path
        file_path = os.path.join(data_folder, "code_test_data.csv")

        #  Act
        positions = load_satellite_positions(file_path)

        # Assert
        assert len(positions) == 1440
