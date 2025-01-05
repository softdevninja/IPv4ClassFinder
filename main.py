#! /usr/bin/env python3
import re


def main() -> None:
    IP_Address: str = None
    pattern: str = re.compile(r"\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}")

    IP_Address = input("Please enter IPv4 address for classification: ")

    result = pattern.match(IP_Address)

    if is_valid_address(result):
        print("A match")
    else:
        print("Entry not accepted")


def is_valid_address(result: float) -> bool:
    return bool(result)


if __name__ == "__main__":
    main()
