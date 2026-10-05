Markdown


# Password Strength Checker

A lightweight, zero-dependency Python script designed to evaluate password security and strength on a comprehensive **0–100 scoring scale**.

---

## ⚡ Features

* **💯 0–100 Strength Score:** Evaluates overall security and categorizes it into clear labels (*Very Weak*, *Weak*, *Moderate*, *Good*, *Excellent*).
* **🔍 Multi-Factor Analysis:**
  * **Length & Diversity:** Checks for length (up to 16+ chars) and character types (uppercase, lowercase, digits, special characters, and support for Cyrillic).
  * **Uniqueness:** Measures unique character ratios to prevent low-entropy inputs.
  * **Pattern Detection:** Identifies simple keyboard and character sequences (e.g., `123`, `abc`, `qwerty`, `йцукен`) both forward and backward.
  * **Repetition Checks:** Penalizes consecutive repeated characters (e.g., `aaa`, `111`).
  * **Common Passwords Blacklist:** Instantly flags top weak/common passwords (e.g., `password123`, `12345678`).
* **💡 Actionable Tips:** Generates dynamic, personalized advice on how to improve the password.
* **🌐 Zero Dependencies:** Runs entirely on standard Python 3 libraries (`re`).

---

## 🚀 Quick Start

### Prerequisites
* Python **3.8+** installed.

### How to Run
Run the script directly via your terminal or IDE:

```bash
python password_checker.py
💻 Usage Example
Plaintext


=== Проверка надёжности пароля ===
Минимальная длина: 8 символов. Для выхода введите 'q'.

Введите пароль: Qwerty123

Надёжность: 28/100 (Очень слабый)
Советы:
  - Сделайте пароль длиннее (лучше 12+ символов)
  - Добавьте спецсимволы (!@#$%^&* и т.д.)
  - Избегайте последовательностей вроде «abc», «123», «qwerty»
