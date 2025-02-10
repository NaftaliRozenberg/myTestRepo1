weight=float(input("what is your weight? "))
height=float(input("what is your height? "))
BMI=weight / height ** 2
if (BMI   <18):
	print("underweight")
if (BMI >=18 and BMI <=25):
	print("normal weignt")
if (BMI >25 and BMI <=30):
	print("overweight")
if (BMI >30 and BMI <=35):
	print("grade 2 overweight")
if (BMI >35):
	print("danger to life")
print('tzvi zait')
