from struct import *



packed_data = pack('B',125)
f = open('file-01','wb')
check = f.write(packed_data)
print(check)

packed_data = pack('B',21)
check = f.write(packed_data)
print(check) 

packed_data = pack('B',13)
check = f.write(packed_data)
print(check)

packed_data = pack('B',41)
check = f.write(packed_data)
print(check)

packed_data = pack('B',15)
check = f.write(packed_data)
print(check)
f.close()