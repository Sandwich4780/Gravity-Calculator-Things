import math

# NOTE: this isn't the most accurate but it works fairly well (try calculating the moon's speed)
print("Calculates the minimum velocity for a satellite to orbit Earth")

height = float(input("Orbit height from Earth's surface [KM]: "))

earthMass = 5.97e24  # [kgs] same as 5.97 * 10^24
earthRadius = 6371  # [km]

totalRadius = (earthRadius + height) * 1000  # [m]

gravConst = 6.67430e-11  # [n] same as 6.67430 * 10^-11

velocity = round(math.sqrt(gravConst * earthMass / totalRadius)) / 1000  # in km/s
print("Minimum velocity: " + str(velocity) + " KM/s")
