class MyCalculator:
    # create new lists for numbers and operators
    @staticmethod
    def num_split(calc_list):
        num = []
        for i in calc_list[0:len(calc_list):2]:
            element = float(i)
            num.append(element)
        return num


    # create new lists for operators
    @staticmethod
    def op_split(calc_list):
        operator = []
        for n in calc_list[1:len(calc_list) - 1:2]:
            operator.append(n)
        return operator


    # terminates the program if user types end
    @staticmethod
    def terminate(calc_input):
        if calc_input == "END" and "End" and "end":
            print("The program has been terminated")
        else:
            return True


    # looks for the index of the operator
    @staticmethod
    def get_op_index(op_list, f):
        return [i for (i, v) in enumerate(op_list) if v == f]


    # multiplication function
    @staticmethod
    def multi(num_split, op_split):
        num_multi = []
        num = num_split
        op_new = op_split
        op = MyCalculator.get_op_index(op_new, "*")
        for i in op:
            num_multi.append(num[i] * num[i + 1])
        for n in op:
            num[n] = num_multi[op.index(n)]
        for index in sorted(op, reverse=True):
            del num[index + 1]
        for index in sorted(op, reverse=True):
            del op_new[index]
        return op_new, num


    # divide function
    @staticmethod
    def divide(num_split, op_split):
        num_divide = []
        num = num_split
        op_new = op_split
        op = MyCalculator.get_op_index(op_new, "/")
        for i in op:
            num_divide.append(num[i] / num[i + 1])
        for n in op:
            num[n] = num_divide[op.index(n)]
        for d in sorted(op, reverse=True):
            del num[d + 1]
        for d in sorted(op, reverse=True):
            del op_new[d]
        return op_new, num


    # add function
    @staticmethod
    def add(num_split, op_split):
        num_add = []
        num = num_split
        op_new = op_split
        op = MyCalculator.get_op_index(op_new, "+")
        for i in op:
            num_add.append(num[i] + num[i + 1])
        for n in op:
            num[n] = num_add[op.index(n)]
        for d in sorted(op, reverse=True):
            del num[d + 1]
        for d in sorted(op, reverse=True):
            del op_new[d]
        return op_new, num


    # subtraction function
    @staticmethod
    def subtract(num_split, op_split):
        num_subtract = []
        num = num_split
        op_new = op_split
        op = MyCalculator.get_op_index(op_new, "-")
        for i in op:
            num_subtract.append(num[i] - num[i + 1])
        for n in op:
            num[n] = num_subtract[op.index(n)]
        for d in sorted(op, reverse=True):
            del num[d + 1]
        for d in sorted(op, reverse=True):
            del op_new[d]
            print(num)
        return op_new, num


    # order of operations in an equation to execute one number
    @staticmethod
    def evaluate():
        num_split = MyCalculator.num_split(MyCalculator.calc_list)
        op_split = MyCalculator.op_split(MyCalculator.calc_list)
        op_split, num_split = MyCalculator.multi(num_split, op_split)
        op_split, num_split = MyCalculator.divide(num_split, op_split)
        op_split, num_split = MyCalculator.add(num_split, op_split)
        op_split, num_split = MyCalculator.subtract(num_split, op_split)
        return num_split[0]