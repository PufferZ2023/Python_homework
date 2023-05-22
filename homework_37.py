#正则表达式匹配中，（.*）和（.*?）匹配区别？
s="<a>哈哈</a><a>呵呵</a>"
import re
res1=re.findall("<a>(.*)</a>", s)
print("贪婪匹配",res1)
res2=re.findall("<a>(.*?)</a>", s)
print("非贪婪匹配",res2)