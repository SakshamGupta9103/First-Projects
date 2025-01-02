# The Currency Converter project

Currency={"USD to INR":83.0,"USD to EUR": 0.92,"USD to GBP": 0.78,"USD to JPY": 148.5,"USD to AUD": 1.55,"USD to CAD": 1.36,"USD to CHF": 0.89,"USD to CNY": 7.35,"USD to RUB": 98.0,"USD to ZAR": 18.7}

Convert_Currency=float(input("Enter the  Amount Currency you want to convert :  "))
Source_Currency=input("Enter The Source Currency  U have: ")
Target_Currency=input("Enter the Target Currency u want to convert  :   ")

Base_Currency={"USD":1,"INR":80,"EUR":0.92,"GBP":0.78}

if Source_Currency in Base_Currency and Target_Currency in Base_Currency:
    Converted_Amount = Convert_Currency * (Base_Currency[Target_Currency] / Base_Currency[Source_Currency])
    print(Converted_Amount)
else:
    print("Enter a valid currency from the available options.")

    











