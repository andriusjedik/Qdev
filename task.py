import os
import datetime

data = None

def read_data_file(file_path):
    global data
    try:
        with open(file_path, 'r') as file:
            data = file.readlines()
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Failed to read file: {e}")
        data = None


# 0. Complete tasks 1-5.
def task0():
    task1()
    task2()
    task3()
    task4()
    task5()


# 1. Find the number of red, yellow & green occurrences.
def task1():
    print("Task 1: Number of occurrences by color:")
    red_occurrences = 0
    yellow_occurrences = 0
    green_occurrences = 0
    for line in data[1:]:
        red, yellow, green, _, _ = line.strip().split(',')
        red_occurrences += int(red)
        yellow_occurrences += int(yellow)
        green_occurrences += int(green)
    print(f"Red={red_occurrences}, Yellow={yellow_occurrences}, Green={green_occurrences}")


# 2. Find how long each color was active for.
def task2():
    print("Task 2: Each color active times:")
    red_time = 0
    yellow_time = 0
    green_time = 0

    for line in data[1:]:
        red, yellow, green, time_active, _ = line.strip().split(',')
        time_active = int(time_active)
        
        if int(red) == 1:
            red_time += time_active
        if int(yellow) == 1:
            yellow_time += time_active
        if int(green) == 1:
            green_time += time_active

    print(f"Red={red_time} seconds, Yellow={yellow_time} seconds, Green={green_time} seconds")


# 3. Find all times when Green was active (by time).
def task3():
    print("Task 3: All times when green was active:")
    green_times = []

    for line in data[1:]:
        _, _, green, _, time = line.strip().split(',')
        if int(green) == 1:
            green_times.append(time)

    print(f"{green_times}")


# 4. Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data.
def task4():
    print("Task 4: Number of complete Red-Yellow-Green-Yellow-Red cycles: ")

    complete_cycle = 0
    state = 0

    for line in data[1:]:
        red, yellow, green, _, _ = line.strip().split(',')
        red, yellow, green = int(red), int(yellow), int(green)

        if state == 0 and red == 1 and yellow == 0 and green == 0:
            state = 1
        elif state == 1 and red == 0 and yellow == 1 and green == 0:
            state = 2
        elif state == 2 and red == 0 and yellow == 0 and green == 1:
            state = 3
        elif state == 3 and red == 0 and yellow == 1 and green == 0:
            state = 4
        elif state == 4 and red == 1 and yellow == 0 and green == 0:
            complete_cycle += 1
            state = 1

    print(f"{complete_cycle}")

# This method works when we exclude overlaping cycles,
# then the number changes, but I was not sure what by 
# saying "Complete" you meant. Please comment function above 
# and un-comment function below, and see what I mean by 
# running example_data.txt.

# def task4():
#     print("Task 4: Number of complete Red-Yellow-Green-Yellow-Red cycles: ")

#     current_cycle = []
#     complete_cycles = 0
#     valid_cycle = ['Red', 'Yellow', 'Green', 'Yellow', 'Red']

#     for line in data[1:]:
#         red, yellow, green, _, _ = line.strip().split(',')

#         if int(red) == 1:
#             current_cycle.append('Red')
#         elif int(yellow) == 1:
#             current_cycle.append('Yellow')
#         elif int(green) == 1:
#             current_cycle.append('Green')

#         if current_cycle == valid_cycle:
#             complete_cycles += 1
#             current_cycle = []

#         if len(current_cycle) > 0 and not all(current_cycle[i] == valid_cycle[i] for i in range(len(current_cycle))):
#             current_cycle = []

#     print(f"{complete_cycles}")


# 5. Find number of lines with mistakes (multiple colors active at the same time or no colors active).
def task5():
    print("Task 5: Lines with mistakes found:")

    mistakes = 0

    for line in data[1:]:
        red, yellow, green, _, _ = line.strip().split(',')
        
        red = int(red)
        yellow = int(yellow)
        green = int(green)
        
        active_colors = red + yellow + green

        if active_colors != 1:
            mistakes += 1

    print(f"{mistakes}")


def main():
    global data
    
    while True:
        use_custom_path = input("Hello, would you like to use a custom path for your data file? If not default file will be used. (y/n): ").strip().lower()
        if use_custom_path in ['y', 'n']:
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

    if use_custom_path == 'y':
        while True:
            custom_data_path = input("Please enter the full path to the data file: ").strip()
            if os.path.exists(custom_data_path):
                data_path = custom_data_path
                print(f"Using custom data path: {data_path}")
                break
            else:
                print("The provided path does not exist. Please try again.")
    else:
        data_path = "data.txt"
        print(f"Using default data path: {data_path}")

    read_data_file(data_path)

    print("Now, please specify which task this script should do?")
    print("Possible options:")
    print("0. Complete tasks 1-5.")
    print("1. Find the number of red, yellow & green occurrences.")
    print("2. Find how long each colour was active for.")
    print("3. Find all times when Green was active (by time).")
    print("4. Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data.")
    print("5. Find number of lines with mistakes (multiple colours active at the same time or no colours active).")
    print("6. Exit the program.")

    while True:

        task = input("Enter the task number (0-6): ")

        try:
            task = int(task)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if task == 0:
            task0()
        elif task == 1:
            task1()
        elif task == 2:
            task2()
        elif task == 3:
            task3()
        elif task == 4:
            task4()
        elif task == 5:
            task5()
        elif task == 6:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option selected. Please choose a valid task number.")

if __name__ == "__main__":
    main()