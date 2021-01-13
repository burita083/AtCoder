# coding: UTF-8

# <<<基本的なimport系>>>
import sys
from sys import stdin
input = stdin.readline
import math
import bisect
# sys.setrecursionlimit(10**7)

# <<<定数系>>>
# ここは問題によって法を変える
MOD = 10**9+7
# MOD = 998244353
nil = None
INF = 10**18

# <<<配列系>>>
# 逆順の走査はreversed(range()):でオッケー
# 番号a~b配列のスライスは、l[a:b+1]
# １次元配列作成、値xをn個
def vec1(n,x):
    return [x]*n
# 2次元配列作成、値xをh行w列
def vec2(h,w,x):
    return [[x]*w for i in range(h)]
# 隣接リストはこちら：edge = [[] for _ in range(v)]
# 2次元配列aryのk番目で昇順ソート
def sort2up(ary,k):
    return sorted(ary, key=lambda x: x[k])
# 2次元配列aryのk番目で降順ソート
def sort2down(ary,k):
    return sorted(ary, reverse=True, key=lambda x: x[k])
# 配列の重複要素を除く（Rubyでいうuniq）
def uniq(ary):
    return list(set(ary))

# <<<二分探索系（必ずソートしてから使え！！！）>>>
# 配列aryにおけるx<aとなる要素xの個数：パターン１
def bsearch1(ary,a):
    return bisect.bisect_left(ary,a)
# 配列aryにおけるx<=aとなる要素xの個数：パターン２
def bsearch2(ary,a):
    return bisect.bisect_right(ary,a)
# 配列aryにおけるx>aとなる要素xの個数：パターン３
def bsearch3(ary,a):
    return len(ary)-bisect.bisect_right(ary,a)
# 配列aryにおけるx>=aとなる要素xの個数：パターン４
def bsearch4(ary,a):
    return len(ary)-bisect.bisect_left(ary,a)

# <<<数学系>>>
# 繰り返し二乗法
# ---> pow(底,累乗,MOD)の組み込み関数を使え！
# MODを指定した時のxの逆元
# ---> pow(x,-1,MOD)・・・ただしxとMODが互いに素でなければエラーが出る
# 組み合わせ(nCr)(MODをとっている)
def nCr(n,r):
    num = 1
    fact = 1
    for i in range(r):
        num = num * (n-i) % MOD
        fact = fact * (i+1) % MOD
    return num * pow(fact, MOD-2, MOD) % MOD
# 重複組み合わせ(nHr)(MODをとっている)
def nHr(n,r): # n個の異なるものからr個とってくる場合の数
    return nCr(n+r-1,r)
# 数字の各桁の合計を返す(負の数に対しては使えないので注意)
def digitsum(n):
    array = list(map(int, str(n)))
    return sum(array)
# 階乗を再帰で求める（このテンプレの上に再起上限変更テンプレがあるよ）
def kaijou(n):
    if n==0:
        return 1
    else:
        return n*kaijou(n-1)
# MOD付きの階乗を再帰で求める（このテンプレの上に再起上限変更テンプレがあるよ）
def kaijoumod(n):
    if n==0:
        return 1
    else:
        return (n*kaijou(n-1))%MOD

# <<<入出力系>>>
# 空白を開けて配列の要素を出力(要素は2個以上必要)
def pjoin1(ary):
    arynew = map(str, ary)
    print(" ".join(arynew))
# 敷き詰めて配列の要素を出力(要素は2個以上必要)
def pjoin2(ary):
    arynew = map(str, ary)
    print("".join(arynew))

# <<<反転系>>>
# リストの反転は、ary[::-1]
# 文字列の反転は、s[::-1]

###########################################################

