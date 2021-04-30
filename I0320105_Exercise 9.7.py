#Exercise 9.7
# mengonversi string ke dalam array.array
import array
B = array.array('b')
B.fromstring("Python")
for karakter in B:
     print("%c " % karakter, end='')