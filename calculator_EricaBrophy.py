


#function executes operation desired in equation
def calc_solver(calc_LHS, calc_RHS,op):
    if op == "+": 
        result = sum(calc_LHS, calc_RHS)
        return result
    elif op == "-":
        result = calc_LHS - calc_RHS
        return result
    elif op == "*":
        result = calc_LHS * calc_RHS
        return result
    elif op == "/":
        calc_LHS / calc_RHS
        return result 

#function will search for operator 
def op_search(calc_input,op):
    op_position=calc_input.find(op)
    if op_position != -1:
        calc_LHS= calc_input[0:op_position]    #calculates left hand side of the equation before the operator
        calc_RHS= calc_input[(op_position + 1):] #calculates right hand side of the equation before the operator

        return (calc_LHS,calc_RHS)
    else:
        return 0 

#user inputs equation 
calc_input = input("Enter your equation that you would like the calculator to solve: ")

#defined list of operators
op = ["*","/","+","-"] 


for item in op: 
    if op_search(calc_input, op) == 0:
        pass
    else: 
        int(calc_LHS), calc_RHS= op_position(calc_input, item)

        #calculate LHS
        calc_input=calc_solver(calc_LHS,int(calc_RHS),op)


while (error == False):
    for i in calc_input:
        if i == " ":
        print("You have an error. Remove spaces in equation.")
        error = True
else:
    print("No more error.")

#calc_input=2+3+5~

def recursion(calc_LHS,calc_RHS):
    if item in calc_input == "~" #want to tag ~ to the end of all user input equations to run recursion loop
        return calc_input
    else: 
        #something

        #currently base case is going to return the calc_RHS and then work backwards























# def calc_solver():
#     calc_input = input("Enter your equation that you would like the calculator to solve: ")
#     calc_list = []
#     for i in calc_input:
#         calc_list.append(i)
#     print(calc_list)
#     return calc_list
# calc_solver()




#
#    for i in calc_list:
#         if i == "+":
#             left_side, right_side = calc_list.split("+", 1)
#         elif i == "-":
#             left_side, right_side = calc_list.split("+", 1)
#     print(left_side)
#     print(right_side)
# calc_solver()


# left_side = []
# right_side = []
# allows user to enter equation to calculate
# def calc_solver():

#     calc_input = input("Enter your equation that you would like the calculator to solve: ")
#     for i in calc_input:
#         if i == "+":
#             left_side, right_side = calc_input.split("+", 1)
#         elif i == "-":
#             left_side, right_side = calc_input.split("+", 1)
#     return (left_side, right_side)
# calc_solver()
# print(left_side)
# print(right_side)

# left_side = []
# right_side = []
# if i == "+":
#         left_side, right_side = calc_input.split("+", 1)
#     elif i == "-":
#         left_side, right_side = calc_input.split("+", 1)
# return (left_side, right_side)


# calc_input = input("Enter your equation that you would like the calculator to solve: ")
# def calc_solver(): #defines function with parameter of user input
#     calc_list = []
#     for i in calc_input: #creates a for loop for each index of the user input
#         calc_list.append(i) #creates a separate string for each item in the user input list
#         print(calc_list)  # prints the list
#     return calc_list #returns this list back to the function
# calc_solver()  # calls the function


#     for i in range(calculator_list):
#         if i == "+":
#             calculator_list.append(i)
#             left_side=eval(calc_list,i-1)
#             right_side=eval(calc_list,i+1)
#     return sum(left_side,right_side)
# print(sum(left_side,right_side))


