import os

# Replace 'directory_path' with the path to your directory containing the .txt files
directory_path = '/home/tony/Projects/machine-learning/computer-vision/hand-seal-detection/data/annotations/11'

# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory_path, filename)
        print(f"Processing {filename}...")
        
        # Read the contents of the file
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Modify the content (change the first character to '1')
        if content.startswith('0'):
            modified_content = '11' + content[1:]
            
            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.write(modified_content)
        
        print(f"{filename} has been updated.")
