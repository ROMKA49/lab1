class StringVar:
    name="1"
    def set(self,newName):
        self.name = newName
    def get(self):
        return self.name
str=StringVar()
print(str.get())
str.set("Changed name")
print(str.get())