# OOP, this is a vast subject, but I'll try to give a gist of it

class Player:
    def __init__(self):
        self.position = 0
        self.bullets = 10
        pass

    def walk(self):
        print("walk")
        self.position += 1

    def shoot(self):
        self.bullets -= 3
        print("pew pew pew")

    def reload(self):
        self.bullets = 10

    def print_stats(self):
        print("Bullets:", self.bullets)
        print("Position:", self.position)

  
p = Player()
p.walk()
p.walk()
p.shoot()
p.shoot()
p.print_stats()
p.reload()
p.walk()
p.print_stats()