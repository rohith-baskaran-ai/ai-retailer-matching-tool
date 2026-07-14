Logger

Purpose:
Centralized application logging.

Responsibilities:
- Console logging
- File logging
- Debug support

Rules:
- Every production module uses the shared logger instance.
- Never use print() in production code.

### Driver

Purpose

Create and configure the Chrome WebDriver.

Responsibilities

- Configure browser options
- Initialize WebDriver
- Handle startup failures

Rules

- Only Browser uses Driver.
- No retailer code.
- No navigation.