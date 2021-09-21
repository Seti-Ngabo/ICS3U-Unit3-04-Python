#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program tells you if the number is positive/negative/0
#   with user input


def main():
    # this function checks if the number is >0/ <0/ ==0

    # input
    number = int(input("Enter a number (integer): "))
    print("")

    # process and output
    if number > 0:
        print("The number is a positive integer.")
    elif number < 0:
        print("The number is a negative integer.")
    else:
        print("The number is 0.")
    print("\nDone.")


if __name__ == "__main__":
    main()
