import math
import matplotlib.pyplot as plt
import numpy as np
# a = 9
# m =1500
# z0 = 10116352
# loop = 20
rataRata1 = 15.522
rataRata2 = 17.944
pencucian = 7
mNormal  =1600 
simpangan = 72.689
z = 100
n1 = 90
rataRataSemua =  rataRata2 / n1

a  = int(input('faktor konstanta pengali (a): '))
m  = int(input('faktor pembagi modulus (m): '))
z0 = int(input('Kunci pembangkit (Z0): '))
loop = int(input('berapa kali pengulangan ? '))


z_1i = z0



print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
print('|        | waktu    |pencucia    |    Waktu       | Kumulatif     |    Waktu        |    Waktu        |')
print('|  No.   |kedatangan|Rambut      |   Kedatangan   | Kedatangan    |  Pemotongan     |   Selesai       |')
print('|        |pelanggan |            |                |               |                 |  Dialayani      |')
print('|        |     A    |       B    |        C       |       D       |       E         |        F        |')
print('-------------------------------------------------------------------------------------------------------------------------------------------------')

for i in range(loop):
    # rumus multipicative
    zi = ((a * z_1i)  % m) 
    z_1i = zi   
    u = zi / m
    b = pencucian
    c = (-rataRata2*math.log(u))     #eksponensial 
    d = c
    e = 100
    f =b+c+d
    x = rataRata2+z
    ln = -2*math.log(u)   #normal
    # sin = (sin(math.pi*2*u))
    kumKedatangan = c+d
    # x = 95.262
    z = 1.097
    x = (x+(rataRata1+(simpangan*z)))
    rambut = (rataRata1+simpangan)

    plt.plot(c)
    plt.show()
  
    print('|{} \t'.format(i+1),'|{:.3f}\t   '.format(u),'|   {}\t'.format(b),'|    {:.3f}\t '.format(c),'|    {:.3f}\t '.format(kumKedatangan),'|    {:.2f}\t     |'.format(x),'    {:.2f}\t   |'.format(f)) 
print('---------------------------------------------------------------------------------------------------------------------------------------------------')
print('rata-rata {:.3f}\t'.format(rataRataSemua))
print('a => kedatangan pelanggan \t b =>Pencucian rambut \t c=>waktu kedatangan \t => d = kumulatif kedatangan \t => e => waktu proses pemotongan rambut \t f=>  waktu selesai dilayani' )
