# SatellitePositions

## Task
Attached you will find a csv with the position of a satellite in the Geocentric Celestial Reference System (GCRS), given as Right Ascension (RA), Declination (Dec), and Distance, over the course of a day. We want you to provide us with a python script that can report/display the times when a ground station can observe the satellite. The ground station is located at a latitude of 78.7199 deg and longitude of 20.3493 deg, and can see a satellite when it is between 10-85deg above the horizon. 

## Theory
My understanding is that I need to convert the GCRS coordinates of the Satellite into Alt/Az so that I can calculate whether the satellite is between 10-85 degrees above the horizon.

To do this I need to find the times when the altitude is between 10-85 degrees.

### Some resources that helped me!
1. [Launch Pad Astronomy - Local Sky & Alt/Az (Video)](https://www.youtube.com/watch?v=i2e0aRtwsCY)
2. [Nebula Photos - Where is it? Celestial Coordinates explained (Video)](https://www.youtube.com/watch?v=S0R8M7CQbVA)

The astronomy side was new to me so I went looking for a python package that would be able to help me perform these calculations. 

I came across the python package Skyfield and decided to use it as it seemed to fit in well with the co-ordinates I have been supplied with.

If there was potential for the scope of the project to change to require other types of calculations it would be better to assess the different available tools for astronomy.

## Assumptions
I have assumed that 'between 10-85deg above the horizon' did not include 10 and 85 as altitudes where the satellite would be visible. This is a requirement that I would ask for clarification on in normal circumstances.

## Repo Structure
I decided to follow a basic repo structure with a src folder containing my src functions, and a test class with tests for each function.
I stored the code_test_data.csv file in a data folder within the repo. 

## Improvements that should be made to the code

### SOLID Principles

### Testing

### Deployment
