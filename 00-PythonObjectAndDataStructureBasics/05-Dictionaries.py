my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)
print(my_dict['key1'])

prices_lookup = {'apple':2.99, 'orange':1.99, 'milk':5.80}
print(prices_lookup['apple'])

d = {'k1':123, 'k2':[6,7,8], "k3":{'insideKey':100}}
print(d)
print(d['k2'])
print(d['k3']['insideKey'])
print(d['k2'][2])

d = {'key1':['a', 'b', 'c']}
print(d['key1'][1].upper())

d = {'k1':100,'k2':200}
d['k3'] = 300
print(d)

d['k1'] = 'New Value'
print(d)

d = {'k1':100,'k2':200, 'k3':300}
print(d.keys())
print(d.values())
print(d.items())