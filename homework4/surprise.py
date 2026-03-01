# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

#1 
def target_names(lst) : 
    for key in lst : 
        print(key)
(target_names(targets))

#2 
def target_name_spectral_type(lst) : 
    for name in lst : 
        for key in lst[name] : 
            if key == "Spectral Type" :
                print(f"{name}, {lst[name][key]}")
target_name_spectral_type(targets)

#3 
def min_magnitude(lst) : 
    for name in lst :
        if "Magnitude" in lst[name] : 
            if lst[name]["Magnitude"] > 0.1 :
                print(name)
min_magnitude(targets)

#4 
# New Target: Alpha Centauri A
# Dec: -60° 50' 02"
# RA: 14h 39m 36.5s 
# Magnitude: -0.01 
# Spectral Type: G2V

targets["Alpha Centauri A"] = {
        "RA": "14h 39m 36.5s", 
        "Dec": "-60° 50′ 02″",
        "Magnitude": -0.01,
        "Spectral Type": "G2V"
        }
print(targets)

#5 

# to find the brightest star we must look at the magnitude 
# lower magnitude ---> brighter star 
# classify stars closed to 20 degrees
# use star declination - 20 degrees

import math

def convert_dec_to_decimal(str) : 
    clean = str.replace("°", "").replace("′", "").replace("″", "")
    clean = clean = clean.replace("−", "-").replace(":", " ")
    parts = clean.split()

    degrees = float(parts[0])
    minutes = float(parts[1])
    seconds = float(parts[2])

    if degrees < 0 :
        sign = -1 
    else : sign = 1 

    decimal = abs(degrees) + minutes/60 + seconds/3600
    
    return sign * decimal


def find_brightest_star(lst) : 
    possible_stars = [] 
    x = 0 # distance of declination from 20 degrees
    decimal = 0

    for star in lst : 
        if "Dec" in lst[star] : 
            decimal = convert_dec_to_decimal(lst[star]["Dec"])
            x = abs(decimal - 20)
            if x < 20 : 
                possible_stars.append(star)

    brightest_star_name = None 
    brightest_star_value = float('inf')  # we want the smallest float 

    for star in possible_stars : 
        if "Magnitude" in lst[star] : 
            if int(lst[star]["Magnitude"]) < brightest_star_value : 
                brightest_star_name = star
                brightest_star_value = lst[star]["Magnitude"]

    return f" The brighest star is {brightest_star_name} with a magnitude, {brightest_star_value}"

print(find_brightest_star(targets))
        

            
        



