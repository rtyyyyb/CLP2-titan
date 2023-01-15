import time
st = time.process_time() # getting start time
define_list = []
reg_list = []
def change(instruction):
    split = instruction.split()
    instr = split[0] # spliting the operands 
    for name in split:
        if name in define_list:
            def_place = define_list.index(name)
            split[split.index(name)] = reg_list[def_place] #changing defiens into register numbers
    if instr.upper() == "@DEFINE":
        define_list.append(split[1])
        reg_list.append(split[2]) 
    elif instr == "ADD": # translations from urcl to clp2
        print("REGA",split[2])
        print("REGB",split[3])
        print("ADD")
        print("OTRG",split[1])
    elif instr == "RSH":
        print("REGA",split[2])
        print("RSHT")
        print("OTRG",split[1])
    elif instr == "LOD":
        print("SMAR",split[2])
        print("RMRG",split[1])
    elif instr == "STR":
        print("SMAR",split[1])
        print("RGRM",split[2])
    elif instr == "BGE":
        print("REGA",split[2])
        print("REGB",split[3])
        print("SUB")
        print("JMPC",split[1])
    elif instr == "NOR":
        print("REGA",split[2])
        print("REGB",split[3])
        print("NOR")
        print("OTRG",split[1])
    elif instr == "IMM":
        print("SREG",split[1])
        print(split[2])
    elif instr == "OUT": # display functions
        if split[1] == "%X":
            print("REGX",split[2])
        elif split[1] == "%Y":
            print("REGY",split[2])
        elif split[1] == "%COLOR" and split[2] == "247":
            print("PLOT")
        elif split[1] == "%COLOR" and split[2] == "0":
            print("RSET")
        else:
            print("OUT",split[2],split[1])
    elif instr == "IN":
        print("IN",split[1],split[2])
    else:
        print(instruction)
with open("C:\\Users\\User\\Documents\\pothon_codes\\CLP2\\urcl code.txt", "r") as f: # dhanges each line one after another
    contents = f.readlines()
for line in contents:
    change(line)
et = time.process_time() # get end time
duration = et - st
print("Done! compile took:",duration,"seconds") # finish statement