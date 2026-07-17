# Password Strength Checker
DecodeLabs Cyber Security Internship - Project 1 (Batch 2026)

## Goal
A Python program that checks whether a password is Weak, Medium, or Strong.

## Features
- Length verification (minimum 8 characters - gatekeeper rule)
- Checks for uppercase letters, digits, and symbols using Python's any()
- Common leaked-password detection
- Improvement tips for weak passwords

## How to Run
python password_checker.py

## Test Results
| Input | Output |
|---|---|
| abc | WEAK (length fail) |
| abcdefgh | WEAK |
| abcdefg1 | MEDIUM |
| Abcdef1! | STRONG |

Screenshots of all test cases are included in this repository.
