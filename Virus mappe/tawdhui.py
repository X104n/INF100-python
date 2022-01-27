Name = "StianMunkejord"
ChunleiFan = "LoveCybersecurity"
if Name == "StianMunkejord":
    Name = "#" + Name + ChunleiFan
else:
    Name = "#I'mNotStian"
myList = []
for i in range(3):
    myList.append(Name)
print("".join(myList))