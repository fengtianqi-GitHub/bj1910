import re

s1 = '/hello/122/34'
# print(re.match(r'/hello',s1))
# print(re.match(r'/hello/12',s1))
res = re.search(r'/hello/(\d+)/\d+',s1)
print(res)
print(res.group(1))