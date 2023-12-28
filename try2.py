import math
from dataclasses import dataclass, make_dataclass, field
from typing import List


class Circle:
    def __init__(self, radius):
        self._radius = radius

    def calculate_area(self):
        return round(math.pi * self._radius ** 2, 2)


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


@dataclass(order=True)
class Card:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = RANKS.index(self.rank)

    def __str__(self):
        return f"{self.suit}{self.rank}"


RANKS = "A 2 3 4 5 6 7 8 9 J Q K".split()
SUITS = "⬦ ♡ ♣ ♠".split()


def make_deck():
    return [Card(r, s) for r in RANKS for s in SUITS]


@dataclass
class Deck:
    cards: List[Card] = field(default_factory=make_deck)

    def __str__(self):
        return f"Deck({','.join(f'{c}' for c in self.cards)})"


if __name__ == "__main__":
    deck = Deck()
    print("what is in a deck", deck)

    a = Card("A", "♡")
    b = Card("2", "♣")
    print(a > b)
