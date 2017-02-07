def apply_rules(lhch):
    rhstr = ""
    if lhch == "A":
        rhstr = "B"
    elif lhch == "B":
        rhstr = "AB"
    else:
        rhstr = lhch
    return rhstr
def process_string(old_str):
    new_str = ""
    for ch in old_str:
        new_str = new_str + apply_rules(ch)
    return new_str
def create_l_system(num_iters, axiom):
    start_string = axiom
    end_string = ""
    for i in range(num_iters):
        end_string = process_string(start_string)
        start_string = end_string
    return end_string
print(create_l_system(6, "B"))
    
    