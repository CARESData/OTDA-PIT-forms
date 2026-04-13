
import tkinter as tk


def main_bye():
    # Create main window
    root = tk.Tk()
    root.title("Task Form")

    # Set form size
    window_width = 360
    window_height = 180

    # Get screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate centered position
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Apply size and centered position
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.resizable(False, False)

    # Main container
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill="both")

    # Centered label
    label = tk.Label(frame, text="I have completed this task", font=("Arial", 14))
    label.pack(expand=True)

    # Bottom-centered close button
    close_button = tk.Button(frame, text="Close", width=12, command=root.destroy)
    close_button.pack(side="bottom", pady=10)

    root.mainloop()

# main_bye()

