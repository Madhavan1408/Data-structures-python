prices=[8,4,6,2,3]
res=prices
stack=[]
for i in range(len(prices)):
    while stack and prices[i]<=prices[stack[-1]]:
        prev=stack.pop()
        res[prev]=abs(prices[prev]-prices[i])
    stack.append(i)
print(res)
        