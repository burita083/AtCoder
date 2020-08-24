import sys
import requests

def main(argv):
  if len(argv) == 0:
    print("引数が1つもないです。")
    exit(1)
  if len(argv) == 1:
    print("引数が1つしか存在しません。")
    exit(1)
    
  n = argv[1]
  if type(n) != str:
    print("第２引数の型がstrではありません。")
    exit(1)

  if len(argv) >= 3:
    print("引数は2つです。")
    exit(1)
   
  print(f(int(n)))

MAX = 100007
memo = [0]*MAX
def f(n):
  if n == 0:
    return 1

  if n == 2:
    return 2

  if n % 2 == 0:
    if memo[n] != 0:
      return memo[n]
    memo[n] = f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4)
    return memo[n]
  else:
    if memo[n] != 0:
      return memo[n]

    memo[n] = askServer(n)
    return memo[n]

def askServer(n):
  response = requests.get(
        'http://challenge-server.code-check.io/api/recursive/ask', 
        params={'seed': '2b89f-4862-4814-8728-ddb0b36076ba', "n": n})
  return response.json()["result"]

     
if __name__ == '__main__':
    main(sys.argv[1:])
