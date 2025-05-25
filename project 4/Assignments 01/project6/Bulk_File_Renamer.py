import os

def bulk_rename(folder_path, prefix="renamed_"):
    try:
        files = os.listdir(folder_path)
        for filename in files:
            old_path = os.path.join(folder_path, filename)
            if os.path.isfile(old_path):
                new_name = prefix + filename
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_name}")
        print("Renaming completed!")
    except Exception as e:
        print("Error:", e)

# Example usage:
folder = input("Enter the folder path: ")
bulk_rename(folder, prefix="new_")
