from My_Point import *
from Point_Repository import *

def print_menu():
    print("\nMenu:")
    print("1. Add a point")
    print("2. Update a point")
    print("3. Delete a point")
    print("4. Delete points in a square")
    print("5. Show all points")
    print("6. Find minimum distance")
    print("7. Get all points")
    print("8. Get point by index")
    print("9. Get points by color")
    print("10. Get points in a square")
    print("11. Get number of points by color")
    print("12. Shift all points on the y-axis")
    print("13. Delete points within a certain distance")
    print("14. Exit")


def main():
    repository = PointRepository()
    colors = ["red", "green", "blue", "yellow"]

    while True:
        print_menu()
        choice = input("Select an option (1-14): ")

        if choice == "1":
            x = float(input("Enter x coordinate: "))
            y = float(input("Enter y coordinate: "))
            color = input("Enter color: ")
            if isinstance(x, float) and isinstance(y, float) and color in colors:
                point = MyPoint(x, y, color)
                repository.add(point)
                print("Point added.")
            else:
                print("Invalid coordinates or color.")

        elif choice == "2":
            index = int(input("Enter point index to update: "))
            x = float(input("Enter new x coordinate: "))
            y = float(input("Enter new y coordinate: "))
            color = input("Enter new color: ")
            if isinstance(x, float) and isinstance(y, float) and color in colors:
                repository.update(index, x, y, color)
                print("Point updated.")
            else:
                print("Invalid coordinates or color.")

        elif choice == "3":
            index = int(input("Enter point index to delete: "))
            if 0 <= index < len(repository.get_all_points()):
                repository.delete(index)
                print("Point deleted.")
            else:
                print("Index out of range.")

        elif choice == "4":
            x = float(input("Enter top-left x coordinate of square: "))
            y = float(input("Enter top-left y coordinate of square: "))
            length = float(input("Enter square side length: "))
            if isinstance(x, float) and isinstance(y, float) and length > 0:
                point = MyPoint(x, y, "")
                repository.delete_square(point, length)
                print("Points deleted.")
            else:
                print("Invalid coordinates or length.")

        elif choice == "5":
            repository.show_points()

        elif choice == "6":
            min_dist = repository.minimum_distance()
            print(f"The minimum distance between any two points is: {min_dist}")

        elif choice == "7":
            points = repository.get_all_points()
            for i, point in enumerate(points):
                print(f"{i}: ({point.get_x()}, {point.get_y()}) - {point.get_color()}")

        elif choice == "8":
            index = int(input("Enter point index: "))
            if 0 <= index < len(repository.get_all_points()):
                point = repository.get_point_by_index(index)
                print(f"Point at index {index}: ({point.get_x()}, {point.get_y()}) - {point.get_color()}")
            else:
                print("Index out of range.")

        elif choice == "9":
            color = input("Enter color to search for: ")
            if color in colors:
                points = repository.get_point_by_color(color)
                if points:
                    for point in points:
                        print(f"({point.get_x()}, {point.get_y()}) - {point.get_color()}")
                else:
                    print("No points found with that color.")

        elif choice == "10":
            x = float(input("Enter top-left x coordinate of square: "))
            y = float(input("Enter top-left y coordinate of square: "))
            length = float(input("Enter square side length: "))
            point = MyPoint(x, y, "")
            points = repository.get_points_in_square(point, length)
            if points:
                for point in points:
                    print(f"({point.get_x()}, {point.get_y()}) - {point.get_color()}")
            else:
                print("No points found within the square.")

        elif choice == "11":
            color = input("Enter the color to count points for: ")
            if color in colors:
                count = repository.get_number_of_points_by_color(color)
                print(f"There are {count} point(s) with the color {color}.")
            else:
                print("Invalid color.")

        elif choice == "12":
            repository.shift_all_points_on_y_axis()
            print("All points have been shifted along the y-axis.")

        elif choice == "13":
            x = float(input("Enter the x-coordinate of the reference point: "))
            y = float(input("Enter the y-coordinate of the reference point: "))
            distance = float(input("Enter the maximum distance from the reference point: "))
            repository.delete_points_within_distance(x, y, distance)
            print("Points within the specified distance have been deleted.")

        elif choice == "14":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()