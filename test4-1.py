#drugi commit w dev

print("inny komunikat")
print("nowy komunikat")

class Punkt():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # metody np __repr__
    def __repr__(self):
        return "pkt: {pkt.x}, {pkt.y}" .format(pkt=self)

    def __str__(self):
        # return 'Punkt o wsp x=%s, y=%s' %(self.x, self.y)
        return 'Punkt o wsp x={0}, y={1}' .format(self.x, self.y)

    def __len__(self):
        return 2

    def odl_od_centrum(self):
        odl = (self.x**2 + self.y**2)**0.5
        return odl

    def odl_od_punktu(self, other):
        odl = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return odl

pkt1 = Punkt(0,0)
print(pkt1)
print(pkt1.__len__())

