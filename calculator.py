state = true
while state :
mode = input ("for scientific_mode --->1  for programmer_mode--->2  for exit----->0")
if mode == 1
num1 = int(input("num1"))
num2 = int(input("num2"))
operator = input("operator")
scientific_mode = {
	"+" : num1+num2,
	"-" : num1-num2,
	"*" : num1*num2,
	"/" : num1/num2
	}
	print(scientific_mode[operator])
}
elif mode == 2
num = int(input(" num"))
programmer_mode = {
    "bin" :bin(num),
	"hex" :hex(num),
	"oct" :oct(num) 
	print(programmer_mode[operator])
}
elif mode == 0
    state=False
else
    print(wrong input)