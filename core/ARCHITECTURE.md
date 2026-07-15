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

### Browser
Rules

- Only Browser uses Driver.
- No retailer code.
- No navigation.

Responsibilities

- Own WebDriver
- Own Finder
- Manage browser tabs
- Open pages
- Expose browser operations

## Finder

Location

core/finder.py

Responsibilities

- Find single element
- Find multiple elements
- Read text
- Read attributes
- Click elements
- Check element existence
- Return page HTML

Dependencies

- Selenium
- config.py

Used By

- Browser

Status

Production Ready ✅

Browser is the ONLY module allowed to interact directly with Selenium.

No other module may access WebDriver.

All retailer modules must use Browser methods.
