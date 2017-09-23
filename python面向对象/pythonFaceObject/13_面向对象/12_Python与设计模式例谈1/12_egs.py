class Singleton:

    def __new__(cls,*args,**kwargs):

        if not hasattr(cls,'_sgl'):
            cls._sgl = super().__new__(cls,*args,**kwargs)
        return cls._sgl

if __name__ == '__main__':
    sa = Singleton()
    sb = Singleton()
    print(id(sa))
    print(id(sb))