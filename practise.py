# lst=[12,5,27,9,18]
# print(max(lst))
# lst=[12,5,27,9,18]
# large=lst[0]
# for i in lst:
#     if i >large:
#         large=i
# print(large)

# lst=[4,7,4,9,7,7,2]
# n=len(lst)
# seen=set()
# for i in lst:
#     if i not in seen:
#         seen.add(i)
# print(seen)

# lst=[2,8,11,3]
# target=14
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]+lst[j]==target:
#             print(lst[i],lst[j])

# arr=[0,5,0,3,8,0]
# lst=[]
# for i in arr:
#     if i!=0:
#         lst.append(i)
# for i in arr:
#     if i==0:
#         lst.append(i)
# print(lst)

# lst=[10,5,20,30,8,3]
# largest=lst[0]
# second_large=lst[0]
# for i in lst:
#     if i >largest:
#         second_large=largest
#         largest=i
#     elif i>second_large and i!=largest:
#         second_large=i
# print(second_large)

# tup1=(4,7,2,9)
# tup2=(5,2,7,8)
# common=[]
# for i in tup1:
#     if i in tup2:
#         common.append(i)
# print(common)

# tuple = ('java', 'python', 'sql', 'java') 
# target = 'sql'

# for i in range(len(tuple)): 
#     if tuple[i] == target: 
#         print("target at index",i)

# elements=(2,3,2,5,3,2)
# freq={}
# for i in elements:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq)

# def tup(arr):
#     ispalin=True
#     l=0
#     r=len(arr)-1
#     while l<r:
#         if arr[l]!=arr[r]:
#             ispalin=False
#             break
#         l+=1
#         r-=1
#     return ispalin
# arr=(1,2,3,2,1,5)
# print(tup(arr))

# t = (14, 3, 27, 8, 19)

# smallest = t[0]
# largest = t[0]

# for num in t:
#     if num < smallest:
#         smallest = num

#     if num > largest:
#         largest = num

# print((smallest, largest))

# marks = {"A": 70, "B": 85, "C": 90, "D": 75}
# sum=0
# for value in marks.values():
#     sum+=value
# avg=sum/len(marks)
# print(avg)
'''hignt value key'''
# scores = {"Asha": 78, "Ravi": 91, "Meena": 85}

# highest = 0
# highest_key = ""

# for key, value in scores.items():
#     if value > highest:
#         highest = value
#         highest_key = key

# print(highest_key)

'''count even values'''
# d = {"a": 10, "b": 15, "c": 20, "d": 25}
# c=0
# for value in d.values():
#     if value%2==0:
#         c+=1
# print(c) 
'''fre fro str'''
# s = "programming"
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq)

'''most frequent charecter'''
# s = "banana"
# count = {}
# for char in s:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1
# highest = 0
# most_frequent = ""

# for char, value in count.items():
#     if value > highest:
#         highest = value
#         most_frequent = char

# print(most_frequent)
'''non repeating charector'''
# s = "aabbcde"
# count={}
# for i in s:
#     if i not in count:
#         count[i]=1
#     else:
#         count[i]+=1
# for i in s:
#     if count[i]==1:
#         print(i)
#         break
'''merge two dictonary'''
# d1 = {"a": 10, "b": 20}
# d2 = {"c": 30, "d": 40}
# res={}
# # result = {**d1, **d2}# unpacking in dict

# # print(result)
# for key,value in d1.items():
#     res[key]=value
# for key,value in d2.items():
#     res[key]=value
# print(res)
'''mege common key and add values '''
# d1 = {"a": 10, "b": 20, "c": 30}
# d2 = {"b": 5, "c": 10, "d": 15}
# result = {}
# for key, value in d1.items():
#     result[key] = value
# for key, value in d2.items():
#     if key in result:
#         result[key] += value
#     else:
#         result[key] = value
# print(result)
'''Find Common Keys'''
# d1 = {"a": 10, "b": 20, "c": 30}
# d2 = {"b": 5, "c": 10, "d": 15}
# comm=[]
# for key in d1:
#     if key in d2:
#         comm.append(key)
# print(comm)
'''invert dictinary'''
# d = {"a": 1, "b": 2, "c": 3}
# res={}
# for key, val in d.items():
#     res[val]=key
# print(res)
'''remove duplicate values'''
# d = {"a": 10, "b": 20, "c": 10, "d": 30}
# result = {}
# for key, value in d.items():
#     if value not in result.values():
#         result[key] = value

# print(result)
'''second highest val'''
# d = {"A": 80, "B": 95, "C": 70, "D": 90}
# high=0
# second=0
# for value in d.values():
#     if value>high:
#         second=high
#         high=value
#     elif value>second and value!=second:
#         second=value
        
# print(second)

# str="50,6,5"
# split=str.split(",")
# total_banana=int(split[0])
# total_monkey=int(split[1])
# total_picy=int(split[2])
# distributed_as_picky=total_picy*5
# print(f"distributed_as_picky{distributed_as_picky}")
# rest=total_banana-distributed_as_picky
# print(f"rest:{rest}")
# share=rest/2
# print(f"each:{share}")
# total=distributed_as_picky+rest
# print(f"total is {total}")


# data = "apple,banana,[20,150],[30,50]"

# split = data.split(",")
# print(split)
# apple_quantity = int(split[2].replace("[", ""))
# # print(apple_quantity)
# apple_price = int(split[3].replace("]", ""))

# apple_cost = apple_quantity * apple_price
# bana_naquantity = int(split[4].replace("[", ""))
# bana_price = int(split[5].replace("]", ""))
# bana_cost=bana_naquantity*bana_price
# print(f"apple cost:{apple_cost}")
# print(f"bana cost:{bana_cost}")
