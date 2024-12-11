import os
import ast

def parse_models(project_path):
    models = {}
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file == "models.py":
                with open(os.path.join(root, file), "r") as f:
                    tree = ast.parse(f.read())
                    for node in ast.walk(tree):
                        if isinstance(node, ast.ClassDef):
                            models[node.name] = [n.arg for n in node.decorator_list]
    return models

def detect_n_plus_one(project_path):
    issues = []
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r") as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if "for" in line and ".objects." in lines[i + 1]:
                            issues.append((file, i + 1, line.strip()))
    return issues

if __name__ == "__main__":
    project_path = os.getcwd()
    models = parse_models(project_path)
    issues = detect_n_plus_one(project_path)

    print("Models Detected:")
    print(models)
    print("\nN+1 Issues Detected:")
    for issue in issues:
        print(f"File: {issue[0]}, Line: {issue[1]}, Code: {issue[2]}")
