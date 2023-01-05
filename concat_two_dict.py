class A:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def co_t_dict(self):
        self.a1.update(self.a2)
        print(self.a1)

