import math

def solution(S):
    occurrences = [0] * 26

    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1
    print(occurrences)
    best_char = 'a'
    best_res = 0

    for i in range(26): # Starting i at 1 will skip 'a'
        if occurrences[i] > best_res: # Removing equal sign will keep the earliest alphabetical character
            best_char = chr(ord('a') + i)
            best_res = occurrences[i]

    return best_char

if __name__ == "__main__":
    print(solution("aaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzz"))
    # print(2**1000)
    # print(1000*2)
    # print(math.factorial(1000) > 2**1000)

