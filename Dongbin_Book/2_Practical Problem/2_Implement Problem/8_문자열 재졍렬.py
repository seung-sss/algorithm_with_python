import sys

# 내 풀이
# s = sys.stdin.readline().rstrip()
# number = 0
# char = ""
#
# for val in s:
#     if ord('1') <= ord(val) <= ord('9'):
#         number += int(val)
#     else:
#         char += val
#
# char = sorted(char)
# res = ''
#
# for val in char:
#     res += val
#
# print(res + str(number))

# 책 풀이 방법
data = sys.stdin.readline().rstrip()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))