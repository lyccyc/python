def is_spellable_by_ptable(in_str, p_table):
    if in_str[0] in p_table:
        if len(in_str) == 1:
            return True
        else:
            a = list(in_str)
            u = a.pop(0)
            in_str = "".join(a)
            if is_spellable_by_ptable(in_str, p_table) != False:
                return is_spellable_by_ptable(in_str, p_table)
            a.insert(0, u)
            in_str = "".join(a)
    if in_str[:2] in p_table:
        if len(in_str) == 2:
            return True
        else:
            a = list(in_str)
            u = a.pop(0)
            v = a.pop(0)
            in_str = "".join(a)
            if is_spellable_by_ptable(in_str, p_table) != False:
                return is_spellable_by_ptable(in_str, p_table)
            a.insert(0, v)
            a.insert(0, u)
            in_str = "".join(a)
    return False


if __name__ == "__main__":
    p_table = ["y", "es", "yb", "se", "s", "mg", "ti", "mn", "mt", "as"]
    p_table = [e.lower() for e in p_table]
    print(is_spellable_by_ptable("yes", p_table))
    # print(is_spellable_by_ptable("math", p_table))
