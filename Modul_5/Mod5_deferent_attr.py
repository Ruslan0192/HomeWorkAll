class Buiding:
    total=0
    def __init__(self):
        Buiding.total += 1

for _ in range(40):
    new_buiding = Buiding()
print(Buiding.total)