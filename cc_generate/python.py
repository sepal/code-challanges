# cc-generation/python_setup.py

import os
import subprocess

def init_venv(folder):
    # Create a virtual environment
    venv_path = os.path.join(folder, '.venv')
    subprocess.run(['python3', '-m', 'venv', venv_path], check=True)
    return venv_path
    


def setup_python(challenge_folder):
    """Set up the Python environment for the given challenge."""
    python_folder = os.path.join(challenge_folder, 'python')
    
    # 1. Create the Python subfolder
    os.makedirs(python_folder, exist_ok=True)
    
    # Activate the virtual environment for further commands
    init_venv(python_folder)

    # 3. Create a solution.py file for the solution
    with open(os.path.join(python_folder, 'solution.py'), 'w') as solution_file:
        solution_file.write("# Implement your solution here\n")

    # 4. Create a test_solution.py for unit testing
    with open(os.path.join(python_folder, 'test_solution.py'), 'w') as test_file:
        test_file.write("def test_solution():\n")
        test_file.write("    # Write your tests here\n")
        test_file.write("    pass\n")

def setup_pytorch(challenge_folder):
    """Set up the PyTorch environment for the given challenge."""
    pytorch_folder = os.path.join(challenge_folder, 'pytorch')
    
    # 1. Create the PyTorch subfolder
    os.makedirs(pytorch_folder, exist_ok=True)
    
    # 2. Create a virtual environment
    venv_path = init_venv(pytorch_folder)
    print(venv_path);
    
    # Activate the virtual environment for further commands
    python_exec = os.path.join(venv_path, 'bin', 'python3')

    # 3. Install PyTorch
    subprocess.run(f"{python_exec} -m pip install torch", shell=True, check=True)

    # 4. Create a solution.py file for the solution
    with open(os.path.join(pytorch_folder, 'solution.py'), 'w') as solution_file:
        solution_file.write("# Implement your solution here\n")

    # 5. Create a train.py file for training models
    with open(os.path.join(pytorch_folder, 'train.py'), 'w') as train_file:
        train_file.write("# Implement your training code here\n")