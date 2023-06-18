# ASSIGNMENT 1
string = input("Enter Your String: ")
number = int(input("Enter a Number: "))


res = [string[i: j] for i in range(len(string))
          for j in range(i + 1, len(string) + 1) if len(string[i: j])>=number and string[i: j][0]==string[i: j][-1] 
          ]
 

print(res)
