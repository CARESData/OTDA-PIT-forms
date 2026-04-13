import tkinter as tk
from tkinter import filedialog
from pathlib import Path



def center_window(window: tk.Tk, width: int, height: int) -> None:
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_pos = (screen_width - width) // 2
    y_pos = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x_pos}+{y_pos}")


def browse_folder(entry_widget: tk.Entry) -> None:
    folder = filedialog.askdirectory(
        title="Select Folder",
        initialdir=Path.cwd()   
    )

    if folder:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, folder)


def submit(root: tk.Tk, first_entry: tk.Entry, second_entry: tk.Entry) -> None:
    # global awards_folder
    global excel_folder
    global awards_folder
    
    awards_folder = first_entry.get()
    excel_folder = second_entry.get()

    
    print(f"Selected AWARDS folder: {awards_folder}")
    print(f"Selected Excel folder: {excel_folder}") 
    

    root.destroy()

def awards_file():
    return awards_folder

def excel_file():
    return excel_folder

def main() -> None:    
    root = tk.Tk()
    root.title("Folder Selection")
    center_window(root, 560, 340)

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(fill="both", expand=True)

    # First folder selector
    label1 = tk.Label(frame, text="Select folder for AWARDS Data")
    label1.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 6))

    entry1 = tk.Entry(frame, width=55)
    entry1.insert(0, "D:\\Data Source\\PIT Numbers for OTDA by County\\Data")

    # entry1.grid(row=1, column=0, padx=(0, 10), pady=(0, 14))
    entry1.grid(row=1, column=0, padx=(0, 10), sticky="ew")

    button1 = tk.Button(frame, text="Browse", width=12, command=lambda: browse_folder(entry1))
    button1.grid(row=1, column=1, pady=(0, 14))

    # Second folder selector
    label2 = tk.Label(frame, text="Select folder holding the OTDA template")
    label2.grid(row=2, column=0, columnspan=2, sticky="w", pady=(0, 6))

    entry2 = tk.Entry(frame, width=55)
    entry2.insert(0, "D:\\Data Source\\PIT Numbers for OTDA by County\\OTDA Template" )
    entry2.grid(row=3, column=0, padx=(0, 10), sticky="ew")

    button2 = tk.Button(frame, text="Browse", width=12, command=lambda: browse_folder(entry2))
    button2.grid(row=3, column=1)

    # Push Submit to the bottom and keep three blank rows above it.
    frame.grid_rowconfigure(4, weight=1)
    spacer1 = tk.Label(frame, text="")
    spacer1.grid(row=5, column=0, columnspan=2)
    spacer2 = tk.Label(frame, text="")
    spacer2.grid(row=6, column=0, columnspan=2)
    spacer3 = tk.Label(frame, text="")
    spacer3.grid(row=7, column=0, columnspan=2)

    submit_button = tk.Button(
        frame,
        text="Submit",
        width=14,
        command=lambda: submit(root, entry1, entry2),
    )
    submit_button.grid(row=8, column=0, columnspan=2, pady=(8, 0))

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=0)

    root.mainloop()



# main()
