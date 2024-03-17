#"abc" -> bac, cab, acb, bca, cba, abc
#3! = 1*2*3 = 6

#   bc   ->[bc, cb]  -> [abc, acb]  arr1 = [i + 1:]
#ac -> [ac, ca]  -> bac, bca arr1 = [:i]
#ab -> [ab, ba]  -> cab, cba arr1 = [:i + 1]

def per(arr:str) -> [str]:
    if len(arr) <= 1:
        return [arr]
    arr1 = []
    for i in range(len(arr)):
        arr2 = (per(arr[:i] + arr[i + 1:]))
        for j in range(len(arr2)):
              arr3 = arr[i] + arr2[j]
              arr1 +=[arr3]
    return arr1 


arr = "abc"
arr = per(arr)
print(arr)


#abcd -> a|b|cd, a|bc|d, a|bcd, abc|d, a|b|c|d
#bcd -> b|c|d , bc|d, b|cd

def perSticks(s):
    if len(s) < 2:
        return s
    
    arr1 = [s]
    for i in range(1, len(s)):
        arr_left = s[:i]
        arr_right = s[i:]
        arr2 = perSticks(arr_right)
        for j in arr2:
            arr3 = arr_left + "|" + j
            arr1 += [arr3]
    return arr1

arr = "abcd"
arr = perSticks(arr)
print(arr)