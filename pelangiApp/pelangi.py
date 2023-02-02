#EMMANUEL CHRISTOPHER ASWAN - 212100154
#WIRA YUDHA TANDUNGAN - 202000536

class Color:
    def __init__(self,color_):
        self.name = str(color_)
    
    def get_color_name(self):
        return self.name

class Rainbow():
    def __init__(self):
        self.name = "Normal Rainbow"
        self.colors = []
        
    def append_color(self,color):
        obj_color = Color(color)
        self.colors.append(obj_color)

    def paint_this_rainbow(self):
        colors = ['merah', 'kuning', 'hijau']
        for color in colors:
            self.append_color(color)

    def get_all_color(self):
        colors = []
        for color in self.colors:
            colors.append(color.get_color_name())
        return colors

class CompleteRainbow(Rainbow):
    def __init__(self):
        super().__init__()
        self.name = "Complete Rainbow"

    def paint_this_rainbow(self):
        colors = ['merah', 'jingga', 'kuning', 'hijau', 'biru', 'nila', 'ungu']
        for color in colors:
            self.append_color(color)

class MockRainbow():
    def __init__(self):
        pass


class Sky():
    def __init__(self):
        self.insideSky = []
        self.color = 'biru'

    def append_rainbow(self,rainbow):
        self.insideSky.append(rainbow)

    def get_all_rainbow(self):
        return self.insideSky
    
        
class God:
    def __init__(self):
        self.sky = None

    def create_sky(self):
        self.sky = Sky()
    
    def create_rainbow(self, kind):
        if kind == 'Normal':
            rainbow = Rainbow()
            rainbow.paint_this_rainbow()
            self.sky.append_rainbow(rainbow)
        
        elif kind == 'Complete':
            rainbow = CompleteRainbow()
            rainbow.paint_this_rainbow()
            self.sky.append_rainbow(rainbow)

class Singers:
    def sing_pelangi_pelangi(self,colors):
        print('\n\n-----Mulai Pujian!-----\n')
        print("PELANGI PELANGI")
        print("ALANGKAH INDAHMU")
        for color in colors:
            print(color, end=' ')
        print("\nDI LANGIT YANG BIRU")
        print("PELUKISMU AGUNG, SIAPA GERANGAN?")
        print("PELANGI PELANGI CIPTAAN TUHAN")
        print("\n---------Amin---------\n\n")


class Interface:
    def __init__(self, god_:God):
        self.god = god_
        self.god.create_sky()

    def start(self):
        while True:
            print('-'*50)
            print("Welcome GOD, what is THOU will for The Rainbow?")
            print('-'*50)
            choice = input("\n1. Add  a rainbow to the sky \n2. Human Praised You with 'Pelangi-Pelangi' \n3. Close \n\n\nChoice: \n")
            if choice == '1':
                self.add_rainbow()
            elif choice == '2':
                self.sing_the_rainbow()
            elif choice == '3':
                break
            else:
                print("Input Type Error")
    
    def add_rainbow(self):
        print("\nWhat kind of rainbow ?")
        choice = input("\n1. Normal Rainbow \n2. Complete Rainbow \n\nChoice: \n")
        if choice == "1":
            self.god.create_rainbow('Normal')
            print("\n\n\n-----NORMAL RAINBOW HAS BEEN CREATED!-----\n\n\n")
        elif choice == "2":
            self.god.create_rainbow('Complete')
            print("\n\n\n-----COMPLETE RAINBOW HAS BEEN CREATED!-----\n\n\n")
        else:
            print("Input Type Error")

    def sing_the_rainbow(self):
        rainbows = self.god.sky.get_all_rainbow()
        for rainbow in rainbows:
            colors = rainbow.get_all_color()
            Singers().sing_pelangi_pelangi(colors)
        
