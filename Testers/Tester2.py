n = 100
ener = int(n % 10) # singles digit 
tier = int(((n % 100) - ener) / 10) # tens digit 
hundrer = int(((n % 1000) - (tier * 10) - ener) / 100) # hundreds digit 

print(hundrer, tier, ener) 