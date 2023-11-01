

class Sqaure():
    def __init__(self,row,col,value=None) :
        self.row=row
        self.col=col
        self.value=value
        
    def has_value(self):
        return self.value!=None