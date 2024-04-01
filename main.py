import os
import time
from send2trash import send2trash

def delete_files(directory, file_size_limit, days_old, extensions_to_keep=None):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            # Check if the file has the correct extension
            if extensions_to_keep is None or not filename.endswith(tuple(extensions_to_keep)):
                file_size = os.path.getsize(file_path)
                # Convert file size to megabytes
                file_size = file_size / (1024 * 1024)
                # Get the time since the file was last modified
                modified_time = os.path.getmtime(file_path)
                # Get the current time
                current_time = time.time()
                # Calculate the age of the file in days
                file_age = (current_time - modified_time) / (24*60*60)
                # If the file is older than the specified number of days and its size is less than the limit
                if file_age > days_old and file_size < file_size_limit:
                    send2trash(file_path)
                    print(f"Moved {file_path} to the recycle bin")

# Remove all files in the recycle bin older than 14 days
delete_files(r'C:\$Recycle.Bin', float('inf'), 14)

# Remove all files in the downloads directory under 'inf' MB except for .pdf, .mkv, and .mp4 files
delete_files(r'C:\Users\warre\Downloads', float('inf'), 0, ['.pdf', '.mkv', '.mp4'])
