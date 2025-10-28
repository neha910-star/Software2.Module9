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
    print()

    # Test the drive method
    print("Testing drive method:")

    # Reset travelled distance for demonstration
    new_car.travelled_distance = 2000
    new_car.current_speed = 60

    print(f"Starting distance: {new_car.travelled_distance} km")
    print(f"Current speed: {new_car.current_speed} km/h")

    # Drive for 1.5 hours
    new_car.drive(1.5)
    print(f"After driving 1.5 hours: {new_car.travelled_distance} km")

    # Additional drive tests
    print("\nAdditional drive tests:")

    # Create a new car for fresh demonstration
    test_car = Car("TEST-001", 120)
    test_car.accelerate(80)  # Set speed to 80 km/h

    print(f"\nNew car - Speed: {test_car.current_speed} km/h, Distance: {test_car.travelled_distance} km")

    test_car.drive(2)  # Drive for 2 hours
    print(f"After driving 2 hours: {test_car.travelled_distance} km")

    test_car.drive(0.5)  # Drive for 30 minutes
    print(f"After driving 0.5 hours: {test_car.travelled_distance} km")


# Run the main program
if __name__ == "__main__":
    main()