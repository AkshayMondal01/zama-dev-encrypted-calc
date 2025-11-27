from concrete import fhe

def build_fhe_calculator():
    @fhe.compiler({"a": "encrypted", "b": "encrypted"})
    def add(a, b):
        return a + b

    @fhe.compiler({"a": "encrypted", "b": "encrypted"})
    def sub(a, b):
        return a - b

    @fhe.compiler({"a": "encrypted", "b": "encrypted"})
    def mul(a, b):
        return a * b

    return add, sub, mul


if __name__ == "__main__":
    add, sub, mul = build_fhe_calculator()

    print("🛡️ Fully Homomorphic Encrypted Calculator (Zama Dev Project)")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("\nEncrypting inputs...")
    add_circ = add.compile({"a": a, "b": b})
    sub_circ = sub.compile({"a": a, "b": b})
    mul_circ = mul.compile({"a": a, "b": b})

    print("\nResults:")
    print("Encrypted Add Result:", add_circ.run({"a": a, "b": b}))
    print("Encrypted Sub Result:", sub_circ.run({"a": a, "b": b}))
    print("Encrypted Mul Result:", mul_circ.run({"a": a, "b": b}))
