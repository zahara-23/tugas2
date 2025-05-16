class A:
    def __init__(self):
        self._a = 0

    def setA(self, a):
        self._a = a

    def getA(self):
        return self._a

class B(A):
    def __init__(self):
        super().__init__()  # Memanggil konstruktor kelas induk
        self._b = 0

    def setB(self, b):
        self._b = b

    def getB(self):
        return self._b

# Membuat objek
obj = B()
obj.setA(10)
print("Nilai a: %d" % obj.getA())
obj.setB(20)
print("Nilai b: %d" % obj.getB())
