"""
Module:
    MatchResult

Purpose:
    Represents the final outcome of the product matching process.

Responsibilities:
    - Store overall match score
    - Store match decision
    - Store matching method
    - Store debug information
    - Store execution time

Author:
    Rohith + ChatGPT

Version:
    1.0
"""

from dataclasses import dataclass, field


@dataclass
class MatchResult:

    # ==================================================
    # Overall Result
    # ==================================================

    score: float = 0.0

    matched: bool = False

    method: str = ""

    # ==================================================
    # Debug Information
    # ==================================================

    matched_values: list[str] = field(default_factory=list)

    missing_values: list[str] = field(default_factory=list)

    extra_values: list[str] = field(default_factory=list)

    notes: list[str] = field(default_factory=list)

    execution_time: float = 0.0