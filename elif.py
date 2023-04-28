#what is the score?

score= int(input("What is your test score?"))

#determine the grade

if score>=90:
    print('Your grade is an A!')
    
elif score>=80:
        print('Your grade is a B.')
        
elif score>=70:
        print('your grade is a C.')
            
elif score>=60:
        print('Your grade is a D')
                
else:
        print('You need a tutor')

Counties=["Arapahoe","Denver", "Jefferson"]

if "Arapahoe" in Counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties")
else:
    print("Arapahoe and El Paso is not in the list of counties.")
        