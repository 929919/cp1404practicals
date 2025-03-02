"""
Wimbledon Champions Data Processing
Estimate: 25 minutes
Actual:
"""
def read_wimbledon_data(filename):
    """Read the Wimbledon CSV file and return data as a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        return [line.strip().split(',') for line in file.readlines()[1:]]

def process_wimbledon_data(data):
    """Process Wimbledon data to count wins per champion and track winning countries."""
    champions = {}
    countries = set()

    for entry in data:
        champion, country = entry[2], entry[1]
        champions[champion] = champions.get(champion, 0) + 1
        countries.add(country)

    return champions, sorted(countries)
