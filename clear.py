import os
import shutil


def clear_and_create_directory(directory_path):
    # Check if the directory exists
    if os.path.exists(directory_path):
        # Clear the directory by removing all its contents
        shutil.rmtree(directory_path)

    # Create a new empty directory
    os.makedirs(directory_path)


# Specify the directory path
directory_path = "C:/website_content"

# Call the function to clear and create the directory
clear_and_create_directory(directory_path)

print("Cleared and created the directory:", directory_path)
