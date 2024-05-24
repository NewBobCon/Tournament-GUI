from tkinter import *
from tkinter import ttk

const ={
    "rWidth": 1000,
    "rHeight": 700
}

def Setup(root: Tk):
    root.title("Tourney Manager")
    root.geometry(f"{const['rWidth']}x{const['rHeight']}")

    parent = ttk.Frame(root)
    parent.pack(expand=True, fill=BOTH)
    
    cnvs = Canvas(parent)
    cnvs.pack(side=LEFT, expand=True, fill=BOTH)

    scrollbar = ttk.Scrollbar(parent, orient="vertical", command=cnvs.yview)
    cnvs.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)

    frm = ttk.Frame(cnvs, padding=10)
    frm.grid()
    frm.grid_columnconfigure(0, weight=1)
    frm.grid_columnconfigure(1, weight=1)
    window_id = cnvs.create_window(0, 0, window=frm)

    # Center the frame in the canvas
    def center_frame(event):
        center_x = event.width // 2
        center_y = (event.height * 4) // 5 
        cnvs.coords(window_id, center_x, center_y)

    cnvs.bind("<Configure>", center_frame)

    # Create label
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
        
    validate_cmd = root.register(validate_num_input)
    num_input = StringVar()
    ttk.Entry(frm, textvariable=num_input, validate="key", validatecommand=(validate_cmd, '%P')).grid(column=1, row=0)

    #Create button
    ttk.Button(frm, text="Create Bracket").grid(column=0, row=1, columnspan=2, sticky="ew", pady=(10, 0))


def create_bracket(cnvs: Canvas, num_competitors: int):
    pass


if __name__ == "__main__":
    root = Tk()
    Setup(root)
    root.mainloop()