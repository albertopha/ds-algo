"""
https://www.geeksforgeeks.org/minimum-characters-that-are-to-be-inserted-such-that-no-three-consecutive-characters-are-same/

Given a string str and the task is to modify the string such that no three consecutive characters are same. In a single operation, any character can be inserted at any position in the string. Find the minimum number of such operations required.
=====================================================================
Test cases
#1
"aabbbcc"
-> aabbabcc

#2
"aaabbbccc"
-> aababbabccac
=====================================================================
Brute force:
1. Iterate through the string from i = 0 to i = len(S) - 1:
    a. Increment the count if S[i] == S[i+1]
    b. If the count == 3:
        a. insert next available character (ie. "a" -> "b", "z" -> "a")

Time: O(N)
Space: O(N)
=====================================================================
=====================================================================
"""
def min_inserted(S):
    if not S:
        return 0

    result = []
    count = 1
    inserted_count = 0
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            count += 1
        else:
            count = 1

        result.append(S[i])

        if count == 3:
            if S[i] == 'z':
                result.append("a")
            else:
                result.append(chr(ord(S[i]) + 1))
            inserted_count += 1
            count = 1

    result.append(S[-1])
    print("".join(result))
    return inserted_count

print(min_inserted("aabbbcc"))
print(min_inserted("aaaabbbccc"))
print(min_inserted("aaaaabbbbbcbccc"))

