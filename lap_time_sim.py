import random

total_laps = int(input("Enter the total number of laps: "))
length_per_lap = int(input("Enter the length of one lap(km): "))
avg_speed = int(input("Enter the average speed(km/h): "))
data_speed_time = []
total_length = float(length_per_lap * total_laps)

for lap in range(total_laps):
    var_speed = round(avg_speed + random.uniform(-7, 7) , 2)
    var_time = round(length_per_lap / var_speed * 60, 2)
    data_speed_time.append({"lap" : lap, "speed" : var_speed, "time" : var_time})

avg_speedf = round(sum(speed["speed"] for speed in data_speed_time) / len(data_speed_time), 2)
avg_timef = round(sum(time["time"] for time in data_speed_time) / len(data_speed_time), 2)
print("The average lap time is " + str(avg_timef) + " minutes")
fastlt = min(ft["time"] for ft in data_speed_time)
slowlt = max(ft["time"] for ft in data_speed_time)
print("The fastest lap time is " + str(fastlt) + " minutes")
print("The slowest lap time is " + str(slowlt) + " minutes")