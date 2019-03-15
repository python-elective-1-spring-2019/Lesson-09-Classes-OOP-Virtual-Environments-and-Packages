from classes import Dog
from classes import Puddle
from color_log import Logger


def main():

    
    log = Logger()
    log.info('Hello')
    
    a = Dog('Claus', 'female')
    print(a.get_gender())

    a.age = 12
    print(a.age)

    b = Dog('Claus', 'female')
    print(a)
    print(b)


    p = Puddle('Jens', 'Female')

    print(p)

    



    
    #print(b.type)




if __name__ == "__main__":
    main()