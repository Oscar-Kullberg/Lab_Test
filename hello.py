print("skriv done om du är färdig")

x = input("förstår du? y för ja, n för nej ")

while x != "done": 
 
 x = input("skriv: ")

 try: 
    if x.isdigit():
        x = float(x) 
        print("varför ett nummer?????")

 except:
    if x != x.isdigit():
     print("not a number")



