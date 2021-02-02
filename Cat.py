"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""

from lagou.python1.test14.homework.Animal import Animal


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.name="Cat"
        self.hair="短毛"
    def catch_mouse(self):
        print(f"{self.name} 会捉老鼠")
    def will_call(self,action):
        print(f"动物：{self.name} 会{action}")


if __name__ == '__main__':
    animal=Animal()
    animal.will_call()
    animal.will_run()
    cat=Cat()
    cat.will_call("喵喵叫")
    cat.will_run()
    cat.catch_mouse()


