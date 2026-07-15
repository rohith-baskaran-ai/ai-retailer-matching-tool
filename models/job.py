"""
Module:
    Job

Purpose:
    Represents one product matching job.

Responsibilities:
    - Store target product
    - Store discovered candidates
    - Store final selected candidate
    - Track workflow status
    - Store processing comments

Author:
    Rohith + ChatGPT

Version:
    1.0
"""

from dataclasses import dataclass, field

from models.product import Product
from models.candidate import Candidate


@dataclass
class Job:

    row_number: int = 0

    retailer: str = ""

    target: Product = field(default_factory=Product)

    candidates: list[Candidate] = field(default_factory=list)

    final_candidate: Candidate | None = None

    status: str = "PENDING"

    comments: list[str] = field(default_factory=list)