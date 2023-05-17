class Vault:
    def __init__(self, galleons =0, sickle =0, knuts =0):
        self.galleons = galleons
        self.sickle = sickle
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} galleons, {self.sickle} sickle, {self.knuts} knuts"
    def __add__(self,other):
      galleons = self.galleons +other.galleons
      sickle = self.sickle + other.sickle
      knuts = self.knuts + other.knuts
      return Vault(galleons, sickle, knuts)


potter = Vault(100, 50, 25)
print(potter)     

weasly = Vault(25, 50, 100)
print(weasly)

total = potter +  weasly
print(total)

