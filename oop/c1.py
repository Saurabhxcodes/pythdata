


from gzip import BadGzipFile


class cat:
    breed = None
    gender = None
    fur_color= None
    age = None
    weight = None
    height = None
    is_tamed = None
    
    def eat(self, food = 'catfood'):
        print(f'cat🏇 is eating  {food}')
    def play(self):
        print('👲 is playing')
    def sleep(self):
        print('cat is sleeping')
billu = cat()
tom = cat()
bagadbilla = cat()

billu.breed = 'persian'
billu.weight=2
billu.age = 2
billu.fur_color='white'
billu.height=1
billu.is_tamed=True
billu.gender = 'M'


tom.breed = 'street cat'
tom.weight=2
tom.age = 2
tom.fur_color='white'
tom.height=1
tom.is_tamed=True
tom.gender = 'M'


bagadbilla.breed = 'Wild cat'
bagadbilla.weight=7
bagadbilla.age = 5
bagadbilla.fur_color='Black'
bagadbilla.height=2
bagadbilla.is_tamed=True
bagadbilla.gender = 'M'

print("BILLU DETAILS")
print('breed = ', billu.breed)
print('gender = ',billu.gender)
billu.eat('mouse')
billu.sleep()
billu.play('football')




