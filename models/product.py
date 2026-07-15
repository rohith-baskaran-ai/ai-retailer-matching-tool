"""
Module:
    Product

Purpose:
    Retailer-independent product model used throughout the
    Product Matching Framework.

Responsibilities:
    - Store product information
    - Store parsed attributes
    - Store variant information
    - Store specifications
    - Store retailer-independent data

Author:
    Rohith + ChatGPT

Version:
    2.0
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class Product:
    # ==================================================
    # Basic Product Information
    # ==================================================

    title: str = ""
    brand: str = ""
    description: str = ""
    upc: str = ""
    url: str = ""

    image: str = ""
    images: List[str] = field(default_factory=list)

    price: str = ""

    retailer: str = ""

    # ==================================================
    # Category Information
    # ==================================================

    category: str = ""
    subcategory: str = ""

    # ==================================================
    # Parsed Information
    # ==================================================

    identity_title: str = ""

    gender: str = ""

    color: str = ""

    size: str = ""

    pack_size: str = ""

    quantity: str = ""

    dimension: str = ""

    # ==================================================
    # Variant Information
    # ==================================================

    # Raw variant information from retailer

    variants: List[Any] = field(default_factory=list)

    # Normalized lookup

    variant_map: Dict[str, Any] = field(default_factory=dict)

    # Fully expanded variant products

    variant_products: List[Any] = field(default_factory=list)

    # ==================================================
    # Additional Information
    # ==================================================

    specifications: Dict[str, Any] = field(default_factory=dict)

    attributes: Dict[str, Any] = field(default_factory=dict)