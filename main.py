import math

print("Modes: Orbit speed [1], Escape velocity [2]")
mode = int(input("Enter desired mode: "))

gravConst = 6.67430e-11  # [n] same as 6.67430 * 10^-11

if mode == 1:  # orbit speed
    # NOTE: this isn't the most accurate but it works fairly well (try calculating the moon's speed)
    height = float(input("Orbit height from Earth's surface [KM]: "))

    earthMass = 5.97e24  # [kgs] same as 5.97 * 10^24
    earthRadius = 6371  # [km]

    totalRadius = (earthRadius + height) * 1000  # [m]

    velocity = round(math.sqrt(gravConst * earthMass / totalRadius)) / 1000  # in km/s
    print("Minimum velocity: " + str(velocity) + " KM/s")

elif mode == 2:  # escape velocity
    massMultiplier = float(input("Mass multipler (based on Earth's mass): "))
    planetRadius = float(input("Planet Radius [KM]: "))

    planetMass = 5.97e24 * massMultiplier
    escapeVelocity = round(math.sqrt(2 * gravConst * planetMass / (planetRadius * 1000))) / 1000  # converts to KM/s
    print("Escape velocity: " + str(escapeVelocity) + " KM/s")

else:
    print("Invalid!!!!!!!!!!")
