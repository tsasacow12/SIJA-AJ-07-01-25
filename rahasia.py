from dotenv import load_dotenv
import os 

load_dotenv

nama_depan = os.getnev("VARIABLE_DEPAN")
nama_belakang = os.getnev("VARIABLE_BELAKANG")

print("VARIABLE_DEPAN: ", nama_depan)
print("VARIABLE_BELAKANG: ", nama_belakang)