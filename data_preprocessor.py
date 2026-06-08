# Data preprocessor
from typing import Iterable

def normalize(items: Iterable[str]) -> list[str]:
    return [s.strip().lower() for s in items if s and s.strip()]
