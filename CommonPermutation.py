def common_permutation(s1, s2):
    # Count the frequency of characters in both strings
    count1 = [0] * 26
    count2 = [0] * 26
    for char in s1:
        count1[ord(char) - ord('a')] += 1
    for char in s2:
        count2[ord(char) - ord('a')] += 1
    
    # Find the common characters
    common_chars = []
    for i in range(26):
        common_chars += [chr(ord('a') + i)] * min(count1[i], count2[i])
    
    # Sort the common characters
    common_chars.sort()
    
    # Convert the common characters to a string
    return "".join(common_chars)

# Example usage
s1 = "pretty"
s2 = "women"
result = common_permutation(s1, s2)
print(result)  # Output: e

s3 = "walking"
s4 = "down"
result2 = common_permutation(s3, s4)
print(result2)  # Output: nw

s5 = "the"
s6 = "street"
result3 = common_permutation(s5, s6)
print(result3)  # Output: et
