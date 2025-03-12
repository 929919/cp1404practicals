"""CP1404 Intermediate Exercises - Languages program.
Estimated time: 10 minutes
Actual time: [To be recorded]
Start time: 10:21 AM, March 11, 2025
"""
from programming_language import ProgrammingLanguage

def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

if __name__ == "__main__":
    main()