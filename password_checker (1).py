"""Проверка надёжности пароля: оценка от 0 до 100."""

from __future__ import annotations

import re

MIN_LENGTH = 8

# Небольшой список самых популярных паролей (можно расширять)
COMMON_PASSWORDS = {
    "password", "password1", "12345678", "123456789", "1234567890",
    "qwerty123", "qwertyui", "iloveyou", "admin123", "letmein123",
    "11111111", "00000000", "abc12345", "пароль123", "йцукен123",
}

# Последовательности символов, которые легко угадать
SEQUENCES = [
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "qwertyuiop", "asdfghjkl", "zxcvbnm",
    "йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю",
]


def has_sequence(password: str, length: int = 3) -> bool:
    """Ищет в пароле куски вроде abc, 123, qwe (и в обратном порядке)."""
    p = password.lower()
    for seq in SEQUENCES:
        for s in (seq, seq[::-1]):
            for i in range(len(s) - length + 1):
                if s[i:i + length] in p:
                    return True
    return False


def evaluate_password(password: str) -> tuple[int, list[str]]:
    """Возвращает (оценка 0-100, список советов)."""
    tips = []

    # 1. Длина: до 40 баллов (максимум достигается на 16+ символах)
    length_score = min(len(password), 16) / 16 * 40
    if len(password) < 12:
        tips.append("Сделайте пароль длиннее (лучше 12+ символов)")

    # 2. Разнообразие символов: до 40 баллов (по 10 за каждый тип)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    variety_score = 10 * (has_lower + has_upper + has_digit + has_special)
    if not has_lower:
        tips.append("Добавьте строчные буквы")
    if not has_upper:
        tips.append("Добавьте заглавные буквы")
    if not has_digit:
        tips.append("Добавьте цифры")
    if not has_special:
        tips.append("Добавьте спецсимволы (!@#$%^&* и т.д.)")

    # 3. Уникальность символов: до 20 баллов
    unique_score = len(set(password)) / len(password) * 20

    score = length_score + variety_score + unique_score

    # Штрафы
    if re.search(r"(.)\1{2,}", password):
        score -= 15
        tips.append("Избегайте повторов вроде «aaa» или «111»")

    if has_sequence(password):
        score -= 15
        tips.append("Избегайте последовательностей вроде «abc», «123», «qwerty»")

    if password.isalpha() or password.isdigit():
        score -= 10

    if password.lower() in COMMON_PASSWORDS:
        score = min(score, 5)
        tips.append("Это один из самых популярных паролей, его взломают мгновенно")

    return max(0, min(100, round(score))), tips


def get_label(score: int) -> str:
    if score < 30:
        return "Очень слабый"
    if score < 50:
        return "Слабый"
    if score < 70:
        return "Средний"
    if score < 85:
        return "Хороший"
    return "Отличный"


def main():
    print("=== Проверка надёжности пароля ===")
    print(f"Минимальная длина: {MIN_LENGTH} символов. Для выхода введите 'q'.\n")

    while True:
        password = input("Введите пароль: ")

        if password.lower() == "q":
            print("До встречи!")
            break

        if len(password) < MIN_LENGTH:
            print(f"Пароль слишком короткий: нужно минимум {MIN_LENGTH} символов "
                  f"(сейчас {len(password)}).\n")
            continue

        score, tips = evaluate_password(password)
        print(f"\nНадёжность: {score}/100 ({get_label(score)})")

        if tips:
            print("Советы:")
            for tip in tips:
                print(f"  - {tip}")
        print()


if __name__ == "__main__":
    main()
