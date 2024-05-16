# input_processing.py

# Bo Zheng Ma, ENSF 692 P24

# A terminal-based program for processing computer vision changes detected by a car.
# The program will prompt the user to update the status of the traffic light, pedestrian, and vehicle.

# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Initializes the sensor object to these default values
    def __init__(self):
        light = "green"
        pedestrian = "no"
        vehicle = "no"

    # Updates the status of the sensor object
    def update_status(self, light, pedestrian, vehicle): 
        self.light = light
        self.pedestrian = pedestrian
        self.vehicle = vehicle


# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    print("Light = " + sensor.light + ", Pedestrian = " + sensor.pedestrian + ", Vehicle = " + sensor.vehicle)


# Complete the main function below
def main():
    s = Sensor()
    light = "green"
    pedestrian = "no"
    vehicle = "no"
    while(True):
        print("\n***Are changes detected in the vision input?***")
        # Prompt the user to update the status of the traffic light, pedestrian, and vehicle   
        selection = input("Select 1 to update the detected traffic light colour, 2 to update whether a pedestrian is detected, 3 to update whether a vehicle is detected, 0 to end the program\n")
        if selection == "0":
            print("Program ended.")
            return
        elif selection == "1":
            temp = input("Traffic light colour detected. Specify the colour(yellow/green/red): ")
            if(temp == "yellow" or temp == "green" or temp == "red"):
                light = temp
            else:    
                print("Invalid input, you must choose yellow/green/red. Please try again.")
        elif selection == "2":
            temp = input("Pedestrian detected. Specify the status(yes/no): ")
            if(temp == "yes" or temp == "no"):
                pedestrian = temp
            else:
                print("Invalid input, you must choose yes/no. Please try again.")
        elif selection == "3":
            temp = input("Vehicle detected. Specify the status(yes/no): ")
            if(temp == "yes" or temp == "no"):
                vehicle = temp
            else:
                print("Invalid input, you must choose yes/no. Please try again.")
        else:
            print("Invalid selection, you must enter 1/2/3/0. Please try again.")
            
        

        # Determine the action message based on the sensor status
        if(light == "red" or pedestrian == "yes" or vehicle == "yes"):
            print("\nSTOP\n")
        elif(light == "green" and (pedestrian == "no" and vehicle == "no")):
            print("\nPROCEED\n")
        elif(light == "yellow" and (pedestrian == "no" and vehicle == "no")):
            print("\nCAUTION\n")
        
        # Update the sensor status and print the status message
        s.update_status(light, pedestrian, vehicle)
        print_message(s)



# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

