import os

def setup_go(challenge_folder):
    """Set up the Go environment for the given challenge."""
    go_folder = os.path.join(challenge_folder, 'go')
    
    # 1. Create the Go subfolder
    os.makedirs(go_folder, exist_ok=True)
    
    # 2. Generate a main.go for the solution
    with open(os.path.join(go_folder, 'main.go'), 'w') as go_file:
        go_file.write("package main\n\n")
        go_file.write("func main() {\n")
        go_file.write("    // Implement your solution here\n")
        go_file.write("}\n")

    # 3. Generate a main_test.go for testing the solution
    with open(os.path.join(go_folder, 'main_test.go'), 'w') as test_file:
        test_file.write("package main\n\n")
        test_file.write("import \"testing\"\n\n")
        test_file.write("func TestSolution(t *testing.T) {\n")
        test_file.write("    // Write your tests here\n")
        test_file.write("}\n")