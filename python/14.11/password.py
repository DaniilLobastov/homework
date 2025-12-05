from random import choice

digits = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'


def generate_password(length, use_digits=True, use_upper=True, use_lower=True, use_punct=True):
    chars = ''
    if use_digits: chars += digits
    if use_upper: chars += uppercase
    if use_lower: chars += lowercase
    if use_punct: chars += punctuation
    return ''.join(choice(chars) for _ in range(length))


def check(password):
    score = 0
    if len(password) >= 8: score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c in punctuation for c in password): score += 1

    if score <= 2: return "Слабый"
    if score == 3: return "Средний"
    return "Сильный"

def passwords(count, length, **kwargs):
    passwords = set()
    while len(passwords) < count:
        passwords.add(generate_password(length, **kwargs))
    return list(passwords)

length = int(input("Введите длину пароля: "))
password = generate_password(length)
print(f"Пароль: {password}")
print(f"Надёжность: {check(password)}")
