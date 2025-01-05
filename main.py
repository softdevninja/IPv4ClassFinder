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
    IP_Address: str = None
    pattern: str = re.compile(r"\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}")

    IP_Address = input("Please enter IPv4 address for classification: ")
    print(IP_Address)

    result = pattern.match(IP_Address)

    if is_valid_address(result):
        print("A match")
    else:
        exit_program()


def is_valid_address(result: float) -> bool:
    return bool(result)


def exit_program() -> None:
    print(f"Entry not accepted. Terminating program, good bye!.")
    sys.exit(0)


if __name__ == "__main__":
    main()
