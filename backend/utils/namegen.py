import random
from crud.url_crud import get_url

ADJECTIVES = [
    "silent", "brave", "calm", "dark", "swift", "cold", "bold", "wild",
    "pale", "soft", "bright", "fierce", "gentle", "hollow", "iron", "jade",
    "keen", "lost", "misty", "noble", "odd", "proud", "quiet", "rough",
    "sharp", "tall", "vast", "warm", "young", "azure", "crimson", "dusty",
    "elder", "faint", "grand", "heavy", "icy", "jolly", "kind", "lunar",
    "muddy", "narrow", "open", "plain", "rapid", "stony", "tired", "urban",
    "vivid", "windy"
]

NOUNS = [
    "river", "falcon", "stone", "ember", "ridge", "cloud", "flame", "brook",
    "cedar", "dune", "frost", "grove", "haven", "isle", "jungle", "knoll",
    "lagoon", "marsh", "nexus", "orbit", "peak", "quill", "reef", "shore",
    "tide", "vale", "wave", "xenon", "yard", "zenith", "arrow", "basin",
    "crest", "delta", "echo", "field", "glade", "horizon", "inlet", "jewel",
    "kite", "lance", "moon", "nova", "oak", "pine", "quest", "rain",
    "storm", "torch"
]

def generate_name(db) -> str:
    # try adjective-noun first
    name = f"{random.choice(ADJECTIVES)}-{random.choice(NOUNS)}"
    if not get_url(db, name):
        return name

    # collision — try adjective-adjective-noun
    name = f"{random.choice(ADJECTIVES)}-{random.choice(ADJECTIVES)}-{random.choice(NOUNS)}"
    if not get_url(db, name):
        return name

    # worst case — add a number suffix
    name = f"{name}-{random.randint(10, 9999)}"
    return name