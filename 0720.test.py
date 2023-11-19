def is_spellable_by_ptable(in_str, p_table):
    if in_str[0] in p_table:
        if len(in_str) == 1:
            print(in_str[0])
        else:
            a = list(in_str)
            u = a.pop(0)
            in_str = "".join(a)
            if is_spellable_by_ptable(in_str, p_table) != False:
                print(is_spellable_by_ptable(in_str, p_table))
            a.insert(0, u)
            in_str = "".join(a)
    if in_str[:2] in p_table:
        if len(in_str) == 2:
            print(in_str[:2])
        else:
            a = list(in_str)
            u = a.pop(0)
            v = a.pop(0)
            in_str = "".join(a)
            if is_spellable_by_ptable(in_str, p_table) != False:
                print(is_spellable_by_ptable(in_str, p_table))
            a.insert(0, v)
            a.insert(0, u)
            in_str = "".join(a)
    print("[]")


if __name__ == "__main__":
    p_table = [
        "H",
        "He",
        "Li",
        "Be",
        "B",
        "C",
        "N",
        "O",
        "F",
        "Ne",
        "Na",
        "Mg",
        "Al",
        "Si",
        "P",
        "S",
        "Cl",
        "Ar",
        "K",
        "Ca",
        "Sc",
        "Ti",
        "V",
        "Cr",
        "Mn",
        "Fe",
        "Co",
        "Ni",
        "Cu",
        "Zn",
        "Ga",
        "Ge",
        "As",
        "Se",
        "Br",
        "Kr",
        "Rb",
        "Sr",
        "Y",
        "Zr",
        "Nb",
        "Mo",
        "Tc",
        "Ru",
        "Rh",
        "Pd",
        "Ag",
        "Cd",
        "In",
        "Sn",
        "Sb",
        "Te",
        "I",
        "Xe",
        "Cs",
        "Ba",
        "La",
        "Ce",
        "Pr",
        "Nd",
        "Pm",
        "Sm",
        "Eu",
        "Gd",
        "Tb",
        "Dy",
        "Ho",
        "Er",
        "Tm",
        "Yb",
        "Lu",
        "Hf",
        "Ta",
        "W",
        "Re",
        "Os",
        "Ir",
        "Pt",
        "Au",
        "Hg",
        "Tl",
        "Pb",
        "Bi",
        "Po",
        "At",
        "Rn",
        "Fr",
        "Ra",
        "Ac",
        "Th",
        "Pa",
        "U",
        "Np",
        "Pu",
        "Am",
        "Cm",
        "Bk",
        "Cf",
        "Es",
        "Fm",
        "Md",
        "No",
        "Lr",
        "Rf",
        "Db",
        "Sg",
        "Bh",
        "Hs",
        "Mt",
        "Ds",
        "Rg",
        "Cn",
        "Nh",
        "Fl",
        "Mc",
        "Lv",
        "Ts",
        "Og",
    ]
    p_table = [e.lower() for e in p_table]
    print(is_spellable_by_ptable("yes", p_table))
    print(is_spellable_by_ptable("math", p_table))
