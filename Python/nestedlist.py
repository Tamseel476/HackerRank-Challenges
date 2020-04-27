'''
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format
The first line contains an integer,N , the number of students.
The  subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

Constraints:
2<= N <= 5
There will always be one or more students having the second lowest grade.

Output Format:

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input:

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output:

Berry
Harry
'''

if __name__ == '__main__':
    
    studentlist=[] #list to store name
    studentscore=[] #list to store score
    y=[]#list to storescore+name
    
    for _ in range(int(input())):
        name = input()
        studentlist.append(name)
        score = float(input())#student grade
        studentscore.append(score)

    s_score = sorted(list(set(studentscore)))#sorted score
    z = s_score[1] # z is 2nd lowest grade
    
    
    for i in range(len(studentscore)):
            if studentscore[i] == z:
                y.append(studentlist[i])
            

    x = sorted(y)
    for re in x:
        print(re)
