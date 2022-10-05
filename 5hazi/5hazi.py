class Team:
    def __init__(self, nev, project, szerep):
        self._nev = nev
        self._project = project
        self._szerep = szerep
        
    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, job):
        self._project = job

    def __str__(self):
        return self._nev + " a " + self._project + "-en dolgozik " + self._szerep + " szerepkörben."

    def __eq__(self, masik_tag):
        return self._nev != masik_tag._nev and self._project == masik_tag._project
 
tag1 = Team("Ricsi", "SolArch", "Frontend")
tag2 = Team("Angéla", "ZerTeng", "Tesztelő")
tag3 = Team("Peti", "KefERP", "Backend")
tag4 = Team("Éva", "KefERP", "Frontend")

print("-- Developer létrehozva. --")
print(tag1)

print("-- Developer létrehozva. --")
print(tag2)

print("-- Developer létrehozva. --")
print(tag3)

print("-- Developer létrehozva. --")
print(tag4)

osszehas = (tag3 == tag4)
if osszehas == True:

    print(tag3._nev + " és " + tag4._nev + " dolgoznak egy projekten.")