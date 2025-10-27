import math
import numpy  as np
import matplotlib.pyplot as ppt

print("Opsi : ")
print("1. Forward Kinematic (Dof 2) ")
print("2. Forward Kinematic (DoF 3) ")
print("3. Inverse Kinematic (DoF 2) ")
print("4. FK dengan gambar (DoF 2) ")
opsi=int(input("Masukkan pilihan: "))
if (opsi==1):
    a=int(input("Masukkan sudut rotasi 1: "))
    b=int(input("Masukkan sudut rotasi 2: "))
    t1=math.radians(a)
    t2=math.radians(b)
    l1=int(input("Masukkan lengan 1: "))
    l2=int(input("Masukkan lengan 2: "))
    #dengan rumus yang telah ada
    H04=np.matrix(([math.cos(t1+t2), -math.sin(t1+t2), l1*math.cos(t1)+l2*math.cos(t1+t2)],
               [math.sin(t1+t2), math.cos(t1+t2), l1*math.sin(t1)+l2*math.sin(t1+t2)],
               [0, 0, 1]))
    print(H04)
    #4.secara homogenous transform
    print("\n")
    print("Secara Homogenous Transform")
    H01=np.matrix(([math.cos(t1), -math.sin(t1), 0],
              [math.sin(t1), math.cos(t1), 0],
              [0, 0, 1]))
    H12=np.matrix(([1, 0, l1],
                   [0, 1, 0],
                   [0, 0, 1]))
    H23=np.matrix(([math.cos(t2), -math.sin(t2), 0],
                   [math.sin(t2), math.cos(t2), 0],
                   [0, 0, 1]))
    H34=np.matrix(([1, 0, l2],
                   [0, 1, 0],
                   [0, 0, 1]))
    H104=H01*H12*H23*H34
    print(H104)


#2.Menambah 1 DoF
elif (opsi==2):
    print("\n")
    a=int(input("Masukkan sudut rotasi 1: "))
    b=int(input("Masukkan sudut rotasi 2: "))
    t1=math.radians(a)
    t2=math.radians(b)
    l1=int(input("Masukkan lengan 1: "))
    l2=int(input("Masukkan lengan 2: "))
    c=int(input("Masukkan sudut rotasi 3: "))
    t3=math.radians(c)
    l3=int(input("Masukkan lengan 3: "))

    H01=np.matrix(([math.cos(t1), -math.sin(t1), 0],
                [math.sin(t1), math.cos(t1), 0],
                [0, 0, 1]))
    H12=np.matrix(([1, 0, l1],
                [0, 1, 0],
                [0, 0, 1]))
    H23=np.matrix(([math.cos(t2), -math.sin(t2), 0],
                [math.sin(t2), math.cos(t2), 0],
                [0, 0, 1]))
    H34=np.matrix(([1, 0, l2],
                [0, 1, 0],
                [0, 0, 1]))
    H45=np.matrix(([math.cos(t3), -math.sin(t3), 0],
                [math.sin(t3), math.cos(t3), 0],
                [0, 0, 1]))
    H56=np.matrix(([1, 0, l3],
                [0, 1, 0],
                [0, 0, 1]))
    H06=H01*H12*H23*H34*H45*H56
    print(H06)

#Untuk invers kinematik DoF 2
elif(opsi==3):
    l1=int(input("Masukkan lengan 1: "))
    l2=int(input("Masukkan lengan 2: "))
    xa=int(input("Masukkan X akhir: "))
    ya=int(input("Masukkan y akhir: "))

    t2= math.acos((xa**2 + ya**2 - l1**2 - l2**2) / (2*l1*l2))
    t1= math.atan2(ya,xa) - math.atan2((l2*math.sin(t2)),l1+l2*math.cos(t2))
    print("\n")
    print(f"Sudut rotasi pertama: {t1}")
    print(f"Sudut rotasi kedua:   {t2}")

#bentuk gambar DoF2
elif(opsi==4):

    a=int(input("Masukkan sudut rotasi 1: "))
    b=int(input("Masukkan sudut rotasi 2: "))
    t1=math.radians(a)
    t2=math.radians(b)
    l1=int(input("Masukkan lengan 1: "))
    l2=int(input("Masukkan lengan 2: "))

    def kin(x,y):
        ha= np.matrix(([math.cos(x), -math.sin(x), 0],
                       [math.sin(x), math.cos(x), 0],
                       [0, 0, 1]))
        hb= np.matrix(([1, 0, y],
                       [0, 1, 0],
                       [0, 0, 1]))
        return ha*hb
    
    jumlah= kin(t1,l1)*kin(t2, l2)

    x = [0]
    y = [0]
    Rad = t1+ t2
    for i in range(2):
        x.append( x[-1] + l1 * np.cos(Rad))
        y.append( x[-1] + l1 * np.sin(Rad))

    ppt.figure(figsize=(9,9))
    warna= ppt.cm.jet(np.linspace(0,1,a))

    for i in range(2):
        ppt.plot(
            [x[i],x[i+1]], [y[i], y[i+1]],
            '-o', linewidth=5, color=warna[i],
            label=f'Link {i+1}'
        )

    for i in range(len(x)):
        label= 'Base' if i == 0 else (f'Joint {i}' if i < a else 'End Effector')
        ppt.text(x[i], y[i], label, fontsize=10, ha='right')

    ppt.show()


    
    