from tkinter import *
from tkinter import ttk

#Constants dictionary
const ={
    "rWidth": 1000, # Width of the root window
    "rHeight": 700 # Height of the root window
}

def Setup(root: Tk):
    # Setting up title and dimensions of the window
    root.title("Tourney Manager")
    root.geometry(f"{const['rWidth']}x{const['rHeight']}")

    # Create parent frame inside root window and make it expandable while filling the entire root
    parent = ttk.Frame(root)
    parent.pack(expand=True, fill=BOTH)
    
    # Create a canvas inside the parent and make it expandable while filling the entire parent
    cnvs = Canvas(parent)
    cnvs.pack(side=LEFT, expand=True, fill=BOTH)

    # Create a scrollbar for the canvas
    scrollbar = ttk.Scrollbar(parent, orient="vertical", command=cnvs.yview)
    cnvs.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Create a frame inside the canvas
    frm = ttk.Frame(cnvs, padding=10)
    frm.grid()
    # Configure the grid to distribute space equally
    frm.grid_columnconfigure(0, weight=1)
    frm.grid_columnconfigure(1, weight=1)
    # Add the frame to the canvas
    window_id = cnvs.create_window(0, 0, window=frm)

    # Center the frame in the canvas
    def center_frame(event):
        center_x = event.width // 2
        center_y = (event.height * 4) // 5 
        cnvs.coords(window_id, center_x, center_y)

    # Binds the center_frame function to the canvas
    cnvs.bind("<Configure>", center_frame)

    # Create "Number of Competitors" label
    ttk.Label(frm, text="Number of Competitors:").grid(column=0, row=0, padx=(0, 10))

    # Validate that text input is numerical
    def validate_num_input(input):
        if input == "":
            return True
        try:
            int(input)
            return True
        except ValueError:
            return False
        
    # Create text input for number of competitors
    validate_cmd = root.register(validate_num_input)
    num_input = StringVar()
    ttk.Entry(frm, textvariable=num_input, validate="key", validatecommand=(validate_cmd, '%P')).grid(column=1, row=0)

    # Create button
    ttk.Button(frm, text="Create Bracket").grid(column=0, row=1, columnspan=2, sticky="ew", pady=(10, 0))

# Function to create a bracket
def create_bracket(cnvs: Canvas, num_competitors: int):
    pass

# Main function
if __name__ == "__main__":
    root = Tk()
    Setup(root)
    root.mainloop()