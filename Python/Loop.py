'''
PS: I have included 2 different variations of the loop
Task
Read an integer n. For all non-negative integers i < n, print i^2. See the sample for details.

Input Format

The first and only line contains the integer,n .

Constraints
1<= n <= 20

Output Format

Print n lines, one corresponding to each .

Sample Input:
5
Sample Output:

0
1
4
9
16
'''
def square(n):
    i=0
    while(i < n):
        print(i*i)
        i+=1

def square2(n):
    for i in range(n):
        print(i*i)



if __name__ == '__main__':
    n = int(input())
    square2(n)
