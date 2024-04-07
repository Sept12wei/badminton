# 定义一个球员信息
class Player:
    def __init__(self, name, height, weight, style):
        self.name = name
        self.height = height
        self.weight = weight
        self.style = style

    def __str__(self):
        return f"{self.name}, Height: {self.height} cm, Weight: {self.weight} kg, Style: {self.style}"







