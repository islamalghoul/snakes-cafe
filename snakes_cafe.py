print("""
************************************************
**       Welcome to the Snackes Cafe!         **
**       Please see our manu below.           **
**
**       To quit at any time, type "quit"     **   
************************************************
""")
menu= {
    "Appetizers":["Wings","Cookies","Spring Rolls"],
    "Entrees":["Salmon","Steak","Meat Tornado","A Literal"],
    "Desserts":["Ice Cream","Cake","Pie"],
    "Drinks":["Coffee","Tea","Unicorn Tears"],
}

for x in menu:
    print(x)
    print("-"*len(x))
    for y in menu[x]:
        print(y)  

q="""
************************************************
what would you like to order?  
************************************************

"""

print(q)
order=input(">")
obj={}
while order.lower()!="quit":
    we_have_this_order=False
    
    for i in menu:
        for x in menu[i]:
            if order.lower()==x.lower():
                we_have_this_order=True
                if  x.lower() in obj:
                    obj[x.lower()]+=1 
                    
                else:
                    obj[x.lower()]=1
                       
            
    if  we_have_this_order :
        
        mass=""
        if len(obj)==1:
                mass=f"{obj[list(obj.keys())[0]]} order of {list(obj.keys())[0]}"
              
        else:        
            for i in obj:
                mass+=f" and {obj[i]} order of {i}"
            mass=mass[4:]    
        print(f" {mass} have been added to your meal")
           
               

    else:
        print("sorry we dont have this order in our menu but we will take your suggestion in consideration")
    order=input(">")
print(f"you have {mass}")