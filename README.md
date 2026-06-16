# 🔐 Caesar Cipher Encryption & Decryption Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

A professional Python implementation of the **Caesar Cipher Algorithm** that allows users to securely encrypt and decrypt messages using a customizable shift value. This project demonstrates fundamental cryptographic concepts, string manipulation techniques, and user interaction in Python.

---

## 📖 Overview

The Caesar Cipher is one of the earliest and simplest encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions in the alphabet.

### Example

| Original Text | Shift | Encrypted Text |
| ------------- | ----- | -------------- |
| HELLO WORLD   | 3     | KHOOR ZRUOG    |

---

## ✨ Features

✔ Encrypt text using a user-defined shift value
✔ Decrypt encrypted text back to its original form
✔ Supports both uppercase and lowercase letters
✔ Preserves spaces, numbers, and special characters
✔ Simple command-line interface (CLI)
✔ Easy-to-understand and beginner-friendly implementation

---

## 🛠 Technologies Used

* Python 3.x
* No Python Libraries needed

---

## 📂 Project Structure

```text
Caesar-Cipher/
│
├── caesar_cipher.py
├── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed on your system.

```bash
python --version
```

or

```bash
python3 --version
```

---

### Installation

1. Clone the repository:

```bash
git clone https://github.com/eanbarasan05/PRODIGY_CS_01.git
```

2. Navigate to the project directory:

```bash
cd Caesar-Cipher
```

3. Run the program:

```bash
python caesar_cipher.py
```

---

## ▶ Usage

### Encrypt a Message

```text
Enter the message: HELLO WORLD
Enter the shift value: 3

Choose an option:
1. Encrypt
2. Decrypt

Enter your choice: 1

Encrypted Message: KHOOR ZRUOG
```

### Decrypt a Message

```text
Enter the message: KHOOR ZRUOG
Enter the shift value: 3

Choose an option:
1. Encrypt
2. Decrypt

Enter your choice: 2

Decrypted Message: HELLO WORLD
```

---

## 🔍 Algorithm Workflow

```text
Start
  │
  ▼
Input Message
  │
  ▼
Input Shift Value
  │
  ▼
Choose Operation
(Encrypt / Decrypt)
  │
  ▼
Shift Characters
According to Value
  │
  ▼
Display Result
  │
  ▼
End
```

---

## 🧠 How Caesar Cipher Works

For each character:

1. Identify its alphabetical position.
2. Shift the character by the specified value.
3. Wrap around the alphabet if necessary.
4. Preserve non-alphabetic characters.

Example:

```text
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

Shift Value = 3

---

## 📈 Learning Outcomes

This project helps in understanding:

* Basic Cryptography Concepts
* Encryption and Decryption Techniques
* ASCII Character Manipulation
* Python Functions
* Conditional Statements
* User Input Handling
* Modular Programming

---

## 🔒 Security Note

The Caesar Cipher is intended for educational purposes only. It is not secure for modern communication because it can be easily broken using brute-force attacks and frequency analysis.

---

## 🎯 Future Enhancements

* Graphical User Interface (GUI)
* File Encryption Support
* Brute Force Attack Demonstration
* Multiple Cipher Algorithms
* Web-Based Implementation

---

## 👨‍💻 Author

**ANBARASAN E - Cyber Security Intern @ Prodigy Infotech**

---
## Internship

This project was completed as part of the Prodigy Infotech Cyber Security Internship.


#Prodigy Infotech #Internship #CyberSecurity #Python #Cryptograpy
