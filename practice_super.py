class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()
        # 다중 상속을 받을 떄, super을 사용하면 맨 처음에 있는 클래스만 상속받음
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()