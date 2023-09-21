#!/usr/bin/env python3
import os
import re
from prompt_toolkit import prompt
from cc_generate import typescript, python, rust, go
from cc_generate.prompt_widgets import checkboxlist_dialog

def get_language_selection():
    """Prompt the user to select languages for initialization."""
    return checkboxlist_dialog(
        title="Which languages/packages would you like to initialize?",
        values=[
            ('typescript', 'TypeScript'),
            ('rust', 'Rust'),
            ('python', 'Python'),
            ('go', 'Go'),
            ('pytorch', 'PyTorch')
        ],
        default_values=['typescript', 'rust', 'python']
        ).run()

def generate_folder_name(challenge_name, prefix_number):
    """Generate a folder name with a prefix number from the challenge name."""
    words = challenge_name.split()
    folder_suffix = '-'.join(words[:3]).lower()
    return f"{prefix_number:02}-{folder_suffix}"

def clean_description(description):
    """Strip blank line breaks and spaces from the description."""
    lines = description.split("\n")
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    return '\n'.join(cleaned_lines)

def get_next_prefix_number():
    """Get the next prefix number for the challenge folder."""
    existing_folders = [d for d in os.listdir() if os.path.isdir(d)]
    max_number = -1
    for folder in existing_folders:
        match = re.match(r'(\d+)-', folder)
        if match:
            max_number = max(max_number, int(match.group(1)))
    return max_number + 1

def create_challenge_folder_and_readme(challenge_name, challenge_description):
    """Create a new folder for the challenge and a README inside it."""
    prefix_number = get_next_prefix_number()
    folder_name = generate_folder_name(challenge_name, prefix_number)
    
    # Create the folder
    os.makedirs(folder_name, exist_ok=True)
    
    # Create and write to the README.md file
    readme_path = os.path.join(folder_name, 'README.md')
    cleaned_desc = clean_description(challenge_description)
    with open(readme_path, 'w') as readme_file:
        readme_file.write(f"# {challenge_name}\n\n")
        readme_file.write(cleaned_desc)

    selected_languages = get_language_selection()

    if 'typescript' in selected_languages:
        typescript.setup_typescript(folder_name)
    if 'rust' in selected_languages:
        rust.setup_rust(folder_name)
    if 'python' in selected_languages:
        python.setup_python(folder_name)
    if 'go' in selected_languages:
        go.setup_go(folder_name)
    if "pytorch" in selected_languages:
        print ("generating pytorch")

def main():
    # Ask the user for a challenge name and description
    challenge_name = prompt("Enter the challenge name: ").strip()
    challenge_description = prompt("Enter the challenge description (press 'ESC' followed by 'Enter' to finish):\n", multiline=True)
    
    # Create challenge folder and README
    create_challenge_folder_and_readme(challenge_name, challenge_description)
    
    # Print success message
    print(f"\nChallenge folder and README created for '{challenge_name}'.")

if __name__ == "__main__":
    main()
