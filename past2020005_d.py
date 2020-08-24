N = int(input())
s1= input()
s2= input()
s3= input()
s4= input()
s5= input()
v1 = [s1[i: i+4] for i in range(0, len(s1), 4)]
v2 = [s2[i: i+4] for i in range(0, len(s2), 4)]
v3= [s3[i: i+4] for i in range(0, len(s3), 4)]
v4= [s4[i: i+4] for i in range(0, len(s4), 4)]
v5= [s5[i: i+4] for i in range(0, len(s5), 4)]


d = {}

d[".###.#.#.#.#.#.#.###"] = 0
d["..#..##...#...#..###"] = 1
d[".###...#.###.#...###"] = 2 
d[".###...#.###...#.###"] = 3 
d[".#.#.#.#.###...#...#"] = 4 
d[".###.#...###...#.###"] = 5 
d[".###.#...###.#.#.###"] = 6
d[".###...#...#...#...#"] = 7
d[".###.#.#.###.#.#.###"] = 8
d[".###.#.#.###...#.###"] = 9
for x1, x2, x3, x4, x5 in zip(v1, v2, v3, v4, v5):
  s = x1+x2+x3+x4+x5
  if s == ".....":
    continue
  else:
    print(d[s], end="")