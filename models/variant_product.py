from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class VariantProduct:

    # Walmart SKU

    product_id: str = ""

    title: str = ""

    url: str = ""

    availability: str = ""

    price: float | None = None

    images: List[str] = field(default_factory=list)

    attributes: Dict[str, Any] = field(default_factory=dict)

    @property
    def color(self):

        return self.attributes.get("color", "")

    @property
    def size(self):

        return self.attributes.get("size", "")

    @property
    def gender(self):

        return self.attributes.get("gender", "")

    @property
    def pack_size(self):

        return self.attributes.get("pack_size", "")

    @property
    def quantity(self):

        return self.attributes.get("quantity", "")

    @property
    def dimension(self):

        return self.attributes.get("dimension", "")