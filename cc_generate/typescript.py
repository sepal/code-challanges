# cc-generation/typescript.py

import os
import subprocess
import json

def setup_typescript(challenge_folder):
    """Set up the TypeScript environment for the given challenge."""
    ts_folder = os.path.join(challenge_folder, 'typescript')
    
    # Create the TypeScript subfolder
    os.makedirs(ts_folder, exist_ok=True)
    
    # Initialize a new Node.js project
    subprocess.run(['npm', 'init', '-y'], cwd=ts_folder, check=True)
    
    # Install TypeScript
    subprocess.run(['npm', 'install', 'typescript', '--save-dev'], cwd=ts_folder, check=True)
    
    # Install vitest
    subprocess.run(['npm', 'install', 'vitest', '--save-dev'], cwd=ts_folder, check=True)
    
    # Create a basic tsconfig.json
    tsconfig = {
        "compilerOptions": {
            "target": "es6",
            "module": "commonjs",
            "strict": True,
            "esModuleInterop": True
        },
        "include": ["src/*.ts"],
        "exclude": ["node_modules"]
    }

    with open(os.path.join(ts_folder, 'tsconfig.json'), 'w') as tsconfig_file:
        json.dump(tsconfig, tsconfig_file, indent=4)

    # Create src folder and an empty index.ts inside it
    src_folder = os.path.join(ts_folder, 'src')
    os.makedirs(src_folder, exist_ok=True)
    with open(os.path.join(src_folder, 'index.ts'), 'w') as index_file:
        index_file.write("// Implement your solution here\n")

    # Create an empty solution.test.ts for unit tests
    with open(os.path.join(src_folder, 'solution.test.ts'), 'w') as test_file:
        test_file.write("// Write your tests here\n")

    # Add "test": "vitest" to the scripts in package.json
    package_json_path = os.path.join(ts_folder, 'package.json')
    with open(package_json_path, 'r') as pkg_file:
        pkg_data = json.load(pkg_file)
    pkg_data['scripts']['test'] = 'vitest'
    with open(package_json_path, 'w') as pkg_file:
        json.dump(pkg_data, pkg_file, indent=2)
