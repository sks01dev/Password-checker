 # Password Checker 🔒

A Python script that helps you validate the strength of your password by checking if it’s commonly used. Avoiding common passwords is a key step in protecting yourself from brute-force attacks, and this tool makes it easy!


---

## 🚀 Features
- **Password Validation**: Checks if the password is among commonly used passwords.
- **Instant Feedback**: Informs if the password is common or unique.
- **Customizable Common Password List**: Easily add to the list in `passwords.txt`.

---

## 📋 Prerequisites
- Python 3.x installed on your machine.

---

## 🛠️ Getting Started

### 1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/password-checker.git
   cd password-checker
   ```

### 2. **Prepare `passwords.txt`**
   - Ensure `passwords.txt` is in the project directory, with each line containing a single common password.
   - If you don't have one, you can create it manually or find a downloadable list online.

### 3. **Run the Script**
   ```bash
   python check_password.py
   ```

### 4. **Enter Password**
   - You'll be prompted to enter a password for validation.
   - The script will instantly tell you if it's common or unique.

---

## 💻 Example Usage

### When a Password is Common:
```plaintext
Enter a password: 123456
123456: Common password found❌ (# 1)
```

### When a Password is Unique:
```plaintext
Enter a password: unique!pass123
unique!pass123: Unique password✅
```

---

## 📁 Project Structure

```plaintext
password-checker/
├── check_password.py      # Main script to run the password checker
├── passwords.txt          # List of common passwords
└── README.md              # Project documentation
```

- **check_password.py**: Contains the main logic for checking passwords.
- **passwords.txt**: Customizable file containing a list of common passwords.
- **README.md**: You are here!

---

## 🌟 How It Works

1. **Input**: Prompts the user to enter a password.
2. **Check**: Compares the entered password with entries in `passwords.txt`.
3. **Result**: Outputs whether the password is commonly used or unique.


---

## 🤝 Contributing

We welcome contributions! To contribute:

1. **Fork** the repository.
2. **Create a new branch** for your feature (`feature/your-feature`).
3. **Commit** your changes.
4. **Push** to the branch.
5. **Create a Pull Request**.


---
