import random
import string


COMMON_WEAK_PASSWORDS = [
    "password",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "abc123",
    "letmein",
    "admin",
    "welcome",
]

WORDS = [
    "river",
    "cobalt",
    "lantern",
    "falcon",
    "cedar",
    "harbor",
    "quartz",
    "ember",
    "summit",
    "meadow",
    "anchor",
    "velvet",
]


def get_valid_int(prompt, min_val, max_val):
    """Safely read an integer within [min_val, max_val]."""
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit():
            value = int(user_input)
            if min_val <= value <= max_val:
                return value
        print(f"Please enter a valid number between {min_val} and {max_val}.")


def get_yes_no(prompt):
    """Safely read a y/n response from the user."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


def analyze_password(password):
    """Evaluate password strength and return (score, tips)."""
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    has_space = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch.isspace():
            has_space = True
        else:
            has_symbol = True

    score = 0
    tips = []
    length = len(password)

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        tips.append("Increase length to at least 8-12 characters.")

    if has_upper:
        score += 1
    else:
        tips.append("Add at least one uppercase letter (A-Z).")

    if has_lower:
        score += 1
    else:
        tips.append("Add at least one lowercase letter (a-z).")

    if has_digit:
        score += 1
    else:
        tips.append("Add at least one digit (0-9).")

    if has_symbol:
        score += 1
    else:
        tips.append("Add at least one symbol (e.g., !, @, #, $).")

    if password.lower() in COMMON_WEAK_PASSWORDS:
        score = max(0, score - 3)
        tips.append("Avoid common passwords like 'password' or '123456'.")

    if has_space:
        score = max(0, score - 1)
        tips.append("Be careful with spaces unless intentionally making a passphrase.")

    return score, tips


def get_strength_label(score):
    """Map numeric score (0-6) to a readable strength label."""
    if score <= 1:
        return "Very Weak"
    elif score <= 3:
        return "Weak"
    elif score <= 4:
        return "Strong"
    else:
        return "Very Strong"


def generate_password(length, use_upper, use_digits, use_symbols):
    """Generate a random password with guaranteed selected character types."""
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits
    symbol_chars = "!@#$%^&*()-_=+"

    required_chars = []
    pool = lowercase_chars

    # Always include at least one lowercase character as a base
    required_chars.append(random.choice(lowercase_chars))

    if use_upper:
        pool += uppercase_chars
        required_chars.append(random.choice(uppercase_chars))

    if use_digits:
        pool += digit_chars
        required_chars.append(random.choice(digit_chars))

    if use_symbols:
        pool += symbol_chars
        required_chars.append(random.choice(symbol_chars))

    if len(required_chars) > length:
        required_chars = required_chars[:length]

    remaining_count = length - len(required_chars)
    password_chars = required_chars[:]

    for _ in range(remaining_count):
        password_chars.append(random.choice(pool))

    random.shuffle(password_chars)
    return "".join(password_chars)


def generate_passphrase(word_count=4, add_number=True):
    """Generate a memorable word-based passphrase."""
    selected_words = [random.choice(WORDS).capitalize() for _ in range(word_count)]
    phrase = "-".join(selected_words)
    if add_number:
        number = random.randint(10, 99)
        phrase = f"{phrase}-{number}"
    return phrase


def run_analyzer():
    """Handle the password analysis flow."""
    print("\n--- Password Strength Analyzer ---")
    password = input("Enter a password to analyze: ")
    if not password:
        print("Password cannot be empty.")
        return

    score, tips = analyze_password(password)
    label = get_strength_label(score)

    print(f"Strength: {label} (Score: {score}/6)")
    if tips:
        print("Suggestions to improve:")
        for tip in tips:
            print(f"  - {tip}")
    else:
        print("Great password! It meets all strength checks.")


def run_generator():
    """Handle the custom password generation flow."""
    print("\n--- Custom Password Generator ---")
    length = get_valid_int("Password length (6-32): ", 6, 32)
    use_upper = get_yes_no("Include uppercase letters (y/n)? ")
    use_digits = get_yes_no("Include numbers (y/n)? ")
    use_symbols = get_yes_no("Include symbols (y/n)? ")

    password = generate_password(length, use_upper, use_digits, use_symbols)
    score, _ = analyze_password(password)
    label = get_strength_label(score)

    print(f"\nGenerated Password: {password}")
    print(f"Strength Rating:    {label} ({score}/6)")


def run_passphrase_generator():
    """Handle the passphrase generation flow."""
    print("\n--- Memorable Passphrase Generator ---")
    word_count = get_valid_int("How many words (3-6)? ", 3, 6)
    add_number = get_yes_no("Add a 2-digit number at the end (y/n)? ")

    phrase = generate_passphrase(word_count, add_number)
    print(f"\nGenerated Passphrase: {phrase}")


def main():
    """Main menu loop."""
    print("=========================================")
    print("  Password & Strength Analyzer Toolkit")
    print("=========================================")

    while True:
        print("\nChoose an option:")
        print("1. Analyze a password")
        print("2. Generate a custom password")
        print("3. Generate a memorable passphrase")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            run_analyzer()
        elif choice == "2":
            run_generator()
        elif choice == "3":
            run_passphrase_generator()
        elif choice == "4":
            print("Goodbye! Stay safe online.")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()