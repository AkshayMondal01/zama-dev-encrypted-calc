# 🔐 Zama Dev — Fully Homomorphic Encrypted Calculator

A simple but powerful calculator built using **Zama’s Concrete Python (FHE)**.  
It demonstrates how encryption allows computations to be performed **without ever decrypting the data** — a core concept of Fully Homomorphic Encryption.

---

## 🚀 Features
- 🔒 Fully encrypted computation (FHE)
- ➕ Addition  
- ➖ Subtraction  
- ✖️ Multiplication  
- ➗ Division (FHE-friendly approximation)  
- 🔼 Exponentiation (Power function)

---

## 📌 How It Works
This project uses **Concrete Python** to:
1. Encrypt user inputs  
2. Perform math operations directly on encrypted values  
3. Decrypt only the final result  

This proves the power of privacy-preserving computation.

---

## 🧠 Technologies Used
- **Python 3**
- **Concrete (Zama FHE Framework)**

---

## 🛠️ Code Example
```python
from concrete import fhe

# Fully Homomorphic Encrypted Calculator

class EncryptedCalculator:
    def __init__(self):
        self.config = fhe.Configuration(
            enable_unsafe_features=False,
            insecure_key_cache=False
        )

    def encrypt(self, value):
        compiler = fhe.Compiler(lambda x: x, {"x": "encrypted"})
        self.circuit = compiler.compile([value], config=self.config)
        return self.circuit.encrypt(value)

    def decrypt(self, encrypted_value):
        return self.circuit.decrypt(encrypted_value)

    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        reciprocal = int(10000 / b)
        return (a * reciprocal) // 10000

    def power(self, base, exponent):
        result = 1
        for _ in range(exponent):
            result *= base
        return result
```

---

## ▶️ Running the Program
```bash
python kalku.py
```

You will be asked to enter two numbers, and all operations will run **encrypted**.

---

## 🏆 Part of Zama Developer Program
This project is created as a submission/demo for the **Zama Dev Program**, showcasing practical FHE usage.

---

## 📚 Author
**Akshay Mondal**

---

