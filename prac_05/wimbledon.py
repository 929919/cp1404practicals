"""
Wimbledon Champions Data Processing
Estimate: 25 minutes
Actual:
"""
def read_wimbledon_data(filename):
    """Read the Wimbledon CSV file and return data as a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        return [line.strip().split(',') for line in file.readlines()[1:]]
