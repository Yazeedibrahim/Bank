import time
import colorama
from colorama import Fore,Style
print("Hint: Pin = (12345) ")
print(Fore.CYAN + "      ##############################################")
print("      ##      UNION BANK LIMITED(U•B•L)NIGERIA    ##")
print("      ##############################################" + Style.RESET_ALL)
print(Fore.GREEN + "          @WELLCOME TO UNION BANK LIMITED(U•B•L)@")
print("____________________________________________________________")
print("____________________________________________________________")
print("____________________________________________________________")
print("                        OPTIONS")
print("                    ______________\n")
pin = 12345
price = 1000000
a = "1. My balance"
b = "2. Airtime/Data"
c = "3. Transfer"
e = "4. Pay Bills"
f = "5. Loans"
g = "6. Cardless Transfer"
h = "7. Other Services\n"
i = "8. Exit"
print(a)
print(b)
print(c)
print(e)
print(f)
print(g)
print(h)
print(i,"\n")
k =int(input("Select an option : "))
if k == 1:
	print('you enter option ',a)
	print("Enter your pin number ,")
	z =int(input())
	if z == pin:
		print("Processing......")
		time.sleep(2)
		print("Your account balance is>>$\n",price)
	else:
			print("Processing..........")
			time.sleep(2)
			print(Fore.RED + "Error: Incorrect pin number,Try again" + Style.RESET_ALL)
if k == 2:
	print('you enter option ',b)
	m =int(input("Enter a phone number "))
	z =int(input('Enter your pin '))
	if z == pin:
	  print("Processing........")
	  time.sleep(2)
	  print("Airtime/Data is succesfully sent to ",m)

if k == 3:
	print('You enter option ',c)
	m =int(input('Enter account number: 1 '))
	q = input('Enter the bank name: ')
	n =int(input('Enter amount $ '))
	z =int(input('Enter your pin: '))
	if z == pin:
		print("Processing.......")
		time.sleep(2)
		print('$',n,'has been sent succesfully to ' , m, q)
if k == 4:
	nepa = "1 Electricity Bill"
	card = "2 Enternet Bill"
	tv = "3 TV Bill"
	print(nepa)
	print(card)
	print(tv)
	sel =int (input("Select a bill : "))
	pas = int(input("Enter a PIN : "))
	if sel == 1:
		if pas == pin:
				print("Processing........")
				time.sleep(2)
				print("Q#: ox street :>> Electricity  is paid succesfully")
		else:
			print(Fore.RED + "Error: Incorrect pin number,Try again" + Style.RESET_ALL)
	if sel == 2:
		if pas == pin:
			print("Processing........")
			time.sleep(2)
			print("NUM: 070629664 :>> Internet is paid succesfully")
		else:
			print(Fore.RED + "Error: Incorrect pin number,Try again" + Style.RESET_ALL)
	if sel == 3:
		if pas == pin:
			print("Processing.......")
			time.sleep(2)
			print("Quart 4HD :>> tv is paid succesfully")
		else:
			print(Fore.RED + "Error: Incorrect pin number,Try again" + Style.RESET_ALL)
		
if k == 5:
	print("options")
	print("1 apply for a loan")
	print("2 paid a loan")
	ses = int(input("Select > "))
	if ses == 1:
		am = int(input("Enter your pin :"))
		if am == pin:
			print("Processing..........")
			time.sleep(2)
			amount = int(input("Enter the amount :"))
			print("Processing........")
			time.sleep(2)
			print("$",amount,"Send succesfull your total amount is $",amount+price)
		else:
			print(Fore.RED + "Error: Incorrect pin number,Try again" + Style.RESET_ALL)
	if ses == 2:
		print("Please visit any union bank close to you to pay the loan, thanks")