"""
https://leetcode.com/discuss/interview-question/351783/

Given a string, what is the minimum number of adjacent swaps required to convert a string into a palindrome. If not possible, return -1.

Practice online: https://www.codechef.com/problems/ENCD12

=================================================================================
Test Cases:
#1:
"mamad"
-> 3

#2:
"asflkj"
-> -1

#3:
"aabb"
-> 2

#4:
"ntiin"
-> 1
=================================================================================
Brute force:
1. Check if string is shuffled palindrome by checking:
    a. If length of the string is even, check if char counts are all even as well.
    b. If the length is odd, check if char counts are all even but one char with odd.
2. Use two pointers, start and end initialized at 0 and len(S) - 1, respectively:
    a. Compare S[start] == S[end]:
        a. If yes, start += 1 and end -= 1
        b. Else, starting from i = end - 1 to i == start:
            a. Check if S[i] == S[start]:
                a. If so, keep swapping S[i] with S[i + 1] until i + 1 == end.
                b. If not, swap S[start] with S[start + 1] and increment the swapCount
                    this is for the case when len(S) is odd and one character that
                    needs to go to the middle is at start position.
                    ie. asffskk -> saffskk

Time: O(N^2), N from checking palindrome and start to end traversal, another N from
    i = end to i = start.
Space: O(N)
=================================================================================
=================================================================================
"""
from collections import Counter

def min_num_swaps_palindrome(S):
    if not S or not is_shuffled_palindrome(S):
        return -1

    start, end = 0, len(S) - 1
    swap_count = 0
    S = list(S)
    print(S)
    while start < end:
        if S[start] != S[end]:
            i = end
            while i > start and S[start] != S[i]:
                i -= 1

            if i == start:
                S[start], S[start+1] = S[start+1], S[start]
                swap_count += 1
            else:
                while i < end:
                    S[i], S[i+1] = S[i+1], S[i]
                    swap_count += 1
                    i += 1
                start += 1
                end -= 1
        else:
            start += 1
            end -= 1
    return swap_count

def is_shuffled_palindrome(S):
    counters = Counter(S)
    is_even = len(S) % 2 == 0
    found_odd = 0
    for counter in counters.values():
        if is_even and counter % 2 == 1:
            return False

        if not is_even and found_odd == 1 and counter % 2 == 1:
            return False

    return True

print(min_num_swaps_palindrome("mamad"))
print(min_num_swaps_palindrome("asflkj"))
print(min_num_swaps_palindrome("aabb"))
print(min_num_swaps_palindrome("ntiin"))
