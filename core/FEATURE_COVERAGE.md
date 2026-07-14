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

## Browser

Location

core/browser.py

Responsibilities

- Browser lifecycle
- Navigation
- Page information
- Element operations
- Tab management

Dependencies

- Driver
- Finder
- Logger

Used By

- All retailer modules

Status

Production Ready ✅