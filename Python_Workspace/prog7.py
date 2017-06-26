spy_list = []
while len(spy_list)<4:
    spy_list.append(raw_input("Enter the spy name : "))
print spy_list[:]
print spy_list
i=0
while i<len(spy_list):
    print spy_list[i]
    i=i+1
for name in spy_list:
    print name