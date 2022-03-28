def bigMod(a,b,M):
    if b==0:
        return 1 % M
    x = bigMod(a, b//2, M)
    x = (x*x) % M
    if b%2==1:
        x = (x * a) % M
    return x

while True:
  try:
    a = int(input())
    b = int(input())
    M = int(input())
    
    # a,b,M = map(int, input().split())
    
    print(bigMod(a,b,M))
    input()
  except(EOFError):
    break

'''
int big_mod(int base, int power, int mod)
{
    if(power==0)    return 1;
    //কোন কিছুর power 0 হলে তার মান 1 হয়ে যায়
    else if(power%2==1) //power বেজোড় হলে
    {
        int p1 = base % mod;
        int p2 = (big_mod(base,power-1,mod))%mod;
        return (p1*p2)%mod;
    }
    else if(power%2==0) //power জোড় হলে
    {
        int p1 = (big_mod(base,power/2,mod))%mod;
        return (p1*p1)%mod;
    }
}
'''
