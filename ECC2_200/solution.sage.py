# This file was *autogenerated* from the file solution.sage
from sage.all_cmdline import *   # import sage library
_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_56027910981442853390816693056740903416379421186644480759538594137486160388926 = Integer(56027910981442853390816693056740903416379421186644480759538594137486160388926); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_129 = Integer(129); _sage_const_5729 = Integer(5729); _sage_const_13993 = Integer(13993); _sage_const_1730599 = Integer(1730599); _sage_const_25255205054024371783896605039267101837972419055969636393425590261926131199030 = Integer(25255205054024371783896605039267101837972419055969636393425590261926131199030); _sage_const_93556643250795678718734474880013829509320385402690660619699653921022012489089 = Integer(93556643250795678718734474880013829509320385402690660619699653921022012489089); _sage_const_0 = Integer(0); _sage_const_61124499720410964164289905006830679547191538609778446060514645905829507254103 = Integer(61124499720410964164289905006830679547191538609778446060514645905829507254103); _sage_const_2595146854028317060979753545310334521407008629091560515441729386088057610440 = Integer(2595146854028317060979753545310334521407008629091560515441729386088057610440); _sage_const_66001598144012865876674115570268990806314506711104521036747533612798434904785 = Integer(66001598144012865876674115570268990806314506711104521036747533612798434904785); _sage_const_224 = Integer(224); _sage_const_65533262933617146434438829354623658858649726233622196512439589744498050226926 = Integer(65533262933617146434438829354623658858649726233622196512439589744498050226926)
from sage.all import *

M = _sage_const_93556643250795678718734474880013829509320385402690660619699653921022012489089 
F = GF(M)
A = _sage_const_66001598144012865876674115570268990806314506711104521036747533612798434904785 
B = _sage_const_25255205054024371783896605039267101837972419055969636393425590261926131199030 
Px = F(_sage_const_56027910981442853390816693056740903416379421186644480759538594137486160388926 )
Py = F(_sage_const_65533262933617146434438829354623658858649726233622196512439589744498050226926 )
Qx = _sage_const_61124499720410964164289905006830679547191538609778446060514645905829507254103 
Qy = _sage_const_2595146854028317060979753545310334521407008629091560515441729386088057610440 

E = EllipticCurve(F, [A, B])

P = E(Px, Py)
Q = E(Qx, Qy)

_order = order(E)
factors = [f[_sage_const_0 ]*f[_sage_const_1 ] for f in factor(_order)]
l = []

# for factor in factors:
#     t = int(_order / factor)
#     tP = t*P
#     tQ = t*Q
#     for j in range(factor):
#         if j*tP == tQ:
#             print j*tP
#             l.append(j)
#             break
#     print l

l = [_sage_const_2 , _sage_const_1 , _sage_const_4 , _sage_const_1 , _sage_const_129 , _sage_const_224 , _sage_const_5729 , _sage_const_13993 , _sage_const_1730599 ]
n = crt(l, factors[:_sage_const_9 ])
print n
assert P*n == Q

# vim: set ft=python: