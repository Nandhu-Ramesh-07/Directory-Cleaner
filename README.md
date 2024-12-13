# Directory Cleaner

Directory Cleaner is a Python tool that helps you clean up files and folders in a directory based on your specifications. It allows you to delete files of a certain type (e.g., PDFs) or even delete entire folders within a directory.

## Features
- Delete files of a specific type (e.g., PDFs, text files, etc.).
- Delete all folders inside a specified directory.
- Safe deletion with a confirmation prompt before proceeding.

## Installation

To use **Directory Cleaner**, you need to clone the repository and install its dependencies.

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/directory-cleaner.git
   cd directory-cleaner
   ```

2. Install required dependencies (if any):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Import the Function

After setting up the project, you can use the cleaning function in your Python script. You will need to import it as shown below:

```python
from residual_cleaner import cleaner
```

### Clean Files or Folders

You can call the `cleaner()` function with the following options:

- **Delete files of a specific type** (e.g., PDF files).
- **Delete entire folders** inside the directory.

#### Example Usage

```python
from residual_cleaner import cleaner

# Specify the directory you want to clean
directory = '/path/to/your/directory'

# Delete all PDF files in the directory
cleaner(directory=directory, kind='pdf')

# Delete all folders inside the directory
cleaner(directory=directory, kind='entire')
```

### Parameters
- **`kind`**: Specifies what to delete.
  - `kind='pdf'`: Deletes all `.pdf` files in the directory.
  - `kind='entire'`: Deletes all folders inside the directory.
- **`directory`**: The path to the directory you want to clean.

### Warning

Before deleting any files or folders, you will be prompted to confirm the action. A message will be displayed asking for a `yes` or `no` response to proceed with the deletion. 

```bash
Warning: This will delete all files/folders. Are you sure? (yes/no)
```

Type `yes` to proceed, or `no` to cancel.

