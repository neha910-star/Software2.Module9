import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        # Calculate new speed
        new_speed = self.current_speed + speed_change

        # Ensure speed doesn't exceed maximum speed
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        # Ensure speed doesn't go below zero
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        # Calculate distance travelled: speed * time
        distance_travelled = self.current_speed * hours

        # Increase the travelled distance
        self.travelled_distance += distance_travelled


def main():
    # Create a list of 10 car objects
    cars = []
    for i in range(1, 11):
        registration = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        car = Car(registration, max_speed)
        cars.append(car)

    print("Starting the car race!")
    print("Race parameters:")
    print("- 10 cars")
    print("- Speed changes: -10 to +15 km/h per hour")
    print("- Race distance: 10,000 km")
    print("- Each car drives 1 hour per race hour")
    print()

    # Race simulation
    hour = 0
    race_finished = False

    while not race_finished:
        hour += 1
        print(f"Hour {hour}:")

        # For each car in the race
        for car in cars:
            # Change speed by random value between -10 and +15 km/h
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)

            # Drive for 1 hour
            car.drive(1)

            # Check if any car has reached 10,000 km
            if car.travelled_distance >= 10000:
                race_finished = True
                print(f"  {car.registration_number} has reached {car.travelled_distance} km! Race finished!")
                break
        else:
            # This runs if no break occurred in the inner loop
            leader = max(cars, key=lambda x: x.travelled_distance)
            print(f"  Current leader: {leader.registration_number} ({leader.travelled_distance} km)")
            continue

        # Break out of the while loop if race is finished
        break

    print(f"\nRace completed in {hour} hours!")
    print()

    # Print final results in a table
    print("FINAL RACE RESULTS")
    print("=" * 70)
    print(
        f"{'Registration':<12} {'Max Speed (km/h)':<15} {'Final Speed (km/h)':<18} {'Distance (km)':<12} {'Status':<10}")
    print("-" * 70)

    # Sort cars by distance travelled (descending)
    cars.sort(key=lambda x: x.travelled_distance, reverse=True)

    for car in cars:
        status = "WINNER!" if car.travelled_distance >= 10000 else ""
        print(
            f"{car.registration_number:<12} {car.max_speed:<15} {car.current_speed:<18} {car.travelled_distance:<12.1f} {status:<10}")

    print("=" * 70)


# Run the main program
if __name__ == "__main__":
    main()