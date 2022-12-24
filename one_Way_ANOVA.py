File = open("file.txt", "w")
File.close()

groups = {
    "A":[] ,
    "B":[] ,
    "C":[]
}

#get info for group A
A_info = 0

while A_info < 5:
    groups["A"].append(input("enter num for group A:  "))
    
    A_info += 1
groups["A"] = list(map(int , groups["A"]))

#end 

#get info for group B
B_info = 0

while B_info < 5:
    groups["B"].append(input("enter num for group B:  "))
    
    B_info += 1
groups["B"] = list(map(int , groups["B"]))

#end 


#get info for group C
C_info = 0

while C_info < 5:
    groups["C"].append(input("enter num  for group C:  "))
    
    C_info += 1
groups["C"] = list(map(int , groups["C"]))

#end 



A_Total = 0

B_Total = 0

C_Total = 0

# here we get Total of each groups
for i in groups["A"]:
    A_Total = A_Total + i

for i in groups["B"]:
    B_Total = B_Total + i

for i in groups["C"]:
    C_Total = C_Total + i

# end 

# here we get CF
cf = A_Total +  B_Total +  C_Total

cf = cf**2 / (5*3)

# end 






# here we try to get sst
sst = 0

for i in groups["A"]:
    sst = sst + i**2

for i in groups["B"]:
    sst = sst + i**2

for i in groups["C"]:
    sst = sst + i**2


sst = sst - cf

#end


# here we get ssb
ssb = ((A_Total**2) + (B_Total**2) + (C_Total**2)) / 5

ssb = ssb - cf

#end

#here we get ssw

ssw = sst - ssb

#end 

#جدول التحليل
#df
df_Between_groups = 3 - 1

df_Within_groups = 3*(5-1)


Total_df = df_Between_groups + df_Within_groups

#end 

#SS

ss_Between_groups = ssb

ss_Within_groups = ssw 

ss_Total = sst

#end 

#MS

msb = ss_Between_groups / df_Between_groups

msw = ss_Within_groups / df_Within_groups

F = msb / msw

if F > 3.89:
    with open("file.txt", "w", encoding="utf-8") as myfile:
        myfile.write("نجد أن القيمة المحسوبة \n")
        myfile.write(str(round(F,2)) + " \n")
        myfile.write("وهي أكبر من قيمة الجدول 3.89 \n ")
        myfile.write(" وعليه قرننا نحن أبو عبدالله و عبدالرحمن ماهو أت نرفض فرض العدم")



else:
    with open("file.txt", "w", encoding="utf-8") as myfile:
        myfile.write("نجد أن القيمة المحسوبة \n")
        myfile.write(str(round(F,2)) + " \n")
        myfile.write("وهي أصغر من قيمة الجدول 3.89 \n ")
        myfile.write(" وعليه قرننا نحن أبو عبدالله و عبدالرحمن ماهو أت نقبل فرض العدم")

   



print("Done go see anwer!! Go to Folder file.txt ")