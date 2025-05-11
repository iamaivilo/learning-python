import os
import shutil

# Source and destination paths
source = "basic_animate.py"
destination = "graphics/basic_animate.py"

# Create graphics directory if it doesn't exist
os.makedirs("graphics", exist_ok=True)

# Move the file
if os.path.exists(source):
    shutil.move(source, destination)
    print(f"Successfully moved {source} to {destination}")
else:
    print(f"Source file {source} not found") 