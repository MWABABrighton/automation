import os
import shutil
import tkinter as tk
from tkinter import messagebox

# Function to move files to the 'Everything' folder
def move_files():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_name = "Everything"
    folder_path = os.path.join(desktop_path, folder_name)

    # Create the folder "Everything" if it doesn't exist
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # Move files from desktop to 'Everything'
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)

        # Skip the "Everything" folder itself
        if item_path == folder_path:
            continue

        # Move only files (not directories)
        if os.path.isfile(item_path):
            dest_path = os.path.join(folder_path, item)
            
            # Handle if the file already exists in the destination folder
            if os.path.exists(dest_path):
                base, extension = os.path.splitext(item)
                counter = 1
                new_file_name = f"{base}_{counter}{extension}"
                new_dest_path = os.path.join(folder_path, new_file_name)

                while os.path.exists(new_dest_path):
                    counter += 1
                    new_file_name = f"{base}_{counter}{extension}"
                    new_dest_path = os.path.join(folder_path, new_file_name)
                
                dest_path = new_dest_path

            shutil.move(item_path, dest_path)

    messagebox.showinfo("Success", "All files moved to 'Everything' folder on your desktop.")

# Create the GUI window
root = tk.Tk()
root.title("Move Files to Everything")
root.geometry("400x200")  # Window size
root.configure(bg='black')  # Set background to black

# Add a label to the window
label = tk.Label(root, text="Move all desktop files to 'Everything' folder", bg='black', fg='white', font=("Helvetica", 12))
label.pack(pady=20)

# Add a button to trigger the file move
move_button = tk.Button(root, text="Move Files", command=move_files, bg='white', fg='black', font=("Helvetica", 12), width=20)
move_button.pack(pady=20)

# Run the application
root.mainloop()
