
import tkinter as tk
from tkinter import messagebox
import re

def analyze_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Warning", "Please enter a password")
        return

    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    # Check common passwords
    common_passwords = [
        "password", "123456", "12345678",
        "qwerty", "admin"
    ]

    if password.lower() in common_passwords:
        score = 0
        suggestions.append("Avoid common passwords")

    # Display strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    result_label.config(
        text=f"Password Strength: {strength}"
    )

    if suggestions:
        suggestion_label.config(
            text="Suggestions:\n• " + "\n• ".join(suggestions)
        )
    else:
        suggestion_label.config(
            text="Good password characteristics!"
        )


# Create window
window = tk.Tk()
window.title("Password Strength Analyzer")
window.geometry("450x350")

title_label = tk.Label(
    window,
    text="Password Strength Analyzer",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=20)

password_entry = tk.Entry(
    window,
    width=35,
    show="*"
)
password_entry.pack(pady=10)

check_button = tk.Button(
    window,
    text="Check Password",
    command=analyze_password
)
check_button.pack(pady=10)

result_label = tk.Label(
    window,
    text="Password Strength: ",
    font=("Arial", 14)
)
result_label.pack(pady=10)

suggestion_label = tk.Label(
    window,
    text="",
    justify="left",
    wraplength=400
)
suggestion_label.pack(pady=10)

window.mainloop()