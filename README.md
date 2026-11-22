# Password & Strength Analyzer Toolkit

A command-line Python toolkit created for **Stanford's Code in Place X** that helps users evaluate password strength, generate customized passwords, and create memorable word-based passphrases.

## Features

- **Password Strength Analyzer:** Checks password length, character variety (uppercase, lowercase, digits, and symbols), spaces, and common weak passwords, then provides a strength rating along with improvement tips.
- **Custom Password Generator:** Generates random passwords of a user-selected length with optional uppercase letters, numbers, and symbols, while ensuring selected character types are included.
- **Memorable Passphrase Generator:** Creates easy-to-remember word-based passphrases with an optional two-digit number at the end.
- **Safe Input Validation:** Handles invalid menu choices, out-of-range numbers, and yes/no prompts cleanly without crashing.

## Project Structure

cip_final_project/
├── main.py
└── README.md

## How to Run

1. Make sure Python 3 is installed on your system.
2. Open a terminal in the project folder and run:

   python main.py

3. Follow the on-screen menu prompts (`1` to analyze a password, `2` to generate a custom password, `3` to generate a passphrase, or `4` to exit).

## Built With

- Python (using built-in `random` and `string` standard library modules)