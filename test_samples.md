
# Phishing URL Awareness Checker - Test Results

## Test Cases

### Test 1
URL: https://www.example.com/login

Expected Result:
No listed warning signs found.

### Test 2
URL: http://192.0.2.10/account

Expected Result:
- IP address warning
- HTTP warning

### Test 3
URL: http://example.com@sample.invalid/login

Expected Result:
- @ symbol warning
- HTTP warning

### Test 4
URL: https://a.b.c.d.e.example.invalid/path

Expected Result:
Many hostname segments warning.

### Test 5
URL: https://xn--example.invalid/

Expected Result:
Punycode hostname warning.

## Test Environment

- Programming Language: Python
- Operating System: Windows
- Python Version: Enter your installed version
- Test Date: Enter the actual date

## Actual Results

Run all five test cases in your Python program.

Record the actual output and mark each test PASS or FAIL.

## Actual Test Results

| Test | Expected Result | Actual Result | Status |
|---|---|---|---|
| 1 | No listed warnings | Enter actual output | PASS/FAIL |
| 2 | IP address and HTTP warnings | Enter actual output | PASS/FAIL |
| 3 | @ symbol and HTTP warnings | Enter actual output | PASS/FAIL |
| 4 | Many hostname segments warning | Enter actual output | PASS/FAIL |
| 5 | Punycode warning | Enter actual output | PASS/FAIL |
