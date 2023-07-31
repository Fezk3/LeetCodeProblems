
def find_common_prefix(pattern1, pattern2):
    i = 0
    while i < min(len(pattern1), len(pattern2)) and pattern1[i] == pattern2[i]:
        i += 1
    return pattern1[:i]

def min_wildcards_for_intersecting_patterns(regex_patterns):
    n = len(regex_patterns)
    unique_chars = set()

    for i in range(n):
        for j in range(i + 1, n):
            common_prefix = find_common_prefix(regex_patterns[i], regex_patterns[j])
            for char in regex_patterns[i][len(common_prefix):]:
                unique_chars.add(char)
            for char in regex_patterns[j][len(common_prefix):]:
                unique_chars.add(char)

    return len(unique_chars)