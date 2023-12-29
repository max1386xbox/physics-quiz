print("this is physics quiz!\n")
socore = 0
qustions1 = input("The strengths of physics knowledge are ..... and .....? :")
if qustions1 == "testability and correcting physics theories" or qustions1 == "testability correcting physics theories" or qustions1 == "testing and correcting physics theories" or qustions1 == "testing correcting physics theories":
    print("correct")
    socore+=1
else :
    print("incorrect")
qustions2 = input("What is the unit of force in si? :")
if qustions2 == "kg.m/s**2" or qustions2 == "kg.m/s^2":
    print("correct")
    socore+=1
else :
    print("incorrect")
qustions3 = input("How many micrometers is one kilometer? :")
if qustions3 == "10**9" or qustions3 == "10^9" or qustions3 == "1000000000":
    print("correct")
    socore+=1
else :
    print("incorrect")
qustions4 = input("How accurate is the measurement? \n\n 38.789 :")
if qustions4 == "0.001" or qustions4 == "00.001":
    print("correct")
    socore+=1
else :
    print("incorrect")
qustions5 = input("A maximum of 272 grams of mercury can be poured into a container. How much water can be poured into that container? :")
if qustions5 == "20" or qustions5 == "20g" or qustions5 == "20grams":
    print("correct")
    socore+=1
else :
    print("incorrect")
print(f"this is your corect answer : {socore} and this is your socore {socore*20}%")