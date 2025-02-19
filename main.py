#comment zuhal
import time

Start_time = time.time()
print ("Zuhal")
""" ini 
adalah komentar multi baris """

a = 10
b = 2
print ("hasil penjumlahan a dan b adalah", a+b)
print ("zuhal coba push")
print ("namanya juga coba")
print ("coba lagi boleh")
print ("zuhal")

print(time.time() - Start_time, "detik")
#kalo mau compile
#python -m py_compile main.py                    


# Data Type int,float,complex,bool,str
data_int = 9
print("data :", data_int, ", type :", type(data_int))

data_float = float(data_int)
print("data :", data_float, ", type :", type(data_float))

data_str = str(data_int)
print("data :", data_str, ", type :", type(data_str))   

data_bool = bool(data_int) 
print("data :", data_bool, ", type :", type(data_bool))
