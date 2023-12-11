# Length conversion functions
def meters_to_feet(meters):
    return meters * 3.28084

def meters_to_inches(meters):
    return meters * 39.3701

def feet_to_meters(feet):
    return feet / 3.28084

def inches_to_meters(inches):
    return inches / 39.3701

# Area conversion functions
def square_meters_to_square_feet(square_meters):
    return square_meters * 10.7639

def square_feet_to_square_meters(square_feet):
    return square_feet / 10.7639

# Volume conversion functions
def cubic_meters_to_cubic_feet(cubic_meters):
    return cubic_meters * 35.3147

def cubic_feet_to_cubic_meters(cubic_feet):
    return cubic_feet / 35.3147

# Temperature conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0 / 5.0) + 32.0

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32.0) * 5.0 / 9.0

# Time conversion functions
def seconds_to_minutes(seconds):
    return seconds / 60.0

def minutes_to_seconds(minutes):
    return minutes * 60.0

def hours_to_minutes(hours):
    return hours * 60.0

def minutes_to_hours(minutes):
    return minutes / 60.0

# Speed conversion functions
def meters_per_second_to_kilometers_per_hour(meters_per_second):
    return meters_per_second * 3.6

def kilometers_per_hour_to_meters_per_second(kilometers_per_hour):
    return kilometers_per_hour / 3.6

# Pressure conversion functions
def pascals_to_atmospheres(pascals):
    return pascals * 9.86923e-6

def atmospheres_to_pascals(atmospheres):
    return atmospheres * 101325.0

# Energy conversion functions
def joules_to_calories(joules):
    return joules * 0.000239006

def calories_to_joules(calories):
    return calories * 4184.0

# Mass conversion functions
def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

# Force conversion functions
def newtons_to_pounds_force(newtons):
    return newtons * 0.224809

def pounds_force_to_newtons(pounds_force):
    return pounds_force / 0.224809

# Power conversion functions
def watts_to_horsepower(watts):
    return watts * 0.00134102

def horsepower_to_watts(horsepower):
    return horsepower / 0.00134102

# Digital storage conversion functions
def bytes_to_kilobytes(bytes):
    return bytes / 1024

def kilobytes_to_bytes(kilobytes):
    return kilobytes * 1024

def bytes_to_megabytes(bytes):
    return bytes / (1024 * 1024)

def megabytes_to_bytes(megabytes):
    return megabytes * (1024 * 1024)
