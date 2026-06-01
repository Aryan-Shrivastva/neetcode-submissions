class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        
        for op in operations:
            if op=="+":
                res+= stack[-1]+stack[-2]
                stack.append(stack[-1]+stack[-2])
            elif op=="D":
                res+=stack[-1]*2
                stack.append(stack[-1]*2)
            elif op=="C":
                res-=stack[-1]
                stack.pop()
            else:
                s = int(op)
                res+=s
                stack.append(s)
        
        return res
        