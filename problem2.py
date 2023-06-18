#ASSIGNMENT 2
s='sHQen}'
list=[ord(v) for v in s]
pre_flag=False
next_flag=False

for i in range(len(list)):
    current=list[i]
    if list[i]%2==0:
        if next_flag==False:
            next=list[i+1]
            updated=current%7+next
            list[i+1]=updated
            if updated <32 or updated>126:
                updated=83
            next_flag=True
        else:
            pre_flag=False
            next_flag=False
    else:
        if i==0:
            continue
        else:
            if pre_flag==False:
                prev=list[i-1]
                updated=prev-current%5
                if updated <32 or updated>126:
                    updated=83
                list[i-1]=updated
                pre_flag=True
            else:
                pre_flag=False
                next_flag=False

new_str=''
for ele in list:
    new_str=new_str+chr(ele)

print(new_str)