print(" \n\t $$$$$$$ WELCOME to ATM sevice .py $$$$$$$ \t \n \t >>>GET AND CARRY WITH GREAT CARE \n\t OUR MOTTO:WE ARE HERE TO SERVE YOU")

#function defined that runs the ATM system

def atmSystem(pinCode,pinCode01,pinCode02,pinCode03,pinCode04,pinCode05,names,name01,name02,name03,name04,name05,acountNums,acountnum01,acountnum02,acountnum03,acountnum04,acountnum05,balance,balance01,balance02,balance03,balance04,balance05):
	for i in range(1,1000000000000000000000000000000000):
		pinCodeinput = int(input("PLEASE ENTER YOUR PIN CODE:\n"))
		if pinCodeinput == pinCode01 :
			print("\nwelcome", name01 ,"\n your account number is :", acountnum01 ,"\n your balance is:",balance01)
			deposition = input("DO YOU WANT TO DEPOSITE MONEY(Y / N):")  
			deposition = deposition.upper()
			withDrawing = input("DO YOU WANT TO WITHDRAW MONEY FROM YOUR ACCOUNT(Y/N):")
			withDrawing = withDrawing.upper()
			if deposition == "Y":
				depositionAmt = int(input("ENTER THE AMOUNT FOR DEPOSITION:"))
				print("ok your new AMOUNT after deposition of RS:", depositionAmt ," is:", balance01 + depositionAmt)
			
		
			if withDrawing == "Y":
				withDrawingAmt = int(input("ENTER THE AMOUNT TO BE WITHDRAW:"))
				print("AFTER withDrawing ", withDrawingAmt ,"YOUR ACCOUNT LEFT WITH RS:",balance01 - withDrawingAmt)

			print("thanks")

		elif pinCodeinput == pinCode02  :
			print("\nwelcome", name02 ,"\n your account number is :",acountnum02,"\n your balance is:",balance02)
			deposition = input("DO YOU WANT TO DEPOSITE MONEY(Y / N):")  
			deposition = deposition.upper()
			withDrawing = input("DO YOU WANT TO WITHDRAW MONEY FROM YOUR ACCOUNT(Y/N):")
			withDrawing = withDrawing.upper()
			if deposition == "Y":
				depositionAmt = int(input("ENTER THE AMOUNT FOR DEPOSITION:"))
				print("ok your new AMOUNT after deposition of ",depositionAmt," is:", balance02 + depositionAmt)
				
			if withDrawing == "Y":
				withDrawingAmt = int(input("ENTER THE AMOUNT TO BE WITHDRAW:"))
				print("AFTER withDrawing ",withDrawingAmt ,"YOUR ACCOUNT LEFT WITH:",balance02 - withDrawingAmt)
			
			print("thanks")

		elif pinCodeinput == pinCode03  :
			print("\nwelcome", name03 ,"\n your account number is :",acountnum03,"\n your balance is:",balance03)
			deposition = input("DO YOU WANT TO DEPOSITE MONEY(Y / N):")  
			deposition = deposition.upper()
			withDrawing = input("DO YOU WANT TO WITHDRAW MONEY FROM YOUR ACCOUNT(Y/N):")
			withDrawing = withDrawing.upper()
			if deposition == "Y":
				depositionAmt = int(input("ENTER THE AMOUNT FOR DEPOSITION:"))
				print("ok your new AMOUNT after deposition of ",depositionAmt," is:", balance03 + depositionAmt)
			
			if withDrawing == "Y":
				withDrawingAmt = int(input("ENTER THE AMOUNT TO BE WITHDRAW:"))
				print("AFTER withDrawing ",withDrawingAmt ,"YOUR ACCOUNT LEFT WITH:",balance03 - withDrawingAmt)
			
			print("thanks")

		elif pinCodeinput == pinCode04  :
			print("\nwelcome", name04 ,"\n your account number is :",acountnum04,"\n your balance is:",balance04)
			if deposition == "Y":
				depositionAmt = int(input("ENTER THE AMOUNT FOR DEPOSITION:"))
				print("ok your new AMOUNT after deposition of ",depositionAmt," is:", balance04 + depositionAmt)
			else:
				print("thanks")		
			if withDrawing == "Y":
				withDrawingAmt = int(input("ENTER THE AMOUNT TO BE WITHDRAW:"))
				print("AFTER withDrawing ",withDrawingAmt ,"YOUR ACCOUNT LEFT WITH:",balance04 - withDrawingAmt)
			
			print("thanks")

		elif pinCodeinput == pinCode05 :
			print("\nwelcome", name05 ,"\n your account number is :",acountnum05,"\n your balance is:",balance05)
			deposition = input("DO YOU WANT TO DEPOSITE MONEY(Y / N):")  
			deposition = deposition.upper()
			withDrawing = input("DO YOU WANT TO WITHDRAW MONEY FROM YOUR ACCOUNT(Y/N):")
			withDrawing = withDrawing.upper()
			if deposition == "Y":
				depositionAmt = int(input("ENTER THE AMOUNT FOR DEPOSITION:"))
				print("ok your new AMOUNT after deposition of ",depositionAmt," is:", balance05 + depositionAmt)
			

			if withDrawing == "Y":
				withDrawingAmt = int(input("ENTER THE AMOUNT TO BE WITHDRAW:"))
				print("AFTER withDrawing ",withDrawingAmt ,"YOUR ACCOUNT LEFT WITH:",balance05 - withDrawingAmt)
			
			print("thanks")	

		else :
			print("\n PLEASE ENTER VALID pinCode  \n")
			main()
	print("\n Thank you for using our ATM service \n")

#main function that hard coded the pincodes , names , account numbers and balance of five users
def main():
	list = [[5678,4089,4568,5987,2078],['AKRAM','ASLAM','UMAR','UMAIR','ASAD'],[52123376524,76583518768,12678945172,67728818265,87266266568],[20000,100000,890000,4500000,9080000]]
	pinCode = list[0]
	pinCode01 = pinCode[0]
	pinCode02 = pinCode[1]
	pinCode03 = pinCode[2]
	pinCode04 = pinCode[3]
	pinCode05 = pinCode[4]
	names     = list[1]
	name01    = names[0]
	name02    = names[1]        
	name03    = names[2]
	name04    = names[3]
	name05    = names[4]
	acountNums = list[2]
	acountnum01 = acountNums[0]
	acountnum02 = acountNums[1]
	acountnum03 = acountNums[2]
	acountnum04 = acountNums[3]
	acountnum05 = acountNums[4]
	balance     =list[3]
	balance01 = balance[0]
	balance02 = balance[1]
	balance03 = balance[2]
	balance04 = balance[3]
	balance05 = balance[4]
	
	
	
	atmSystem(pinCode,pinCode01,pinCode02,pinCode03,pinCode04,pinCode05,names,name01,name02,name03,name04,name05,acountNums,acountnum01,acountnum02,acountnum03,acountnum04,acountnum05,balance,balance01,balance02,balance03,balance04,balance05)


main()






















	
