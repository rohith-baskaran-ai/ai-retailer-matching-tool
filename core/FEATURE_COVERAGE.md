# Feature Coverage

---

## Logger

Location

core/logger.py

Responsibilities

- Console logging
- File logging
- Timestamped log files
- Debug logging

Used By

- Browser
- Parser
- Search
- Reader
- Matcher
- Workflow

## Driver

Location
core/driver.py

Purpose
Creates and configures the Chrome WebDriver.

Responsibilities
- Configure Chrome options
- Initialize WebDriver
- Apply global browser configuration
- Return configured driver

Dependencies
- config.py
- core.logger
- undetected_chromedriver

Used By
- Browser

Status
Production Ready ✅