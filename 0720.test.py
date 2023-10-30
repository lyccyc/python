def is_spellable_by_ptable(in_str, p_table: str):
    for i in in_str:
        if i in p_table:
            return True
        else:
            return False


if __name__ == "__main__":
    p_table = ["y", "es", "yb", "se", "s", "mg", "ti", "mn", "mt", "as"]
    p_table = [e.lower() for e in p_table]
    print(is_spellable_by_ptable("yes", p_table))
    print(is_spellable_by_ptable("math", p_table))
