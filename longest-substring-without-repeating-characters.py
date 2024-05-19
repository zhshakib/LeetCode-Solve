def longest_substring(s: str) -> int:
    char_set = set()
    n = len(s)
    left = 0
    max_length = 0

    for right in range(n):
        if s[right] not in char_set:
            char_set.add(s[right])
            max_length = max(max_length, right-left+1)
        else:
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
    
    return max_length
    


ans: int = longest_substring("ACACACABAABA")

print(ans)