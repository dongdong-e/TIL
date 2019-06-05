class Person:
    name = '사람의 고유한 속성'
    age = '충생 이후부터 삶을 마감할 때까지의 시간'

    def greeting(self):
        print(f'{self.name}이 인사합니다. 안녕하세요')

    def eating(self):
        print(f'{self.name}은 밥을 먹고 있습니다.')

    def aging(self):
        print(f'{self.name}은 현재 {self.age}살이고, 현재 노화가 진행중입니다.')

kyd = Person()
print(kyd.name)
print(kyd.age)

kyd.name = 'KYD'
kyd.age = 17

print(kyd.name)
print(kyd.age)

kyd.greeting()
kyd.eating()
kyd.aging()