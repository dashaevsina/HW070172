# This is an interactive Python calculator program.

print("This is an interactive calulator.")
print("Please enter your calculations below.") 

def main():
    for i in range(100):
        calculation = eval(input(""))
        print(calculation)

main()