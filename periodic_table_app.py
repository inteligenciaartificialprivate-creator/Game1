import tkinter as tk
from tkinter import ttk, messagebox


class PeriodicTableApp:
    """Tkinter desktop app that shows an interactive periodic table."""

    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Periodic Table")
        self.root.geometry("1500x780")
        self.root.configure(bg="#f4f6f8")

        self.family_colors = {
            "alkali metal": "#ffb3ba",
            "alkaline earth metal": "#ffdfba",
            "transition metal": "#fff5ba",
            "post-transition metal": "#d5f5e3",
            "metalloid": "#c9daf8",
            "nonmetal": "#d9ead3",
            "halogen": "#f4cccc",
            "noble gas": "#d9d2e9",
            "lanthanide": "#fce5cd",
            "actinide": "#ead1dc",
            "unknown": "#e6e6e6",
        }

        # Element data is stored directly in-program as requested.
        self.elements = self._build_elements()
        self.elements_by_symbol = {e["symbol"]: e for e in self.elements}
        self.elements_by_name = {e["name"].lower(): e for e in self.elements}

        self.button_by_symbol = {}
        self._build_ui()
        self._draw_periodic_table()

    def _build_elements(self):
        """Create element data dictionaries from compact source tuples."""
        raw = [
            # atomic_number, symbol, name, atomic_mass, category, period, group
            (1, "H", "Hydrogen", 1.008, "nonmetal", 1, 1),
            (2, "He", "Helium", 4.003, "noble gas", 1, 18),
            (3, "Li", "Lithium", 6.94, "alkali metal", 2, 1),
            (4, "Be", "Beryllium", 9.012, "alkaline earth metal", 2, 2),
            (5, "B", "Boron", 10.81, "metalloid", 2, 13),
            (6, "C", "Carbon", 12.011, "nonmetal", 2, 14),
            (7, "N", "Nitrogen", 14.007, "nonmetal", 2, 15),
            (8, "O", "Oxygen", 15.999, "nonmetal", 2, 16),
            (9, "F", "Fluorine", 18.998, "halogen", 2, 17),
            (10, "Ne", "Neon", 20.180, "noble gas", 2, 18),
            (11, "Na", "Sodium", 22.990, "alkali metal", 3, 1),
            (12, "Mg", "Magnesium", 24.305, "alkaline earth metal", 3, 2),
            (13, "Al", "Aluminum", 26.982, "post-transition metal", 3, 13),
            (14, "Si", "Silicon", 28.085, "metalloid", 3, 14),
            (15, "P", "Phosphorus", 30.974, "nonmetal", 3, 15),
            (16, "S", "Sulfur", 32.06, "nonmetal", 3, 16),
            (17, "Cl", "Chlorine", 35.45, "halogen", 3, 17),
            (18, "Ar", "Argon", 39.948, "noble gas", 3, 18),
            (19, "K", "Potassium", 39.098, "alkali metal", 4, 1),
            (20, "Ca", "Calcium", 40.078, "alkaline earth metal", 4, 2),
            (21, "Sc", "Scandium", 44.956, "transition metal", 4, 3),
            (22, "Ti", "Titanium", 47.867, "transition metal", 4, 4),
            (23, "V", "Vanadium", 50.942, "transition metal", 4, 5),
            (24, "Cr", "Chromium", 51.996, "transition metal", 4, 6),
            (25, "Mn", "Manganese", 54.938, "transition metal", 4, 7),
            (26, "Fe", "Iron", 55.845, "transition metal", 4, 8),
            (27, "Co", "Cobalt", 58.933, "transition metal", 4, 9),
            (28, "Ni", "Nickel", 58.693, "transition metal", 4, 10),
            (29, "Cu", "Copper", 63.546, "transition metal", 4, 11),
            (30, "Zn", "Zinc", 65.38, "transition metal", 4, 12),
            (31, "Ga", "Gallium", 69.723, "post-transition metal", 4, 13),
            (32, "Ge", "Germanium", 72.630, "metalloid", 4, 14),
            (33, "As", "Arsenic", 74.922, "metalloid", 4, 15),
            (34, "Se", "Selenium", 78.971, "nonmetal", 4, 16),
            (35, "Br", "Bromine", 79.904, "halogen", 4, 17),
            (36, "Kr", "Krypton", 83.798, "noble gas", 4, 18),
            (37, "Rb", "Rubidium", 85.468, "alkali metal", 5, 1),
            (38, "Sr", "Strontium", 87.62, "alkaline earth metal", 5, 2),
            (39, "Y", "Yttrium", 88.906, "transition metal", 5, 3),
            (40, "Zr", "Zirconium", 91.224, "transition metal", 5, 4),
            (41, "Nb", "Niobium", 92.906, "transition metal", 5, 5),
            (42, "Mo", "Molybdenum", 95.95, "transition metal", 5, 6),
            (43, "Tc", "Technetium", 98, "transition metal", 5, 7),
            (44, "Ru", "Ruthenium", 101.07, "transition metal", 5, 8),
            (45, "Rh", "Rhodium", 102.906, "transition metal", 5, 9),
            (46, "Pd", "Palladium", 106.42, "transition metal", 5, 10),
            (47, "Ag", "Silver", 107.868, "transition metal", 5, 11),
            (48, "Cd", "Cadmium", 112.414, "transition metal", 5, 12),
            (49, "In", "Indium", 114.818, "post-transition metal", 5, 13),
            (50, "Sn", "Tin", 118.710, "post-transition metal", 5, 14),
            (51, "Sb", "Antimony", 121.760, "metalloid", 5, 15),
            (52, "Te", "Tellurium", 127.60, "metalloid", 5, 16),
            (53, "I", "Iodine", 126.904, "halogen", 5, 17),
            (54, "Xe", "Xenon", 131.293, "noble gas", 5, 18),
            (55, "Cs", "Cesium", 132.905, "alkali metal", 6, 1),
            (56, "Ba", "Barium", 137.327, "alkaline earth metal", 6, 2),
            (57, "La", "Lanthanum", 138.905, "lanthanide", 8, 3),
            (58, "Ce", "Cerium", 140.116, "lanthanide", 8, 4),
            (59, "Pr", "Praseodymium", 140.908, "lanthanide", 8, 5),
            (60, "Nd", "Neodymium", 144.242, "lanthanide", 8, 6),
            (61, "Pm", "Promethium", 145, "lanthanide", 8, 7),
            (62, "Sm", "Samarium", 150.36, "lanthanide", 8, 8),
            (63, "Eu", "Europium", 151.964, "lanthanide", 8, 9),
            (64, "Gd", "Gadolinium", 157.25, "lanthanide", 8, 10),
            (65, "Tb", "Terbium", 158.925, "lanthanide", 8, 11),
            (66, "Dy", "Dysprosium", 162.500, "lanthanide", 8, 12),
            (67, "Ho", "Holmium", 164.930, "lanthanide", 8, 13),
            (68, "Er", "Erbium", 167.259, "lanthanide", 8, 14),
            (69, "Tm", "Thulium", 168.934, "lanthanide", 8, 15),
            (70, "Yb", "Ytterbium", 173.045, "lanthanide", 8, 16),
            (71, "Lu", "Lutetium", 174.967, "lanthanide", 8, 17),
            (72, "Hf", "Hafnium", 178.49, "transition metal", 6, 4),
            (73, "Ta", "Tantalum", 180.948, "transition metal", 6, 5),
            (74, "W", "Tungsten", 183.84, "transition metal", 6, 6),
            (75, "Re", "Rhenium", 186.207, "transition metal", 6, 7),
            (76, "Os", "Osmium", 190.23, "transition metal", 6, 8),
            (77, "Ir", "Iridium", 192.217, "transition metal", 6, 9),
            (78, "Pt", "Platinum", 195.084, "transition metal", 6, 10),
            (79, "Au", "Gold", 196.967, "transition metal", 6, 11),
            (80, "Hg", "Mercury", 200.592, "transition metal", 6, 12),
            (81, "Tl", "Thallium", 204.38, "post-transition metal", 6, 13),
            (82, "Pb", "Lead", 207.2, "post-transition metal", 6, 14),
            (83, "Bi", "Bismuth", 208.980, "post-transition metal", 6, 15),
            (84, "Po", "Polonium", 209, "metalloid", 6, 16),
            (85, "At", "Astatine", 210, "halogen", 6, 17),
            (86, "Rn", "Radon", 222, "noble gas", 6, 18),
            (87, "Fr", "Francium", 223, "alkali metal", 7, 1),
            (88, "Ra", "Radium", 226, "alkaline earth metal", 7, 2),
            (89, "Ac", "Actinium", 227, "actinide", 9, 3),
            (90, "Th", "Thorium", 232.038, "actinide", 9, 4),
            (91, "Pa", "Protactinium", 231.036, "actinide", 9, 5),
            (92, "U", "Uranium", 238.029, "actinide", 9, 6),
            (93, "Np", "Neptunium", 237, "actinide", 9, 7),
            (94, "Pu", "Plutonium", 244, "actinide", 9, 8),
            (95, "Am", "Americium", 243, "actinide", 9, 9),
            (96, "Cm", "Curium", 247, "actinide", 9, 10),
            (97, "Bk", "Berkelium", 247, "actinide", 9, 11),
            (98, "Cf", "Californium", 251, "actinide", 9, 12),
            (99, "Es", "Einsteinium", 252, "actinide", 9, 13),
            (100, "Fm", "Fermium", 257, "actinide", 9, 14),
            (101, "Md", "Mendelevium", 258, "actinide", 9, 15),
            (102, "No", "Nobelium", 259, "actinide", 9, 16),
            (103, "Lr", "Lawrencium", 266, "actinide", 9, 17),
            (104, "Rf", "Rutherfordium", 267, "transition metal", 7, 4),
            (105, "Db", "Dubnium", 268, "transition metal", 7, 5),
            (106, "Sg", "Seaborgium", 269, "transition metal", 7, 6),
            (107, "Bh", "Bohrium", 270, "transition metal", 7, 7),
            (108, "Hs", "Hassium", 269, "transition metal", 7, 8),
            (109, "Mt", "Meitnerium", 278, "unknown", 7, 9),
            (110, "Ds", "Darmstadtium", 281, "unknown", 7, 10),
            (111, "Rg", "Roentgenium", 282, "unknown", 7, 11),
            (112, "Cn", "Copernicium", 285, "transition metal", 7, 12),
            (113, "Nh", "Nihonium", 286, "post-transition metal", 7, 13),
            (114, "Fl", "Flerovium", 289, "post-transition metal", 7, 14),
            (115, "Mc", "Moscovium", 290, "post-transition metal", 7, 15),
            (116, "Lv", "Livermorium", 293, "post-transition metal", 7, 16),
            (117, "Ts", "Tennessine", 294, "halogen", 7, 17),
            (118, "Og", "Oganesson", 294, "noble gas", 7, 18),
        ]

        elements = []
        for num, symbol, name, mass, category, period, group in raw:
            elements.append(
                {
                    "atomic_number": num,
                    "symbol": symbol,
                    "name": name,
                    "atomic_mass": mass,
                    "category": category,
                    "period": period,
                    "group": group,
                    "description": f"{name} is a {category} element in the periodic table.",
                }
            )
        return elements

    def _build_ui(self):
        top = tk.Frame(self.root, bg="#f4f6f8")
        top.pack(fill="x", padx=12, pady=8)

        tk.Label(top, text="Search by name or symbol:", bg="#f4f6f8", font=("Arial", 11, "bold")).pack(side="left")

        self.search_var = tk.StringVar()
        entry = ttk.Entry(top, textvariable=self.search_var, width=30)
        entry.pack(side="left", padx=(8, 4))
        entry.bind("<Return>", lambda _e: self.search_element())

        ttk.Button(top, text="Find", command=self.search_element).pack(side="left", padx=2)
        ttk.Button(top, text="Reset", command=self.reset_highlights).pack(side="left", padx=2)

        legend = tk.Frame(self.root, bg="#f4f6f8")
        legend.pack(fill="x", padx=12, pady=(0, 6))
        for family, color in self.family_colors.items():
            swatch = tk.Label(legend, text=family.title(), bg=color, relief="solid", bd=1, padx=6, pady=2)
            swatch.pack(side="left", padx=2, pady=2)

        self.table_frame = tk.Frame(self.root, bg="#f4f6f8")
        self.table_frame.pack(fill="both", expand=True, padx=12, pady=6)

    def _draw_periodic_table(self):
        # Column labels (groups)
        for g in range(1, 19):
            lbl = tk.Label(self.table_frame, text=str(g), bg="#f4f6f8", font=("Arial", 9, "bold"))
            lbl.grid(row=0, column=g, padx=2, pady=2)

        # Period labels
        for p in range(1, 8):
            lbl = tk.Label(self.table_frame, text=str(p), bg="#f4f6f8", font=("Arial", 9, "bold"))
            lbl.grid(row=p, column=0, padx=2, pady=2)

        tk.Label(self.table_frame, text="La-Lu", bg="#f4f6f8", font=("Arial", 9, "bold")).grid(row=8, column=0)
        tk.Label(self.table_frame, text="Ac-Lr", bg="#f4f6f8", font=("Arial", 9, "bold")).grid(row=9, column=0)

        for el in self.elements:
            row = el["period"]
            col = el["group"]
            color = self.family_colors.get(el["category"], self.family_colors["unknown"])

            btn = tk.Button(
                self.table_frame,
                text=f"{el['atomic_number']}\n{el['symbol']}",
                width=6,
                height=3,
                bg=color,
                relief="raised",
                command=lambda e=el: self.show_details(e),
                font=("Arial", 8, "bold"),
            )
            btn.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
            self.button_by_symbol[el["symbol"]] = btn

        for c in range(1, 19):
            self.table_frame.grid_columnconfigure(c, weight=1)

    def search_element(self):
        query = self.search_var.get().strip().lower()
        if not query:
            return

        self.reset_highlights()

        element = self.elements_by_name.get(query)
        if element is None:
            # If it is not a name, try symbol match.
            for symbol, el in self.elements_by_symbol.items():
                if symbol.lower() == query:
                    element = el
                    break

        if element is None:
            messagebox.showinfo("Not found", f"No element found for '{query}'.")
            return

        btn = self.button_by_symbol[element["symbol"]]
        btn.config(relief="sunken", bd=4, highlightbackground="black", highlightthickness=2)
        self.show_details(element)

    def reset_highlights(self):
        for btn in self.button_by_symbol.values():
            btn.config(relief="raised", bd=1, highlightthickness=0)

    def show_details(self, element):
        """Open a popup with full element information."""
        top = tk.Toplevel(self.root)
        top.title(f"{element['name']} ({element['symbol']})")
        top.geometry("420x360")
        top.configure(bg="white")

        protons = element["atomic_number"]
        electrons = element["atomic_number"]  # neutral atom assumption
        neutrons = int(round(element["atomic_mass"])) - element["atomic_number"]

        title = tk.Label(
            top,
            text=f"{element['name']} ({element['symbol']})",
            font=("Arial", 16, "bold"),
            bg="white",
        )
        title.pack(pady=(12, 8))

        info_lines = [
            ("Element name", element["name"]),
            ("Symbol", element["symbol"]),
            ("Atomic number", element["atomic_number"]),
            ("Atomic mass", element["atomic_mass"]),
            ("Protons", protons),
            ("Neutrons", neutrons),
            ("Electrons", electrons),
            ("Category", element["category"].title()),
        ]

        info_frame = tk.Frame(top, bg="white")
        info_frame.pack(fill="x", padx=16)

        for label, value in info_lines:
            row = tk.Frame(info_frame, bg="white")
            row.pack(fill="x", pady=1)
            tk.Label(row, text=f"{label}:", width=16, anchor="w", bg="white", font=("Arial", 10, "bold")).pack(side="left")
            tk.Label(row, text=str(value), anchor="w", bg="white", font=("Arial", 10)).pack(side="left")

        tk.Label(top, text="Description:", bg="white", font=("Arial", 10, "bold")).pack(anchor="w", padx=16, pady=(10, 0))
        msg = tk.Message(top, text=element["description"], width=380, bg="white", font=("Arial", 10))
        msg.pack(anchor="w", padx=16, pady=(0, 8))


if __name__ == "__main__":
    root = tk.Tk()
    app = PeriodicTableApp(root)
    root.mainloop()
