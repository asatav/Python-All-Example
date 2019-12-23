class Animal:
    IEgs=4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} IEgs...'.format(name, cls.IEgs))
Animal.walk('DOG')
Animal.walk('CAT')