import math
sudut = 35
y = 0
v = 50
deltat = 0.01
x = 0
g = -9.8
t = 0

vx = v * math.cos(math.radians(sudut))
vy = v * math.sin(math.radians(sudut))

while True :
    print(x,y)
    t = t + deltat
    vy = vy + (g*deltat)
    x = x + (vx * deltat)
    y = y + (vy * deltat)
    
    if y < 0 :
        break


# Dibawah dipake untuk melakukan simulasi (menggunakan anaconda -> JupyterLab)
# import math
# import matplotlib.pyplot as plt

# def solusi_numerik(y,v,sudut):
#     deltat = 0.01
#     x = 0
#     g = -9.8
#     t = 0
    
#     x_arr = []
#     y_arr = []

#     vx = v * math.cos(math.radians(sudut))
#     vy = v * math.sin(math.radians(sudut))

#     while True :
#         x_arr.append(x)
#         y_arr.append(y)

#         t = t + deltat
#         vy = vy + (g * deltat)
#         y = y + (vy * deltat)
#         x = x + (vx * deltat)

#         if y < 0 :
#             break
#     return x_arr, y_arr

# x_arr,y_arr = solusi_numerik(0,50,35

# plt.plot(x_arr,y_arr)

# line 54 berfungsi untuk menampilkan simulasi di JupyterLab
