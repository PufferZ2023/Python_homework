#s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"


unique_chars = list(set(s))


unique_chars.sort()


sorted_string = ''.join(unique_chars)

print(sorted_string)
