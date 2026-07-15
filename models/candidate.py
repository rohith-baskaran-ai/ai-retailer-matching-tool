"""
Module:
    Candidate

Purpose:
    Represents one discovered candidate product together with
    all matching scores.

Author:
    Rohith + ChatGPT

Version:
    1.0
"""

from dataclasses import dataclass, field

from models.product import Product


@dataclass
class Candidate:

    product: Product = field(default_factory=Product)

    identity_score: float = 0.0

    variant_score: float = 0.0

    image_score: float = 0.0

    final_score: float = 0.0

    best_rank: int = 999

    discovery_count: int = 0

    discovered_by: list[str] = field(default_factory=list)