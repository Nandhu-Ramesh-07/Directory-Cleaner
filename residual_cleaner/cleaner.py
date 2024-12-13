import os
import shutil
import logging

# Set up logging
logging.basicConfig(
    filename="deletion_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def confirm_deletion(directory, kind):
    """Prompt user for confirmation before deleting files."""
    if kind == "entire":
        print(f"Warning: This will delete all files and folders in {directory}.")
    else:
        print(f"Warning: This will delete all *.{kind} files in {directory}.")
    
    confirmation = input("Are you sure you want to proceed? (yes/y to confirm): ").strip().lower()
    if confirmation not in ['yes', 'y']:
        print("Operation cancelled.")
        return False
    return True

def cleaner(kind, directory):
    """Delete files or entire contents of the directory based on the specified kind."""
    try:
        # Proceed only if the user confirms the action
        if not confirm_deletion(directory, kind):
            return

        if kind == "entire":
            # Delete all files and folders
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                    print(f"Deleted file: {item_path}")
                    logging.info(f"Deleted file: {item_path}")
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    print(f"Deleted folder: {item_path}")
                    logging.info(f"Deleted folder: {item_path}")
        else:
            # Delete only files with the specified extension
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isfile(item_path) and item.endswith(f".{kind}"):
                    os.remove(item_path)
                    print(f"Deleted file: {item_path}")
                    logging.info(f"Deleted file: {item_path}")
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Error: {e}")
