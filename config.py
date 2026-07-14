"""
Application Configuration

This file contains global configuration values used across the
Product Matching Framework.

Guidelines:
- Configuration only.
- No business logic.
- No functions.
- No retailer-specific values.
"""

# ==========================================================
# General
# ==========================================================

DEBUG = True

SKIP_COMPLETED = False


# ==========================================================
# Browser
# ==========================================================

HEADLESS = False

CHROME_VERSION = 149


# ==========================================================
# Timeouts
# ==========================================================

PAGE_LOAD_TIMEOUT = 60

ELEMENT_TIMEOUT = 20

PAGE_STABILIZE_TIME = 3


# ==========================================================
# Search
# ==========================================================

MAX_SEARCH_RESULTS = 20

TOP_CANDIDATES = 5


# ==========================================================
# Matching
# ==========================================================

IDENTITY_THRESHOLD = 85

IMAGE_THRESHOLD = 90


# ==========================================================
# Retry
# ==========================================================

MAX_RETRY = 2