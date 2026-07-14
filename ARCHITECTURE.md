# Product Matching Framework
## Architecture Document v1.0

---

# Vision

The goal of this project is to build a scalable Retail Product Matching Framework.

The framework should support multiple retailers (Target, Walmart, Amazon, Costco, etc.) while keeping retailer-specific logic isolated and shared logic reusable.

The architecture follows these principles:

- Single Responsibility Principle
- Modular Design
- Feature-Oriented Development
- Reusable Components
- Easy Testing
- Easy Expansion

---

# Project Structure

```
product_matching/
│
├── core/
├── models/
├── excel/
├── parser/
├── retailer/
├── search/
├── matcher/
├── image/
├── utils/
├── resources/
├── tests/
│
├── config.py
├── main.py
└── ARCHITECTURE.md
```

---

# Folder Responsibilities

---

# core/

## Purpose

Application infrastructure.

Contains components required for the application to run.

## Contains

- Browser
- Chrome Driver
- Logger
- Workflow
- Tab Manager

## Allowed

✔ Browser Management

✔ Logging

✔ Workflow Orchestration

✔ Shared Services

## Not Allowed

✘ Retailer Logic

✘ Product Matching

✘ Title Parsing

✘ Excel Logic

---

# models/

## Purpose

Shared data models.

Every module may import models.

Models should NEVER import business logic.

## Contains

- Product
- VariantProduct
- Candidate
- Job
- MatchResult

## Rules

Models contain only:

- Data
- Properties
- Small helper methods

No browser.

No matching.

No scraping.

---

# excel/

## Purpose

Read and write Excel files.

## Contains

- Reader
- Writer

## Allowed

✔ Read Excel

✔ Write Excel

## Not Allowed

✘ Parsing

✘ Matching

✘ Searching

✘ Retailer Logic

---

# parser/

## Purpose

Extract structured information from text.

Input

Product Title

Output

- Identity Title
- Brand
- Color
- Size
- Gender
- Pack Size
- Quantity
- Dimensions

## Contains

- TitleParser
- KeywordExtractor

## Allowed

✔ Text Parsing

✔ Keyword Extraction

## Not Allowed

✘ Browser

✘ JSON

✘ Matching

✘ Retailer Logic

---

# retailer/

Everything retailer-specific belongs here.

Retailers must never depend on each other.

---

## retailer/target/

Responsible only for Target.

Contains

- Reader
- Mapper
- Finder

Allowed

✔ Read Target PDP

✔ Parse Target JSON

✔ Convert JSON → Product

Not Allowed

✘ Walmart

✘ Matching

✘ Excel

---

## retailer/walmart/

Responsible only for Walmart.

Contains

- Session
- Discovery
- Extractor
- Reader
- Mapper
- VariantReader
- VariantProductReader
- ProductNodeFinder

Allowed

✔ Search Walmart

✔ Discover Products

✔ Read PDP

✔ Read Variants

✔ Convert JSON → Product

Not Allowed

✘ Target

✘ Matching

✘ Excel

---

# search/

## Purpose

Retailer-independent search pipeline.

Contains

- SearchStrategy
- SearchExecutor
- CandidatePool

Allowed

✔ Build Search Strategies

✔ Execute Searches

✔ Merge Results

✔ Remove Duplicates

Not Allowed

✘ PDP Reading

✘ Matching

---

# matcher/

## Purpose

Compare products.

Never scrape.

Never read webpages.

Contains

- IdentityMatcher
- VariantResolver
- ImageMatcher

Allowed

✔ Compare Products

✔ Score Products

✔ Resolve Variants

Not Allowed

✘ Browser

✘ Search

✘ JSON

---

# matcher/filters/

Contains one filter per attribute.

Example

- ColorFilter
- SizeFilter
- GenderFilter
- PackFilter
- QuantityFilter
- DimensionFilter

Rule

One Filter = One Responsibility

---

# image/

Purpose

Everything image related.

Contains

- Downloader
- Cache
- ImageMatcher
- CLIP
- SigLIP

Allowed

✔ Download Images

✔ Cache Images

✔ Compare Images

Not Allowed

✘ Product Matching Logic

---

# utils/

Purpose

Reusable helper utilities.

These utilities should be generic enough to reuse in another project.

Contains

- Finder
- JsonSearch
- ResourceLoader
- ValueNormalizer

Allowed

✔ Generic Utilities

Not Allowed

✘ Retailer-specific Logic

✘ Business Logic

---

# resources/

Contains static resource files.

Examples

- colors.txt
- genders.txt
- sizes.txt
- quantity_units.txt
- dimension_units.txt

Contains ONLY data.

Never code.

---

# tests/

Contains test scripts.

Every production component should eventually have a corresponding test.

Example

test_title_parser.py

test_target_reader.py

test_identity_matcher.py

---

# Application Flow

```
Excel
    │
    ▼
Excel Reader
    │
    ▼
Title Parser
    │
    ▼
Target Reader
    │
    ▼
Search Strategy Builder
    │
    ▼
Search Executor
    │
    ▼
Retailer Search
    │
    ▼
Discovery
    │
    ▼
Candidate Pool
    │
    ▼
Identity Matcher
    │
    ▼
Top Candidates
    │
    ▼
Retailer Product Reader
    │
    ▼
Variant Resolver
    │
    ▼
Image Matcher
    │
    ▼
Final Decision
    │
    ▼
Excel Writer
```

---

# Golden Rules

## Rule 1

One Class = One Responsibility

---

## Rule 2

One Folder = One Responsibility

---

## Rule 3

Readers only read.

Never compare.

---

## Rule 4

Matchers only compare.

Never scrape.

---

## Rule 5

Parsers only parse.

Never search.

---

## Rule 6

Retailer folders know only their own retailer.

Never import another retailer.

---

## Rule 7

Shared logic belongs in

- core
- models
- utils

Never duplicate it.

---

## Rule 8

Never use

sys.path.insert(...)

Use proper package imports.

---

## Rule 9

Never use print() in production.

Use Logger.

---

## Rule 10

Workflow controls the application.

Every module performs ONE job.

Workflow connects them.

---

## Rule 11

Think in Features, not Files.

Always ask

"What feature am I implementing?"

before asking

"Which file should I edit?"

---

## Rule 12

Every new feature must answer these questions

1. Does this feature already exist?

2. Which folder owns this responsibility?

3. Can I extend an existing class?

4. Is this retailer-specific?

5. Is this reusable?

If uncertain,

STOP

Review ARCHITECTURE.md

before writing code.

---

# Project Status

Infrastructure

⬜ Browser

⬜ Logger

⬜ Config

⬜ Workflow

Core

⬜ Models

⬜ Excel

⬜ Parser

Retailers

⬜ Target

⬜ Walmart

Matching

⬜ Identity

⬜ Variant

⬜ Image

Output

⬜ Excel Writer

⬜ Main