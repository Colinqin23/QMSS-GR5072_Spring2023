# set working directory
import os
path = r'C:\Users\nicka\OneDrive\Desktop\1 Modern Data Structures - GR5072\QMSS-GR5072_Spring2023\Week 7\Class Activity'
os.chdir(path)
os.getcwd()

# Import rocket and shuttle class
from Rocket_and_shuttle_classes import Rocket
from Rocket_and_shuttle_classes import Shuttle



#======== Q2. =========

# Initalize rocket at (0, 0)
rocket_0 = Rocket()
rocket_0.x
rocket_0.y

# Initalize rocket at (10, 5)
rocket_1 = Rocket(10,5)
rocket_1.x
rocket_1.y

# Move rocket_1 to (3, 4)
rocket_1.move_rocket(-7, -1)
rocket_1.x
rocket_1.y

# Show the distance between the two rockets
distance = rocket_0.get_distance(rocket_1)
print("The rockets are {} units apart.".format(distance))


#======== Q3. =========

#Create a shuttle
shuttle = Shuttle(10,0,3)
print(shuttle)
print("The shuttle is located at ({}, {}), and has recorded {} flights".format(shuttle.x, shuttle.y, shuttle.flights_completed))


#======== Q4. =========

# Create several shuttles and rockets, with random positions.
#  Shuttles have a random number of flights completed.
from random import randint
shuttles = []
for x in range(0,11):
    x = randint(0,100)
    y = randint(1,100)
    flights_completed = randint(0,10)
    shuttles.append(Shuttle(x, y, flights_completed))

rockets = []
for x in range(0,11):
    x = randint(0,100)
    y = randint(1,100)
    rockets.append(Rocket(x, y))
    
# Show the number of flights completed for each shuttle.
for index, shuttle in enumerate(shuttles):
    print("Shuttle {} has completed {} flights.".format(index, shuttle.flights_completed))
    
print("\n")    
# Show the distance from the first shuttle to all other shuttles.
first_shuttle = shuttles[0]
for index, shuttle in enumerate(shuttles):
    distance = round(first_shuttle.get_distance(shuttle), 2)
    print("The first shuttle is {} units away from shuttle {}.".format(distance, index))

print("\n")
# Show the distance from the first shuttle to all other rockets.
for index, rocket in enumerate(rockets):
    distance = round(first_shuttle.get_distance(rocket), 2)
    print("The first shuttle is {} units away from rocket {}.".format(distance, index))