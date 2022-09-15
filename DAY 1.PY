'''exc 1

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

'''

num_finded = []
for i in range(2000,3200):
    if(i%7==0) and (i%5 != 0):
        num_finded.append(i)
# print(num_finded)


'''exc 2
Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320
'''
n = int(input())
def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
print(shortFact(n))

'''
With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included).
and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
'''
n = int(input())
ans={i : i*i for i in range(1,n+1)}
print(ans)

# raw_input = input('please enter numbers separated by comma:')

# Values = raw_input.split(",")
# t = tuple(Values)
# print(t)
