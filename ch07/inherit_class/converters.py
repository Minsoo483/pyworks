from ch07.myclass.converter import ScaleConverter


class Converters(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor)
        self.offset = offset

    def convert(self, val):
        return self.factor * val + self.offset


con = Converters("C", "F", 1.8, 32)
print("Converting 20C")
print(str(con.convert(20)) + con.units_to)
