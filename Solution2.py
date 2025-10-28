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


def main():
    # Create a new car with registration number ABC-123 and maximum speed 142 km/h
    new_car = Car("ABC-123", 142)

    # Print initial properties
    print("Initial Car Properties:")
    print(f"Registration Number: {new_car.registration_number}")
    print(f"Maximum Speed: {new_car.max_speed} km/h")
    print(f"Current Speed: {new_car.current_speed} km/h")
    print(f"Travelled Distance: {new_car.travelled_distance} km")
    print()

    # Test the accelerate method
    print("Testing accelerate method:")

    # Increase speed by +30 km/h
    new_car.accelerate(30)
    print(f"After +30 km/h: {new_car.current_speed} km/h")

    # Increase speed by +70 km/h
    new_car.accelerate(70)
    print(f"After +70 km/h: {new_car.current_speed} km/h")

    # Increase speed by +50 km/h
    new_car.accelerate(50)
    print(f"After +50 km/h: {new_car.current_speed} km/h")

    # Print current speed
    print(f"\nCurrent speed before emergency brake: {new_car.current_speed} km/h")

    # Emergency brake: force -200 km/h change
    new_car.accelerate(-200)
    print(f"After emergency brake (-200 km/h): {new_car.current_speed} km/h")

    # Print final speed
    print(f"\nFinal speed: {new_car.current_speed} km/h")


# Run the main program
if __name__ == "__main__":
    main()