print("сортировка пузырьком")
list1=[243,18,280,365,264,732,570,720,208,716,96,341,763,560,698]
for i in range(0,len(list1)):
    for j in range(0,len(list1)-1):
        if list1[j] > list1[j+1]:
            temp =list1[j]
            list1[j] =list1[j+1]
            list1[j+1] = temp
for i in range(0,len(list1)):
    print(list1[i])
print("сортировка вставка")
list2=[898,966,434,750,570,744,560,945,166,728,325,923,604,781,226]
for i in range (len(list2)):
    temp=list2[i]
    j=i
    while(j>0 and list2[j-1]>temp):
        list2[j]=list2[j-1]
        j=j-1
    list2[j]=temp
print(list2)
print("сортировка выбором")
list3=[167,582,352,68,259,755,717,482,936,427,383,143,992,349,805]
length_list3 = len(list3)
i = 0
while i < length_list3-1:
    m = i
    j = i+1
    while j<length_list3:
        if list3[j] < list3[m]:
            m=j
        j += 1
    list3[i], list3[m] = list3[m], list3[i]
    i += 1
print(list3)