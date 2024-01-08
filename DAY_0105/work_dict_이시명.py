x= {'a':10, 'b':20, 'c':30, 'd':40}
x.setdefault(('e'))
print(x)

print(x.setdefault('f',100))
print(x)

x= {'a':10, 'b':20, 'c':30, 'd':40}
x.update(e=50)
print(x)
x.update(a=900, f=60)
print(x)

y = {1:'one', 2:'two'}
y.update({1:'ONE', 3:"THREE"})
print(y)

y.update([[2, 'TWO'], [4,'FOUR']])
print(y)

y.update(zip([1,2], ['one', 'two']))
print(y)


x= {'a':10, 'b':20, 'c':30, 'd':40}
print(x.setdefault('a',90))             # setdefault는 기존값 변환되지 않음
print(x)                                # setdefault는 기존값 변환되지 않음

x= {'a':10, 'b':20, 'c':30, 'd':40}
print(x.pop('a'))
print(x)

print(x.pop('z',0))     # 해당 값이 없을 때는 지정한 값 반환

x= {'a':10, 'b':20, 'c':30, 'd':40}
del x['a']
print(x)

x= {'a':10, 'b':20, 'c':30, 'd':40}
print(x.popitem())      # 가장 마지막에 추가된 값 삭제, 3.5 이하는 값 달라짐
print(x)

x= {'a':10, 'b':20, 'c':30, 'd':40}
print(x.get('a'))
print(x.get('z',0))     # 해당 값이 없을 때는 지정한 값 반환

x= {'a':10, 'b':20, 'c':30, 'd':40}
print(x.items())
print(x.keys())
print(x.values())

keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys((keys))
print(x)

keys = ['a', 'b', 'c', 'd']
print(set(keys))
print(list(keys))
print(tuple(keys))

x ={'a':10, 'b':20, 'c':30, 'd':40}
for i in x:
    print(i, end=' ')

x ={'a':10, 'b':20, 'c':30, 'd':40}
for key, value in x.items():
    print(key, value)

x ={'a':10, 'b':20, 'c':30, 'd':40}
for key in x.keys():
    print(key, end=' ')

x ={'a':10, 'b':20, 'c':30, 'd':40}
for value in x.values():
    print(value, end=' ')

keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)

print({key : 0 for key in dict.fromkeys(['a','b','c','d']).keys()})
print({value : 0 for value in {'a':10,'b':20,'c':30,'d':40}.values()})

x ={'a':10, 'b':20, 'c':30, 'd':40}

# for key, value in x.items():
#     if value == 20:
#         del x[key]
#
# print(x)
x= {key:value for key, value in x.items() if value != 20}
print(x)   # 이해가 잘 안되긴 하지만.. if 조건문일 때는 딕셔너리를 새로 생성하므로 가능해짐

terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}

print(terrestrial_planet['Venus']['mean_radius'])
print('{:0^10}'.format(terrestrial_planet['Mars']['orbital_period']))
# print(a[])

x = {'a':0, 'b':0, 'c':0, 'd':0}
y = x
print(x is y)

y['a']=99
print(x)

x = {'a':0, 'b':0, 'c':0, 'd':0}
y = x.copy()
print(x is y)
print(x == y)

x = {'a':{'python':'2.7'}, 'b':{'python':'3.6'}}
y = x.copy()

y['a']['python'] = '2.7.15'
print(x)

x = {'a':{'python':'2.7'}, 'b':{'python':'3.6'}}
import copy
y = copy.deepcopy(x)
y['a']['python'] = '2.7.15'
print(x)
print(y)

x = {'key':'value', 'Python':'language'}
x.clear()
print(x)

keys = ['alpha', 'bravo', 'charlie', 'delta']
values = [10, 20, 30, 40]

x = dict(zip(keys, values))

x = {keys:values for keys, values in x.items() if (keys != 'delta' and values != 30)}
# x = {keys:values for keys, values in x.items() if keys != 'delta'}
# x = {keys:values for keys, values in x.items() if values != 30}

print(x)