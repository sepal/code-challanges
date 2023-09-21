# cc-generation/rust.py

import os
import subprocess

def setup_rust(challenge_folder):
    """Set up the Rust environment for the given challenge."""
    rust_folder = os.path.join(challenge_folder, 'rust')
    
    # 1. Create the Rust subfolder
    os.makedirs(rust_folder, exist_ok=True)
    
    # 2. Initialize a new Rust project
    subprocess.run(['cargo', 'init'], cwd=rust_folder, check=True)
    
    test_folder = os.path.join(rust_folder, 'tests')
    test_file_path = os.path.join(test_folder, 'solution_test.rs')
    os.makedirs(test_folder, exist_ok=True)

    with open(test_file_path, 'w') as test_file:
        test_file.write("#[cfg(test)]\nmod tests {\n    #[test]\n    fn test_solution() {\n        // Write your tests here\n    }\n}")
