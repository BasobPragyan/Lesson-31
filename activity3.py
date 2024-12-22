class India():
    def capital(self):
        print("Delhi")
    def language(self):
        print("No official language so far")
    def type(self):
        print("Developing and Third World country and imporant for world and future superpower")

class Germany():
    def capital(self):
        print("Berlin")
    def language(self):
        print("German")
    def type(self):
        print("Developed and First World country. Great power")


india=India()
deutschland=Germany()
for obj in (india,deutschland):
    obj.capital()
    obj.language()
    obj.type()