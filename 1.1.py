S0=2.846
K=2.75
T=0.56
r=0.05
sigma=0.1524
from numpy import *
I=100000
z=random.standard_normal(I)
ST=S0*exp((r-0.5*sigma**2)*T+sigma*sqrt(T)*z)
hT=maximum(ST-K,0)
C0=exp(-r*T)*sum(hT)/I
print(C0)