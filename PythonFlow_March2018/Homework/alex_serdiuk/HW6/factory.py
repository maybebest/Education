"""- Implement Factory pattern for some classes (up to you) (try not to use code from examples :) )"""

class Shoes:
    color = ""

    # This is the factory method
    @staticmethod
    def getShoes(shoesColor):
        if (shoesColor == "red"):
            return RedShoes()
        elif (shoesColor == "blue"):
            return BlueShoes()
        else:
            return None

class RedShoes(Shoes):
    color = "red"

class BlueShoes(Shoes):
    color = "blue"


redShoes = Shoes.getShoes("red")
print("%s(%s)" % (redShoes.color, redShoes.__class__.__name__))

blueShoes = Shoes.getShoes("blue")
print("%s(%s)" % (blueShoes.color, blueShoes.__class__.__name__))