import os

def create_research_skeleton():
    # Core directories based on your 52-week roadmap
    directories = [
        "journals",          # Daily research logs (The "Golden Rule")
        "notebooks",         # Jupyter Math Labs (Calculus/Linear Algebra)
        "src/crypto",        # Phase 1: Modular Crypto Toolkit
        "src/data_engine",   # Phase 2: Cyber-Data Insights Engine
        "src/ml_security",   # Phase 3/4: Phishing Sentinel & NID-ML
        "docs/proofs",       # LaTeX mathematical proofs for your portfolio
        "data/raw_logs",     # For firewall/network datasets
        "data/processed"     # For cleaned research data
    ]
    
    # Fundamental files to initialize the project
    files = {
        "app.py": "# Main Streamlit Dashboard Entry Point\n",
        "roadmap.json": "{}", 
        "requirements.txt": "streamlit\npandas\nmatplotlib\nscikit-learn\nscapy\n",
        "README.md": "# Cybersecurity Master's & PhD Research Portfolio\n"
    }
    
    # Create folders
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"📁 Created directory: {directory}")

    # Create initial files
    for filename, content in files.items():
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write(content)
            print(f"📄 Created file: {filename}")

if __name__ == "__main__":
    create_research_skeleton()
    print("\n✅ Step 1 Complete: Research skeleton is ready.")