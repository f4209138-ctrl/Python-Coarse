import random

def generate_password(length=12):
    if length < 3:
        raise ValueError("Length must be at least 3")
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]
    all_chars = lower + upper + digits
    chars += [random.choice(all_chars) for _ in range(length - 3)]
    random.shuffle(chars)
    return "".join(chars)

print(generate_password())