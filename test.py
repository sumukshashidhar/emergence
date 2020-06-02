from ant import Ant

antx = Ant('harvester')
anty = Ant('caretaker')
for i in range(10):
    antxrole = antx.role
    ret = antx.meet(anty.role)
    print("TESTFILE:antxrole", antxrole)
    print("TESTFILE:return value", )