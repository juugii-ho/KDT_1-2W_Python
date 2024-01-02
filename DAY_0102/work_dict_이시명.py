# 12. 1
lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
print(lux)

lux = {'health' : 490, 'health' : 800, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
print(lux['health'])
print(lux)

x = {100: 'hundred', False : 0, 3.5 : [3.5, 3.5]}
print(x)

# x = {[10, 20] : 100}
# x = {{'a':10} : 100}

x = {}
print(x)

y =dict()
print(y)

lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
print(lux1)

lux3 = dict([('health', 490), ('mana',334), ('melee', 550), ('armor', 18.72)])
print(lux3)

#12.2
lux = {'health' : 490, 'health' : 800, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
print(lux['health'])
print(lux['armor'])

lux = {'health' : 490, 'health' : 800, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
lux['health'] = 2037
lux['mana'] = 1184
print(lux)

lux['mana_regen'] = 3.28
print(lux)

lux = {'health' : 490, 'health' : 800, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
print('health' in lux)
print('attack_speed' in lux)

print('attack_speed' not in lux)
print('health' not in lux)

lux = {'health' : 490, 'health' : 800, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
print(len(lux))
print(len({'health' : 490, 'health' : 800, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}))


#12.5

keys = input().split(' ')
values = input().split(' ')
if bool(keys[4]) == True:
    print(f''' {(keys[0])} :{values[0]}, {keys[1]}:{values[1]}, {keys[2]}:{values[2]}, {keys[3]}:{values[3]}, {keys[4]}:{values[4]}''')
else:
    print(f''' {keys[0]} :{values[0]}, {keys[1]}:{values[1]}, {keys[2]}:{values[2]}, {keys[3]}:{values[3]}''')

print(bool(keys[4]))