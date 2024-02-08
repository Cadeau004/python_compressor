import os
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compressed_type):
    try:
        folder_name = os.path.basename(folder_path)
        current_date = datetime.now().strftime("%Y_%m_%d")
        compressed_filename = f"{folder_name}_{current_date}.{compressed_type}"

        if compressed_type == 'zip':
            with zipfile.ZipFile(compressed_filename, 'w') as zip_file:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, folder_path)
                        zip_file.write(file_path, arcname=arcname)

        elif compressed_type == 'tar':
            with tarfile.open(compressed_filename, 'w') as tar_file:
                tar_file.add(folder_path, arcname=os.path.basename(folder_path))

        elif compressed_type == 'tgz':
            with tarfile.open(compressed_filename, 'w:gz') as tar_file:
                tar_file.add(folder_path, arcname=os.path.basename(folder_path))

        print(f"Compression successful. File saved as: {compressed_filename}")
    except Exception as e:
        print(f"Compression failed. Error: {str(e)}")

def main():
    folder_path = input("Enter the path of the folder to compress: ")

    if not os.path.exists(folder_path):
        print("Error: The specified folder does not exist.")
        return

    compressed_types = ['zip', 'tar', 'tgz']
    print("Available compressed file types:")
    for idx, compressed_type in enumerate(compressed_types, start=1):
        print(f"{idx}. {compressed_type}")

    try:
        selected_index = int(input("Select the desired compressed file type (enter the corresponding number): ")) - 1
        selected_type = compressed_types[selected_index]

        compress_folder(folder_path, selected_type)
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
