
def complement(dna_in):

    #Reverse in_1
    reverse = in_1[::-1]
    txt = ""
    #Switcing each letter
    for x in reverse:
        
        if x == "A":
            y = "T"
        elif x == "T":
            y = "A"
        elif x == "G":
            y = "C"
        else:
            y = "G"
        
        txt = txt + y

    return txt
    
    



in_1 = "ATAGCAGT"
out_1 = complement(in_1)
print(out_1)