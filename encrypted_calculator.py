from concrete import fhe

# ===================================================
#   FULLY HOMOMORPHIC ENCRYPTED CALCULATOR (Zama Dev)
# ===================================================

class EncryptedCalculator:
    def __init__(self):
        # Safe default configuration
        self.config = fhe.Configuration(
            enable_unsafe_features=False,
            insecure_key_cache=False
        )

    # -----------------------------------------------
    # Encryption / Decryption
    # -----------------------------------------------
    def encrypt(self, value):
        compiler = fhe.Compiler(lambda x: x, {"x": "encrypted"})
        self.circuit = compiler.compile([value], config=self.config)
        return self.circuit.encrypt(value)

    def decrypt(self, encrypted_value):
        return self.circuit.decrypt(encrypted_value)

    # -----------------------------------------------
    # Basic Math Operations (FHE SAFE)
    # -----------------------------------------------
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    # -----------------------------------------------
    # Division (integer-friendly FHE approximation)
    # -----------------------------------------------
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")

        # Approximated reciprocal for FHE
        reciprocal = int(10000 / b)
        return (a * reciprocal) // 10000

    # -----------------------------------------------
    # Power (Exponentiation)
    # -----------------------------------------------
    def power(self, base, exponent):
        result = 1
        for _ in range(exponent):
            result *= base
        return result


# ===================================================
#                     TEST RUN
# ===================================================

if __name__ == "__main__":
    calc = EncryptedCalculator()

    print("🛡️ Fully Homomorphic Encryption Calculator — Zama Project")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    ex = calc.encrypt(x)
    ey = calc.encrypt(y)

    print("\n🔒 Running encrypted operations...\n")

    add_result = calc.decrypt(calc.add(ex, ey))
    sub_result = calc.decrypt(calc.subtract(ex, ey))
    mul_result = calc.decrypt(calc.multiply(ex, ey))
    div_result = calc.decrypt(calc.divide(ex, ey))
    pow_result = calc.decrypt(calc.power(ex, 3))  # example: x³

    print("➕ Add:", add_result)
    print("➖ Sub:", sub_result)
    print("✖️ Mul:", mul_result)
    print("➗ Div:", div_result)
    print("🔼 Power (x³):", pow_result)
