import pytest
import os
from src.positions_module import *

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

    #  Arrange
    @pytest.mark.parametrize("ra, dec, observer, expected_altitude", [
        (1, 1, 1, 2),
        (2, 3, 2, 5),
        (5, 5, 6, 10),
        (-1, 1, 7, 0),
    ])  
    def test_convert_RA_Dec_To_Alt_Az_For_Observer(self, ra, dec, observer, expected_altitude):
        # Act
        calculated_altitude = convert_RA_Dec_To_Alt_Az_For_Observer(ra, dec, observer)

        # Assert
        assert calculated_altitude == expected_altitude
