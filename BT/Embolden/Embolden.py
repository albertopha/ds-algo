class Solution:
    def solve(self, text, patterns):
        if not text or not patterns:
            return text
        
        found = [False] * len(text)
        seen = set()

        for pattern in patterns:
            if pattern in seen:
                continue
            seen.add(pattern)

            i = 0
            while i < len(text):
                i = text.find(pattern, i)
                if i == -1:
                    break
                
                for j in range(i, i+len(pattern)):
                    found[j] = True
                
                i += 1
        
        output = []
        i = 0
        while i < len(text):
            if not found[i]:
                output.append(text[i])
                i += 1
                continue
            start = i
            while i < len(text) and found[i]:
                i += 1
            output.append('<b>%s</b>' %text[start:i])
        return "".join(output)

