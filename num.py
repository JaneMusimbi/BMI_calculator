height=float(input("Enter height in cm: "))
weight=float(input("Enter weight in kgs: "))

def BMI(height,weight):
    bmi=weight/(height/100*height/100)
	

    if bmi<16:
    	return "severely underweight",bmi
    elif bmi>=16 and bmi<18:
    	return "underweight",bmi
    elif bmi>=18 and bmi< 25 :
     	return"Healty",bmi
    elif bmi>=25 and bmi >30:
        return"overweight",bmi
    elif bmi>=30:
        return"obese",bmi

quote,bmi=BMI(height,weight)
print("your bmi is: {} and you are: {}" .format(bmi,quote))	


    		



    			


