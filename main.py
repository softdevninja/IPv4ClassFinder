#! /usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Requesting IPv4 Address to get classification based on range. 

References:
    https://www.geeksforgeeks.org/how-to-calculate-a-subnet-mask-from-ip-address/, 
    https://www.meridianoutpost.com/resources/articles/IP-classes.php

Example:
    Class A -> Used for networks with large number of hosts
    Class B -> Used for medium to large networks
    Class C -> Used for small local area networks
    Class D -> Used for multicasting
    Class E -> Reserved for research
"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"

import re
import sys


def main() -> None:
    """
    Performs 2 types of condition checks before serving a result.
    - Checks to see if the regex pattern matches user input
    - Checks to make sure the value of each octet does not exceed 8 bits

    Returns: None
    """
    ip_Address: str = None
    ip_oct: list = None
    pattern: str = re.compile(r"\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}")

    ip_Address = input("Please enter IPv4 address for classification: ")
    result = pattern.match(ip_Address)

    if is_valid_address(result):
        check_boundaries: bool = False

        ip_oct = list(map(int, ip_Address.split(".")))
        check_boundaries = len([x for x in ip_oct if x >= 256]) == 0

        if check_boundaries is False:
            exit_program()

        if ip_oct[0] <= 127 and ip_oct[1] <= 255:
            print(f"{ip_Address} --> Belongs to Class A")
        elif ip_oct[0] >= 128 and (ip_oct[0] <= 191 and ip_oct[1] <= 255):
            print(f"{ip_Address} --> Belongs to Class B")
        elif (
            ip_oct[0] >= 192
            and (ip_oct[0] <= 223 and ip_oct[1] <= 255)
            and ip_oct[2] <= 255
        ):
            print(f"{ip_Address} --> Belongs to Class C")
        elif ip_oct[0] >= 224 and ip_oct[0] < 240:
            print(f"{ip_Address} --> Belongs to Class D")
        else:
            print(f"{ip_Address} --> Belongs to Class E")

    else:
        exit_program()


def is_valid_address(result: float) -> bool:
    """
    Checks to see if regex returned a positive match.

    Args:
        result (float): Represents the result from regex.

    Returns:
        bool: Returns true if pattern is found
    """
    return bool(result)


def exit_program() -> None:
    """
    Using OS module, gracefully exit the application.

    Returns:
        None:
    """
    print(f"Entry not accepted. Terminating program, good bye!.")
    sys.exit(0)


if __name__ == "__main__":
    main()
