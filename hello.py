class user:

    def __init__(self,id,name):
        self.id=id
        self.name=name 

    def __str__(self):
         return f"hello{self.name},welcome to python"

    u1 = user(1,"omkar")
    print(u1)