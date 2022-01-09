# #https://www.acmicpc.net/problem/17413
# import sys
#
# tmp=sys.stdin.readline().rstrip()
# stack=[]
# strstack=[]
#
# for value in tmp:
#     if value=='<':
#         stack.append(value)
#     elif value == '>':
#         stack.append(value)
#         print(''.join(stack))
#         stack.clear()
#     else:
#         if stack:
#             stack.append(value)
#         else:
