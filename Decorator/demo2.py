def decor(func):
    def inner(name):
        if name=="sunny":
            print("Hello sunny bad morning")
        else:
            func(name)
    return inner

def wish(name):
    print("Hello",name,"Good morning")
decorfunction=decor(wish)

wish("ASHISH")
wish("AJIT")
wish("sunny")
decorfunction("ASHISH")
decorfunction("sunny")
