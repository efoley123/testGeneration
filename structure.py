import os
import subprocess
from pathlib import Path

class RepoStructure:
    def __init__(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        
        self.startpath = current_path
        self.max_depth = 4  # Change this value to limit depth
        self.file_extensions = [
            '.py',   # Python files
            '.js',   # JavaScript files
            '.java', # Java files
            '.c',    # C files
            '.cpp',  # C++ files
            '.h',    # C/C++ header files
            '.rb',   # Ruby files
            '.go',   # Go files
            '.md',   # Markdown files for documentation
            '.txt',  # Text files (optional)
            'Dockerfile', # Dockerfile for environment context
            'requirements.txt', # Python dependencies
            'Pipfile', # Python dependency management
            'package.json', # JavaScript dependencies
            # Add any other specific file names or extensions you want to include
        ]
    def get_repo_path():
        try:
            repo_path = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).strip().decode('utf-8')
            return repo_path
        except subprocess.CalledProcessError:
            print("Not a Git repository.")
            return None

    def list_files(self):
        # (startpath, max_depth, file_extensions)
        structure = ""
        for root, dirs, files in os.walk(self.startpath):
            # Ignore the '.github' directory
            if ('.github' in root.split(os.sep)) or  ('.git' in root.split(os.sep)) :
                continue
            
            level = root.replace(self.startpath, '').count(os.sep)
            if level > self.max_depth:  # Limit the depth
                continue
            indent = ' ' * 4 * level
            structure += f'{indent}{os.path.basename(root)}/\n'
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                if any(file.endswith(ext) for ext in self.file_extensions):  # Filter by extensions
                    structure += f'{subindent}{file}\n'
        return structure


if __name__ == '__main__':

    current_path = os.path.dirname(os.path.abspath(__file__))

    base_name = str(Path("tinydb/storages.py")).split(".")
    val = base_name[0].replace(str(current_path),'')
    val = val.replace('/','.')
    
    print("module_path = "+ val+"\n")

    current_path = str(os.path.dirname(os.path.abspath(__file__)))
    
    current_path = str(os.path.dirname(os.path.abspath(__file__))) + "/"
    print("current path is "+ current_path+ "\n")

    file_name = "tinydb/storage.py"
    base_name = Path(file_name).resolve()
    print("step "+ str(base_name)+"\n")
    base_name = str(base_name).replace(current_path,'').replace('/', '.') 
    print("step "+ base_name+"\n")
    base_name = base_name.replace(file_name,"")

    print("module_path = "+ base_name+"\n")

    file_name = "calculator.py"
    base_name = Path(file_name).resolve()
    base_name = str(base_name).replace(current_path,'').replace('/', '.') 
    base_name = base_name.replace(file_name,"")

    print("module_path = "+ base_name+"\n")

    
    
    
    # repo_path = current_path
    # max_depth = 4  # Change this value to limit depth
    # file_extensions = [
    #     '.py',   # Python files
    #     '.js',   # JavaScript files
    #     '.java', # Java files
    #     '.c',    # C files
    #     '.cpp',  # C++ files
    #     '.h',    # C/C++ header files
    #     '.rb',   # Ruby files
    #     '.go',   # Go files
    #     '.md',   # Markdown files for documentation
    #     '.txt',  # Text files (optional)
    #     'Dockerfile', # Dockerfile for environment context
    #     'requirements.txt', # Python dependencies
    #     'Pipfile', # Python dependency management
    #     'package.json', # JavaScript dependencies
    #     # Add any other specific file names or extensions you want to include
    # ]
    # test = RepoStructure()
    # structure = test.list_files()
    # print(structure)
    #print('Filtered repository structure saved to repo_structure.txt\n')

    