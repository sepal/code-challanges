# cc-generation/python_setup.py

import os
import subprocess

def setup_python(challenge_folder):
    """Set up the Python environment for the given challenge."""
    python_folder = os.path.join(challenge_folder, 'python')
    
    # 1. Create the Python subfolder
    os.makedirs(python_folder, exist_ok=True)
    
    # 2. Create a virtual environment
    venv_path = os.path.join(python_folder, 'venv')
    subprocess.run(['python3', '-m', 'venv', venv_path], check=True)
    
    # Activate the virtual environment for further commands
    activate_script = os.path.join(venv_path, 'bin', 'activate')
    activate_cmd = f"source {activate_script}"

    # 3. Create a solution.py file for the solution
    with open(os.path.join(python_folder, 'solution.py'), 'w') as solution_file:
        solution_file.write("# Implement your solution here\n")

    # 4. Create a test_solution.py for unit testing
    with open(os.path.join(python_folder, 'test_solution.py'), 'w') as test_file:
        test_file.write("def test_solution():\n")
        test_file.write("    # Write your tests here\n")
        test_file.write("    pass\n")
