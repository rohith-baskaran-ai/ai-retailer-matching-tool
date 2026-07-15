# models/

## Purpose

Shared data models.

Every module may import models.

Models should NEVER import business logic.

---

## Contains

- Product
- VariantProduct
- Candidate
- Job
- MatchResult

---

## Rules

Models contain only:

- Data
- Properties
- Small helper methods

Never contain:

- Browser logic
- Matching logic
- Parsing logic
- Scraping logic

---

## Product

Purpose

Represents one logical retailer-independent product.

Responsibilities

- Store product information
- Store parsed attributes
- Store variant information
- Store specifications
- Store retailer-independent data

---

## VariantProduct

Purpose

Represents one purchasable retailer SKU.

Responsibilities

- Store SKU information
- Store normalized attributes
- Store availability
- Store images
- Store price

One Product may contain many VariantProducts.

---

## Candidate

Purpose

Represents one discovered search result together with all matching scores.

Responsibilities

- Store Product
- Store identity score
- Store variant score
- Store image score
- Store final score
- Store discovery information

Candidate is NOT the final match.

It is only an evaluated search result.

---

## Job

Purpose

Represents one product matching task.

Responsibilities

- Store input product
- Store discovered candidates
- Store final selected candidate
- Track workflow status
- Store processing comments

Job flows through the entire application.

Excel Reader
↓

Job
↓

Workflow
↓

Search
↓

Matcher
↓

Result

---

### MatchResult

Purpose

Represents the outcome of a product match.

Rules

Contains data only.

Created by the Matcher.

Consumed by the Workflow and Excel Writer.

---

## Design Rules

Product
↓

Logical Product

VariantProduct
↓

Purchasable SKU

Candidate
↓

Evaluated Search Result

Job
↓

Complete Processing Pipeline

MatchResult
↓

Final Matching Decision


