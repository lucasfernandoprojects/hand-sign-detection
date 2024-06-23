import os

def rename_images(directory, new_names):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a directory.")
        return
    
    # Get the list of image files in the directory
    image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    if not image_files:
        print(f"No image files found in {directory}.")
        return
    
    if len(image_files) != len(new_names):
        print("Error: Number of images doesn't match the number of specified names.")
        return
    
    # Rename the images
    for i, image_file in enumerate(image_files):
        original_path = os.path.join(directory, image_file)
        new_name = new_names[i]
        _, extension = os.path.splitext(image_file)
        new_path = os.path.join(directory, new_name + extension)
        
        try:
            os.rename(original_path, new_path)
            print(f"Renamed {original_path} to {new_path}")
        except Exception as e:
            print(f"Error renaming {original_path} to {new_path}: {e}")

# Example usage
if __name__ == "__main__":
    directory = "/home/tony/Projects/machine-learning/computer-vision/hand-sign-detection/data/0"
    new_names = list()
    for i in range(0, 100, 1):
        new_names.append(str(i))
    rename_images(directory, new_names)
    