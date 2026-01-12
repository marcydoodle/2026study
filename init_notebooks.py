import nbformat as nbf
import os

def create_math_lab():
    nb = nbf.v4.new_notebook()
    
    # Research Header
    header = """# 🔬 Cyber-Math Research Lab: Week 01
## Focus: Algebra Foundations & Security Variables
**The Golden Rule:** Documenting the relationship between mathematical logic and computational security."""
    
    # LaTeX Math Cell (PhD Standard)
    math_cell = """### 🔢 Mathematical Proof: Order of Operations
In cryptography, the order of operations ensures that decryption is the perfect inverse of encryption. 
Consider the expression for a simple shift:
$$ C = (P + K) \pmod{26} $$
If the order of operations ($PEMDAS$) is not strictly followed by the algorithm, the integrity of the ciphertext is compromised."""

    # Python Code Cell
    code_cell = """# Verifying variable assignment for security strings
x = 5
y = "Secret_Key"
print(f"Variable {y} assigned value {x}")"""

    nb['cells'] = [
        nbf.v4.new_markdown_cell(header),
        nbf.v4.new_markdown_cell(math_cell),
        nbf.v4.new_code_cell(code_cell)
    ]

    # Save to the notebooks directory created in Step 1
    with open('notebooks/Week_01_Foundations.ipynb', 'w') as f:
        nbf.write(nb, f)
    
    print("✅ Created notebooks/Week_01_Foundations.ipynb")

if __name__ == "__main__":
    create_math_lab()