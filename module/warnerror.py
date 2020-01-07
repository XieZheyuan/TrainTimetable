class TrainCodeNoneWarning(Warning):
    def __init__(self,s):
        self.string=s
    def __str__(self):
        return self.string
    def __repr__(self):
        return self.string

class TrainCodeNoneError(Exception):
    def __init__(self,s):
        self.string=s
    def __str__(self):
        return self.string
    def __repr__(self):
        return self.string