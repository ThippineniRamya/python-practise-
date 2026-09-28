'''Reverse a String'''
# s="python"
# rev=""
# for i in s:
#     if i not in rev:
#         rev=i+rev
# print(rev)
'''Check Palindrome'''
# s=input("enter your number")
# n=len(s)
# left=0
# right=n-1
# while left<right:
#     if s[left]!=s[right]:
#         print("not palindrome")
#         break
#     left+=1
#     right-=1
# else:
#     print("palindrom")
'''Count Characters  ,Input: hello,Output: 5'''
# str=input("enter your str")
# count=0
# for i in str:
#     count+=1
# print(count)

'''4. Count Vowels,Input: programming,Output: 3'''
# s="programming"
# c=0
# for i in s:
#     if i in "aeiou":
#         c+=1
# print(c)

'''5. Count Consonants       Input: hello,Output: 3'''
# s="programming"
# c=0
# for i in s:
#     if i not in "aeiou":
#         c+=1
# print(c)

'''# 6. Count Spaces  Input: python is easy   Output: 2'''
# s="python is easy"
# c=0
# for i in s:
#     if i.isspace():
#         c+=1
# print(c)

'''# 8. Remove Spaces  Input: python is easy   Output: pythoniseasy'''
# s=" python is easy "
# s.replace(" ","")
# print(s.replace(" ",""))

# s="python is easy"
# str=""
# for i in s:
#     if i!=" ":
#         str+=i
# print(str)
'''Count Number of Words      Input: Python is very easy  Output: 4'''
# s="Python is very easy"
# split=s.split()
# count=0
# for i in split:
#     count+=1
# print(count)
'''Find Longest Word   Input: Python programming is easy Output: programming'''
# s="Python programming is easy"
# longest=""
# for i in s.split():
#     if len(i)>len(longest):
#         longest=i
# print(longest)
'''Reverse Each Word  Input: python is easy Output: nohtyp si ysae'''
# s = "python is easy"
# result = " ".join(word[::-1] for word in s.split())
# print(result)

# s = "python is easy"
# word = ""
# result = ""
# for ch in s:
#     if ch != " ":
#         word += ch
#     else:
#         result += word[::-1] + " "
#         word = ""
# result += word[::-1]
# print(result)
'''reverse words order'''
# s="python is easy to learn"
# result = " ".join(s.split()[::-1])
# print(result)
'''Find Word with Maximum Vowels  Input: apple orange sky Output: orange'''
# s="apple orange sky"
# max=""
# vowel_count=0
# for i in s.split():
#     count=0
#     for ch in i:
#         if ch in "aeiou":
#             count+=1
#     if count>vowel_count:
#         vowel_count=count
#         max=i
# print(max)
'''Count Vowels in Each Word  Input: python is easy  Output:python → 1
is → 1
easy → 2'''
# s="python is easy"

