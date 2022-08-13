from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if not secret or not guess:
            return ''
        
        secret_counter = Counter(secret) 
        bulls, cows = 0, 0
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                secret_counter[secret[i]] -= 1
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                continue
            
            if guess[i] in secret_counter and\
                secret_counter[guess[i]] > 0:
                cows += 1
                secret_counter[guess[i]] -= 1
        return '%iA%iB' % (bulls, cows)
