# SatellitePositions
## Task
Attached you will find a csv with the position of a satellite in the Geocentric Celestial Reference System (GCRS), given as Right Ascension (RA), Declination (Dec), and Distance, over the course of a day. We want you to provide us with a python script that can report/display the times when a ground station can observe the satellite. The ground station is located at a latitude of 78.7199 deg and longitude of 20.3493 deg, and can see a satellite when it is between 10-85deg above the horizon.

## Theory
My understanding is that I need to convert the GCRS coordinates of the Satellite into Alt/Az so that I can calculate whether the satellite is between 10-85 degrees above the horizon.

To do this I need to find the times when the altitude is between 10-85 degrees.

### Some resources that helped me!
1. [Launch Pad Astronomy - Local Sky & Alt/Az (Video)](https://www.youtube.com/watch?v=i2e0aRtwsCY)
2. [Nebula Photos - Where is it? Celestial Coordinates explained (Video)](https://www.youtube.com/watch?v=S0R8M7CQbVA)

## Repo Structure
I decided to follow a basic repo structure with a src folder containing my src functions, and a test class with tests for each function.

I stored the code_test_data.csv file in a data folder within the repo.

## Testing
To test my code I added basic unit tests for each method.
The most important method to test is the 'observe_satellite_position' method.
To do this I needed some test data where I could verify that the altitude returned was the correct value for the RA, Dec, Distance and ground_station values I had supplied.

Unfortunately I struggled to find reliable RA, Dec, Distance, Time and Ground station data online that I could use to valdiate my solution. This is something that I would go back to the team and ask if they could help me source.

Since I don't have complete validation data the test_observe_satellite_position() test is currently failing. I have added a TODO with some more information on this failing test.
Leaving this test as failing for now is better practice than adding an ignore attribute to exclude it from the report.

I would have liked to follow a TDD style approach for this, especially to verify that the altitude output by my code is correct but I didn't have the testing data available to get started with this initially.

## GitHub Actions
As an aside, I wanted to try using Pylint in GitHub Actions as I haven't used this CI/CD interface before.

I created a pylint task in .github/workflows/pylint.yml

This now runs on every push to main and outputs a score of the code quality.

This was just a bit of a Proof of Concept exercise but I thought it was interesting to include. If this was meant to be a production-ready solution I would fix the suggestions in pylint and continue to build up a GitHub Actions pipeline.

## Answer
My program prints 631 times where the satellite is visible to the console.

### Running the solution:
Clone and open the repository locally

```bash
    # Start a Virtual Environment
    python3 -m venv myenv

    # Navigate to the src folder and run the module
    cd ./src
    python -m positions_module
```

### Running the tests from the root of the repository:
```bash
    pytest
```