# for i in s.split():
#     count=0
#     for ch in i:
#         if ch in "aeiou":
#             count+=1
#     print(f"{i}->{count}")
'''Count Letters and Digits Input: abc123'''
# s="abc123"
# count_l=0
# count_d=0
# for i in s:
#     if i.isalpha():
#         count_l+=1
#     else:
#         count_d+=1
# print(f"""count letter{count_l} 
# count digits {count_d}""")
'''freauency od each cahrectre'''
# s="hello"
# fre={}
# for i in s:
#     if i not in fre:
#         fre[i]=1
#     else:
#         fre[i]+=1
# print(fre)
'''Find Frequency of a Given Character  Input: programming, g Output: 2'''
# s="programming"
# target="g"
# count=0
# for i in s:
#     if i==target:
#         count+=1
# print(count)
'''Find Most Frequent Character Input: aabbccc Output: c'''
# s="aabbcccc"
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# max_freq=0
# max_word=""
# for  key in freq:
#     if freq[key]>max_freq:
#         max_freq=freq[key]
#         max_word=key
# print(max_word,max_freq)
'''rotate  a string right by one'''
# s="python"
# n=len(s)
# s=s[-1:]+s[0:n-1]
# print(s)
'''left by on position'''
# s = "python"
# s = s[1:] + s[0]
# print(s)
'''43. Right Rotate by K=2  Input: abcdef,    Output: efabcd'''
# s="abcdef"
# k=2
# n=len(s)
# k=k%n
# s=s[n-k:]+s[:n-k]
# print(s)
'''left rotate k=2'''
# s="abcdef"
# k=2
# n=len(s)
# k=k%n
# s=s[k:]+s[:k]
# print(s)
'''Check Whether One String Is Rotation of AnotherInput:
String 1: abcde
String 2: cdeab'''
# s1="abcde"
# s2="deabc"
# if len(s1)!=len(s2):
#     print("False") 
# double=s1+s1
# if s2 in double:
#     print("True")
# else:
#     print("false")
'''Check Palindrome Using Two Pointers     Input: racecar Output: Palindrome'''
# def palin(s):
#     is_palindrome=True
#     n=len(s)
#     l=0
#     r=n-1
#     while l<r:
#         if s[l]!=s[r]:
#             is_palindrome= False
#         l+=1
#         r-=1
#     return is_palindrome
# print(palin("racecar"))
'''Reverse String Using Two Pointers Input: abcdef  Output: fedcba'''
# str="abcdef"
# s=list(str)
# n=len(str)
# l=0
# r=n-1
# while l<r:
#     s[l],s[r]=s[r],s[l]
    
#     l+=1
#     r-=1
# print("".join(s))
'''Remove Duplicate Characters  Input: aabbcc  Output: abc'''
# s="aabbcc"
# dup=[]
# for i in s:
#     if i not in dup:
#         dup+=i
# print("".join(dup))
'''Check Whether Substring Exists
Input: programming
Substring: gram'''
# s="programming"
# sub="gram"
# if sub in s:
#     print("substring found")
# else:
#     print("not sub stringg")
'''Find First Occurrence
Input: hello
Character: l'''
# s="hello"
# char="l"
# for i in range(len(s)):
#     if s[i]==char:
#         print(i)
#         break
'''check anagram'''
# s1="silent"
# s2="listeeen"
# if sorted(s1)==sorted(s2):
#     print("anagram")
# else:
#     print("not  an anagram")

# from collections import Counter
# s1="listen"
# s2="silent"
# if Counter(s1)==Counter(s2):
#     print("it is a anagram")
# else:
#     print("not an anagram")
'''sum of digits in string abc123'''
# str="abc123"
# sum=0
# for i in str:
#     if i.isdigit():
#         sum+=int(i)
# print(sum)
'''Extract Numbers From String
Input: abc12def34
Output: 12 34'''
'''first occurence charter swiss'''
# s="swiss"
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# for i in freq:
#     if freq[i]==1:
#         print(i)
#         break
'''Character With Maximum Frequency
Input: mississippi
Output: i'''
# s="mississippi"
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# max=0
# max_word=""
# for i in freq:
#     if freq[i]>max:
#         max=freq[i]
#         max_word=i
# print(max,max_word)
'''minimum deletion made to make unique'''
# s="aabbcc"
# dup=[]
# for i in s:
#     if i not in dup:
#         dup.append(i)
# print(len(dup))
'''misising charecter'''
# s="abcdefghijklmnopqstuvwxyz"
# for i in "abcdefghijklmnopqrstuvwxyz":
#     if i not in s:
#         print(i)
'''find extra chaecter in two strings'''
# s1 = "abcde"
# s2 = "abxcde"

# for ch in s2:
#     if ch not in s1:
#         print(ch)
'''Longest Substring Without Repeating Characters'''
s = "abcabcbb"
left = 0
max_len = 0
seen = set()
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    max_len = max(max_len, right - left + 1)
print(max_len)
'''Longest Substring With K Distinct Characters'''
s = "aabacbebebe"
k = 3
left = 0
max_len = 0
freq = {}
for right in range(len(s)):
    freq[s[right]] = freq.get(s[right], 0) + 1
    while len(freq) > k:
        freq[s[left]] -= 1
        if freq[s[left]] == 0:
            del freq[s[left]]
        left += 1
    max_len = max(max_len, right - left + 1)
print(max_len)