from musician import Musician


class Band:
    """Band class that contains a list of musicians and allows them to play."""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band, listing all musicians and their instruments."""
        musician_strs = [f"{musician.name} ({', '.join(str(instrument) for instrument in musician.instruments)})" for
                         musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strs)})"

    def add(self, musician):
        """Add a Musician to the band's list of musicians."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing what each musician in the band is playing."""
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)
