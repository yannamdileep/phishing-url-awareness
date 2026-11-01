
# Phishing URL Awareness Checker

## 1. Project Overview
The Phishing URL Awareness Checker is a Python-based
cybersecurity project that identifies common warning
signs in suspicious URLs.

## 2. Objectives
- Identify common phishing URL warning signs.
- Improve awareness about suspicious links.
- Help users understand URL-based risks.

## 3. Features
- Detects @ symbols in URLs.
- Checks unusually long URLs.
- Identifies IP address hostnames.
- Detects multiple hostname segments.
- Identifies punycode hostnames.
- Checks HTTP protocol usage.
- Supports multiple URL checking.

## 4. Technologies Used
- Programming Language: Python
- Editor: Visual Studio Code
- Libraries: re, urllib.parse

## 5. Requirements
- Python 3.10 or above.
- Windows operating system.

## 6. How to Run

1. Open the project in VS Code.
2. Open the terminal.
3. Execute:

python phishing_checker.py

## 7. Testing
Five sample URLs are used to test the application.
Test details are available in tests/test_samples.md.

## 8. Limitations
- Does not open or visit websites.
- Does not check domain reputation.
- Cannot guarantee that a URL is safe.

## 9. Ethical Use
This project is developed for educational purposes.
Use only the provided sample URLs for testing.

## 10. Conclusion
The project helps users recognize common phishing
warning signs by examining visible URL text.
