class Outer:
    def __init__(self):
        print('outer class constructor')

    class Inner:
        def __init__(self):
            print('Inner class construtor')

        def show(self):
            print('in inner class - show method')


o=Outer()
o.Inner().show()

o1=Outer()
i1=o1.Inner()
i1.show()



Outer().Inner().show()
        