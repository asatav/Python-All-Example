def decor(func):
    def inner(name):
        if name=="sunny":
            print("Hello sunny bad morning")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("Hello",name,"Good morning")
wish("ASHISH")
wish("AJIT")
wish("sunny")