import random

# Constant for the range of numbers
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def generate_quick_pick():
    """Generate a sorted list of 6 unique random numbers between 1 and 45."""
    quick_pick = random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_PICK)
    quick_pick.sort()
    return quick_pick


def main():
    """Main function to execute the lottery quick pick generator."""
    num_picks = int(input("How many quick picks? "))

    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2d}" for num in quick_pick))


if __name__ == "__main__":
    main()