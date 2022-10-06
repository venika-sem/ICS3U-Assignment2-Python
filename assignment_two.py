#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Sep 2022
# This program calculates the perimeter of a parallelogram
#    with base and side inputted from the user

import math


def main():
    # this function calculates the perimeter of a parallelogram

    # input
    base_of_parallelogram = int(input("Enter the base (mm): "))
    side_of_parallelogram = int(input("Enter the side (mm): "))

    # process
    perimeter_of_parallelogram = 2 * (base_of_parallelogram + side_of_parallelogram)

    # output
    print("")
    print(
        "The perimeter of the parallelogram is {0} mm.".format(
            perimeter_of_parallelogram
        )
    )

    print("\nDone.")


if __name__ == "__main__":
    main()
