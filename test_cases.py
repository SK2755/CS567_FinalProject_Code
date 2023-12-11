from units import *

import unittest

# Test Length Conversions
class TestLengthConversions(unittest.TestCase):
    def test_meters_to_feet(self):
        self.assertAlmostEqual(meters_to_feet(1), 3.28084)

    def test_meters_to_inches(self):
        self.assertAlmostEqual(meters_to_inches(1), 39.3701)

    def test_feet_to_meters(self):
        self.assertAlmostEqual(feet_to_meters(3.28084), 1)

    def test_inches_to_meters(self):
        self.assertAlmostEqual(inches_to_meters(39.3701), 1)

# Test Area Conversions
class TestAreaConversions(unittest.TestCase):
    def test_square_meters_to_square_feet(self):
        self.assertAlmostEqual(square_meters_to_square_feet(1), 10.7639)

    def test_square_feet_to_square_meters(self):
        self.assertAlmostEqual(square_feet_to_square_meters(10.7639), 1)

# Test Volume Conversions
class TestVolumeConversions(unittest.TestCase):
    def test_cubic_meters_to_cubic_feet(self):
        self.assertAlmostEqual(cubic_meters_to_cubic_feet(1), 35.3147)

    def test_cubic_feet_to_cubic_meters(self):
        self.assertAlmostEqual(cubic_feet_to_cubic_meters(35.3147), 1)

# Test Temperature Conversions
class TestTemperatureConversions(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)

# Test Time Conversions
class TestTimeConversions(unittest.TestCase):
    def test_seconds_to_minutes(self):
        self.assertAlmostEqual(seconds_to_minutes(60), 1)

    def test_minutes_to_seconds(self):
        self.assertAlmostEqual(minutes_to_seconds(1), 60)

    def test_hours_to_minutes(self):
        self.assertAlmostEqual(hours_to_minutes(1), 60)

    def test_minutes_to_hours(self):
        self.assertAlmostEqual(minutes_to_hours(60), 1)

# Test Speed Conversions
class TestSpeedConversions(unittest.TestCase):
    def test_meters_per_second_to_kilometers_per_hour(self):
        self.assertAlmostEqual(meters_per_second_to_kilometers_per_hour(1), 3.6)

    def test_kilometers_per_hour_to_meters_per_second(self):
        self.assertAlmostEqual(kilometers_per_hour_to_meters_per_second(3.6), 1)


class TestEnergyConversions(unittest.TestCase):
    def test_joules_to_calories(self):
        self.assertAlmostEqual(joules_to_calories(4184), 1, places=5)

class TestPressureConversions(unittest.TestCase):
    def test_pascals_to_atmospheres(self):
        self.assertAlmostEqual(pascals_to_atmospheres(101325), 1, places=6)

# Test Mass Conversions
class TestMassConversions(unittest.TestCase):
    def test_kilograms_to_pounds(self):
        self.assertAlmostEqual(kilograms_to_pounds(1), 2.20462)

    def test_pounds_to_kilograms(self):
        self.assertAlmostEqual(pounds_to_kilograms(2.20462), 1)

# Test Force Conversions
class TestForceConversions(unittest.TestCase):
    def test_newtons_to_pounds_force(self):
        self.assertAlmostEqual(newtons_to_pounds_force(1), 0.224809)

    def test_pounds_force_to_newtons(self):
        self.assertAlmostEqual(pounds_force_to_newtons(0.224809), 1)

# Test Power Conversions
class TestPowerConversions(unittest.TestCase):
    def test_horsepower_to_watts(self):
        self.assertAlmostEqual(horsepower_to_watts(1), 746, places=4)

    def test_watts_to_horsepower(self):
        self.assertAlmostEqual(watts_to_horsepower(746), 1, places=4)

# Test Digital Storage Conversions
class TestDigitalStorageConversions(unittest.TestCase):
    def test_bytes_to_kilobytes(self):
        self.assertAlmostEqual(bytes_to_kilobytes(1024), 1)

    def test_kilobytes_to_bytes(self):
        self.assertAlmostEqual(kilobytes_to_bytes(1), 1024)

    def test_bytes_to_megabytes(self):
        self.assertAlmostEqual(bytes_to_megabytes(1024 * 1024), 1)

    def test_megabytes_to_bytes(self):
        self.assertAlmostEqual(megabytes_to_bytes(1), 1024 * 1024)

# Main block to run the tests
if __name__ == '__main__':
    unittest.main()
