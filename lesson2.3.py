a = 'ABCA1AAC'
def strcounter(a): #O(n**2)
    for char in a:
        counter = 0
        for sub_chur in a:
            if char == sub_chur:
                counter+=1
        print(char,counter)
strcounter(a)
def strcounter1(a):   #O(N*M)
    for char in set(a):
        counter = 0
        for sub_chur in a:
            if char == sub_chur:
                counter+=1
        print(char,counter)
strcounter1(a)
def strcounter2(a):   #O(N*0)
    syms_counter = {}
    for char in a:
        syms_counter[char] = syms_counter.get(char, 0)+1
    print(syms_counter)
strcounter2(a)
#новый код