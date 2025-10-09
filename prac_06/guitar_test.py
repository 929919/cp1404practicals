"""CP1404 Practical - Guitar test program.
Estimated time: 15 minutes
Actual time: 15 minutes
"""
from guitar import Guitar

def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 0)

    print(f"Gibson L-5 CES get_age() - Expected 103. Got {guitar1.get_age()}")
    print(f"Another Guitar get_age() - Expected 12. Got {guitar2.get_age()}")

    print(f"Gibson L-5 CES is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"Another Guitar is_vintage() - Expected False. Got {guitar2.is_vintage()}")

if __name__ == "__main__":
    main()