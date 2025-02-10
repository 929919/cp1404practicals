import random

def determine_score_status(score):
    """Determine the score status based on the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    """Get user input, determine score status, and generate a random score."""
    score = float(input("Enter score: "))
    print(determine_score_status(score))

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score} - {determine_score_status(random_score)}")

main()
