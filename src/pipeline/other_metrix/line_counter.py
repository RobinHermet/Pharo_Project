import os

def count_lines_of_code_and_comments(file_path):
    code_lines = 0
    comment_lines = 0
    in_block_comment = False
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line.startswith('/*'):
                in_block_comment = True
                comment_lines += 1
            elif stripped_line.endswith('*/'):
                in_block_comment = False
                comment_lines += 1
            elif in_block_comment or stripped_line.startswith('//'):
                comment_lines += 1
            elif stripped_line != '':
                code_lines += 1
    
    return code_lines, comment_lines

def analyze_typescript_project(directory_path):
    print(directory_path)
    total_code_lines = 0
    total_comment_lines = 0
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.ts') and not file.endswith('.d.ts'):
                code_lines, comment_lines = count_lines_of_code_and_comments(os.path.join(root, file))
                # Ajoute seulement si le fichier contient au moins une ligne de code
                if code_lines > 0:
                    total_code_lines += code_lines
                    total_comment_lines += comment_lines
    return total_code_lines, total_comment_lines
