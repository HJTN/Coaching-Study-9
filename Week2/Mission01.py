class Score:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        return self.__func(*args, **kwargs)

@Score
def printer(mid, final):
    print((mid + final)/2)

printer(50,75)