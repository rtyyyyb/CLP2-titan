import time
label_list = []
address_list = []
line_number = 0
label = ""
with open("urcl code.txt", "r") as f:
    contents = f.readlines()
for line in contents:
    if line[0] == ".":
        length = len(line)
        label_list.append(line[0:length - 1])
        address_list.append(line_number + 1)
    instr = line.split()
    if instr[0] == "ADD":
        line_number = line_number + 4
    elif instr[0] == "RSH":
        line_number = line_number + 3
    elif instr[0] == "LOD":
        line_number = line_number + 2
    elif instr[0] == "STR":
        line_number = line_number + 2
    elif instr[0] == "BGE":
        line_number = line_number + 6
    elif instr[0] == "NOR":
        line_number = line_number + 4
    elif instr[0] == "IMM":
        line_number = line_number + 2
    elif instr[0] == "OUT":
        line_number = line_number + 1
    elif instr[0] == "IN":
        line_number = line_number + 1
st = time.process_time() # getting start time
define_list = []
reg_list = []
def change(instruction):
    split = instruction.split()
    instr = split[0] # spliting the operands
    if instr[0] != ".":
        for name in split:
            if name in define_list:
                def_place = define_list.index(name)
                split[split.index(name)] = reg_list[def_place] #changing defiens into register numbers
        if instr.upper() == "@DEFINE":
            define_list.append(split[1])
            reg_list.append(split[2])
        if split[1] in label_list:
            label_place = label_list.index(split[1])
            split[1] = address_list[label_place]
        if instr == "ADD": # translations from urcl to clp2
            print("REGA",split[2])
            print("REGB",split[3])
            print("ADD")
            print("OTRG",split[1])
        if instr == "RSH":
            print("REGA",split[2])
            print("RSHT")
            print("OTRG",split[1])
        if instr == "LOD":
            print("SMAR",split[2])
            print("RMRG",split[1])
        if instr == "STR":
            print("SMAR",split[1])
            print("RGRM",split[2])
        if instr == "BGE":
            print("REGA",split[2])
            print("REGB",split[3])
            print("SUB")
            print("SREG JMPREG")
            print(split[1])
            print("JMPC JMPREG")
        if instr == "NOR":
            print("REGA",split[2])
            print("REGB",split[3])
            print("NOR")
            print("OTRG",split[1])
        if instr == "IMM":
            print("SREG",split[1])
            print(split[2])
        if instr == "OUT": # display functions
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
        if instr == "IN":
            print("IN",split[1],split[2])
with open("urcl code.txt", "r") as f: # changes each line one after another
    contents = f.readlines()
for line in contents:
    change(line)
et = time.process_time() # get end time
duration = et - st
print("Done! compile took:",duration,"seconds") # finish statement
