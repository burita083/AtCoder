S = input()
op_cnt = len(S) - 1
ops = []
ans = 0
for i in range(2 ** op_cnt):
    op = [""] * op_cnt 
    for j in range(op_cnt):
        if ((i >> j) & 1):
            op[op_cnt - 1 - j] = "+"
    formula = ""
    for p_n, p_o in zip(S, op + [""]):
        formula += (p_n + p_o)
    ans += eval(formula)

print(ans)
  