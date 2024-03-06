import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

elements = {
    1: {"symbol": "H", "name": "Hydrogen", "color": "sky blue"},
    2: {"symbol": "He", "name": "Helium", "color": "yellow"},
    3: {"symbol": "Li", "name": "Lithium", "color": "pink"},
    4: {"symbol": "Be", "name": "Beryllium", "color": "purple"},
    5: {"symbol": "B", "name": "Boron", "color": "light green"},
    6: {"symbol": "C", "name": "Carbon", "color": "sky blue"},
    7: {"symbol": "N", "name": "Nitrogen", "color": "sky blue"},
    8: {"symbol": "O", "name": "Oxygen", "color": "sky blue"},
    9: {"symbol": "F", "name": "Fluorine", "color": "yellow"},
    10: {"symbol": "Ne", "name": "Neon", "color": "yellow"},
    11: {"symbol": "Na", "name": "Sodium", "color": "pink"},
    12: {"symbol": "Mg", "name": "Magnesium", "color": "light green"},
    13: {"symbol": "Al", "name": "Aluminum", "color": "gray"},
    14: {"symbol": "Si", "name": "Silicon", "color": "orange"},
    15: {"symbol": "P", "name": "Phosphorus", "color": "orange"},
    16: {"symbol": "S", "name": "Sulfur", "color": "yellow"},
    17: {"symbol": "Cl", "name": "Chlorine", "color": "green"},
    18: {"symbol": "Ar", "name": "Argon", "color": "light blue"},
    19: {"symbol": "K", "name": "Potassium", "color": "purple"},
    20: {"symbol": "Ca", "name": "Calcium", "color": "light green"},
    21: {"symbol": "Sc", "name": "Scandium", "color": "gray"},
    22: {"symbol": "Ti", "name": "Titanium", "color": "gray"},
    23: {"symbol": "V", "name": "Vanadium", "color": "gray"},
    24: {"symbol": "Cr", "name": "Chromium", "color": "gray"},
    25: {"symbol": "Mn", "name": "Manganese", "color": "gray"},
    26: {"symbol": "Fe", "name": "Iron", "color": "gray"},
    27: {"symbol": "Co", "name": "Cobalt", "color": "gray"},
    28: {"symbol": "Ni", "name": "Nickel", "color": "gray"},
    29: {"symbol": "Cu", "name": "Copper", "color": "orange"},
    30: {"symbol": "Zn", "name": "Zinc", "color": "gray"},
    31: {"symbol": "Ga", "name": "Gallium", "color": "light blue"},
    32: {"symbol": "Ge", "name": "Germanium", "color": "gray"},
    33: {"symbol": "As", "name": "Arsenic", "color": "gray"},
    34: {"symbol": "Se", "name": "Selenium", "color": "yellow"},
    35: {"symbol": "Br", "name": "Bromine", "color": "orange"},
    36: {"symbol": "Kr", "name": "Krypton", "color": "light blue"},
    37: {"symbol": "Rb", "name": "Rubidium", "color": "purple"},
    38: {"symbol": "Sr", "name": "Strontium", "color": "light green"},
    39: {"symbol": "Y", "name": "Yttrium", "color": "gray"},
    40: {"symbol": "Zr", "name": "Zirconium", "color": "gray"},
    41: {"symbol": "Nb", "name": "Niobium", "color": "gray"},
    42: {"symbol": "Mo", "name": "Molybdenum", "color": "gray"},
    43: {"symbol": "Tc", "name": "Technetium", "color": "gray"},
    44: {"symbol": "Ru", "name": "Ruthenium", "color": "gray"},
    45: {"symbol": "Rh", "name": "Rhodium", "color": "gray"},
    46: {"symbol": "Pd", "name": "Palladium", "color": "gray"},
    47: {"symbol": "Ag", "name": "Silver", "color": "gray"},
    48: {"symbol": "Cd", "name": "Cadmium", "color": "gray"},
    49: {"symbol": "In", "name": "Indium", "color": "gray"},
    50: {"symbol": "Sn", "name": "Tin", "color": "gray"},
    51: {"symbol": "Sb", "name": "Antimony", "color": "gray"},
    52: {"symbol": "Te", "name": "Tellurium", "color": "gray"},
    53: {"symbol": "I", "name": "Iodine", "color": "purple"},
    54: {"symbol": "Xe", "name": "Xenon", "color": "light blue"},
    55: {"symbol": "Cs", "name": "Cesium", "color": "purple"},
    56: {"symbol": "Ba", "name": "Barium", "color": "light green"},
    57: {"symbol": "La", "name": "Lanthanum", "color": "gray"},
    58: {"symbol": "Ce", "name": "Cerium", "color": "gray"},
    59: {"symbol": "Pr", "name": "Praseodymium", "color": "gray"},
    60: {"symbol": "Nd", "name": "Neodymium", "color": "gray"},
    61: {"symbol": "Pm", "name": "Promethium", "color": "gray"},
    62: {"symbol": "Sm", "name": "Samarium", "color": "gray"},
    63: {"symbol": "Eu", "name": "Europium", "color": "gray"},
    64: {"symbol": "Gd", "name": "Gadolinium", "color": "gray"},
    65: {"symbol": "Tb", "name": "Terbium", "color": "gray"},
    66: {"symbol": "Dy", "name": "Dysprosium", "color": "gray"},
    67: {"symbol": "Ho", "name": "Holmium", "color": "gray"},
    68: {"symbol": "Er", "name": "Erbium", "color": "gray"},
    69: {"symbol": "Tm", "name": "Thulium", "color": "gray"},
    70: {"symbol": "Yb", "name": "Ytterbium", "color": "gray"},
    71: {"symbol": "Lu", "name": "Lutetium", "color": "gray"},
    72: {"symbol": "Hf", "name": "Hafnium", "color": "gray"},
    73: {"symbol": "Ta", "name": "Tantalum", "color": "gray"},
    74: {"symbol": "W", "name": "Tungsten", "color": "gray"},
    75: {"symbol": "Re", "name": "Rhenium", "color": "gray"},
    76: {"symbol": "Os", "name": "Osmium", "color": "gray"},
    77: {"symbol": "Ir", "name": "Iridium", "color": "gray"},
    78: {"symbol": "Pt", "name": "Platinum", "color": "gray"},
    79: {"symbol": "Au", "name": "Gold", "color": "gold"},
    80: {"symbol": "Hg", "name": "Mercury", "color": "gray"},
    81: {"symbol": "Tl", "name": "Thallium", "color": "gray"},
    82: {"symbol": "Pb", "name": "Lead", "color": "gray"},
    83: {"symbol": "Bi", "name": "Bismuth", "color": "gray"},
    84: {"symbol": "Po", "name": "Polonium", "color": "gray"},
    85: {"symbol": "At", "name": "Astatine", "color": "gray"},
    86: {"symbol": "Rn", "name": "Radon", "color": "gray"},
    87: {"symbol": "Fr", "name": "Francium", "color": "purple"},
    88: {"symbol": "Ra", "name": "Radium", "color": "gray"},
    89: {"symbol": "Ac", "name": "Actinium", "color": "red"},
    90: {"symbol": "Th", "name": "Thorium", "color": "red"},
    91: {"symbol": "Pa", "name": "Protactinium", "color": "red"},
    92: {"symbol": "U", "name": "Uranium", "color": "red"},
    93: {"symbol": "Np", "name": "Neptunium", "color": "red"},
    94: {"symbol": "Pu", "name": "Plutonium", "color": "red"},
    95: {"symbol": "Am", "name": "Americium", "color": "red"},
    96: {"symbol": "Cm", "name": "Curium", "color": "red"},
    97: {"symbol": "Bk", "name": "Berkelium", "color": "red"},
    98: {"symbol": "Cf", "name": "Californium", "color": "red"},
    99: {"symbol": "Es", "name": "Einsteinium", "color": "red"},
    100: {"symbol": "Fm", "name": "Fermium", "color": "red"},
    101: {"symbol": "Md", "name": "Mendelevium", "color": "red"},
    102: {"symbol": "No", "name": "Nobelium", "color": "red"},
    103: {"symbol": "Lr", "name": "Lawrencium", "color": "red"},
    104: {"symbol": "Rf", "name": "Rutherfordium", "color": "sky blue"},
    105: {"symbol": "Db", "name": "Dubnium", "color": "sky blue"},
    106: {"symbol": "Sg", "name": "Seaborgium", "color": "sky blue"},
    107: {"symbol": "Bh", "name": "Bohrium", "color": "sky blue"},
    108: {"symbol": "Hs", "name": "Hassium", "color": "sky blue"},
    109: {"symbol": "Mt", "name": "Meitnerium", "color": "sky blue"},
    110: {"symbol": "Ds", "name": "Darmstadtium", "color": "sky blue"},
    111: {"symbol": "Rg", "name": "Roentgenium", "color": "sky blue"},
    112: {"symbol": "Cn", "name": "Copernicium", "color": "sky blue"},
    113: {"symbol": "Nh", "name": "Nihonium", "color": "orange"},
    114: {"symbol": "Fl", "name": "Flerovium", "color": "orange"},
    115: {"symbol": "Mc", "name": "Moscovium", "color": "orange"},
    116: {"symbol": "Lv", "name": "Livermorium", "color": "orange"},
    117: {"symbol": "Ts", "name": "Tennessine", "color": "yellow"},
    118: {"symbol": "Og", "name": "Oganesson", "color": "yellow"}
}

default_color = "white"

def display_info(atomic_number):
    if atomic_number in elements:
        element = elements[atomic_number]
        messagebox.showinfo(
            "Element Information",
            f"Number: {atomic_number}\nSymbol: {element['symbol']}\nName: {element['name']}",
        )
    else:
        messagebox.showerror("Element Not Found", "The selected element was not found.")

window = tk.Tk()
window.title("Periodic Table")
button_font = Font(family="Helvetica", size=10, weight="bold")

for atomic_number in range(1,119):
    element_data = elements.get(atomic_number, {})
    button_color = element_data.get("color", default_color)

    element_button = tk.Button(
        window,
        text=str(atomic_number),
        width=4,
        height=2,
        font=button_font,
        command=lambda atomic_number=atomic_number: display_info(atomic_number),bg=button_color,
    )
    element_button.grid(row=(atomic_number - 1) // 18, column=(atomic_number - 1) % 18)

window.mainloop()
