print("-------")
print("python has entered the building")    
type(3)
counties= ["Arapahoe", "Denver", "Jefferson"]
counties 
counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
counties_dict
counties=["Arapahoe","Denver", "Jefferson"]
if counties[1]=='Denver':
    print(counties[1])
    
temperature= int(input("what is the temperture outside?"))

if temperature>80:
    print("Turn on the AC.")
    
else:
    print("Open the windows!")
    
#what is the score?

score= int(input("What is your test score?"))

#determine the grade

if score>=90:
    print('Your grade is an A!')
    
else:
    if score>=80:
        print('Your grade is a B.')
        
    else:
        if score>=70:
            print('your grade is a C.')
            
        else:
            if score>=60:
                print('Your grade is a D')
                
            else:
                print('You need a tutor')
                
#new look

Counties=["Arapahoe","Denver", "Jefferson"]

if "Arapahoe" in Counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties")
else:
    print("Arapahoe and El Paso is not in the list of counties.")
    
    
for county in counties_dict:
    print(county)
    
    

                
                
                
        