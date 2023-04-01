import json
import time
import os


def load_units():
    with open("units.json", "r") as f:
        units = json.load(f)
    return units


def print_categories(units):
    print("Available unit categories:")
    for category in units.keys():
        print("-", category)


def print_units(units, category):
    print("Available units for {}: ".format(category))
    for unit in units[category].keys():
        print("-", unit)


def convert_units(units, category, source_unit, target_unit, value):
    converted_value = value * \
        units[category][source_unit] / units[category][target_unit]
    return converted_value


if __name__ == '__main__':
    units = load_units()

    while True:
        print("|------------------|")
        print("|  Unit Converter  |")
        print("| 1. Convert units |")
        print("| 2. Quit          |")
        print("|------------------|")
        print()

        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            print_categories(units)
            category = input("Select a unit category: ")
            while category not in units:
                print("Invalid category!")
                category = input("Select a unit category: ")
            print()
            print_units(units, category)
            source_unit = input("Enter the source unit: ")
            while source_unit not in units[category]:
                print("Invalid source unit!")
                source_unit = input("Enter the source unit: ")

            print()
            target_unit = input("Enter the target unit: ")
            while target_unit not in units[category]:
                print("Invalid target unit!")
                target_unit = input("Enter the target unit: ")

            print()
            value = float(input("Enter the value to convert: "))

            print()
            print("Converting {} {} to {}...".format(
                value, source_unit, target_unit))
            time.sleep(3)
            converted_value = convert_units(
                units, category, source_unit, target_unit, value)
            print("Result: {:.2f} {} (was {:.2f} {})".format(
                converted_value, target_unit, value, source_unit))

            input("\nPress Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif choice == "2":
            print("Goodbye!")
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        else:
            print("Invalid chice, please try again.")
