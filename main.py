#! /usr/bin/env python3
import re

sample = "232.113.411.115"

def main() -> None:
    IP_Address : str = None
    
# r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}'
pattern  = re.compile(r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}')
matches = pattern.match(sample)

if matches == None:
    print("false")

print("true")


if __name__ == "__main__":
    main()