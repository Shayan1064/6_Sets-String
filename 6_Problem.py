
# write code to count wowels and consunent in String......
text=input("Enter Text: ")
V_count=0
c_count=0
for i in text:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U" ):
        V_count+=1
        
    else:
        c_count+=1
        

print("Total vowels: ",V_count)
print("Total Consunent: ",c_count)