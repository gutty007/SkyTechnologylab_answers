#Sky Technology lab Q2 解答
#2022 7/31 提出締切
#正解でした

import math

NT=[int(s) for s in input().split(" ")]
N=NT[0]
T=NT[1]
count=0
count1=0

def counter(N,T_):
  #[1,T_-1]>>>[T_-1,1]
  if T_ <= N:
    count = T_-1
  #[T_-N,N]>>>[N,T_-N]
  else:
    count = 2*N-T_+1
  return count

if T == 3:
  count=8
#[1,?,?]
elif T-2*N <= 1 :
  #[1,1,T-2]
  if T-2 <= N:
    count1=9+3*(counter(N,T-1)-2)
  #[1,T-N-1,N]
  else:
    count1=3*counter(N,T-1)
  for i in range(min(T-2,N)):
    count += counter(N,T-1-i)
#[T-2N,N,N]
else:
  for i in range(3*N-T+1):
    count += counter(N,2*N-i)

count += count1

gcd=math.gcd(count,(N+1)**3)

print("{}/{}".format(int(count/gcd),int(((N+1)**3)/gcd)))

