GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
del GeekTech['bag']

GeekTech['address'] = 'Ibraimova 103'

GeekTech['phone_number'] = '+996507052018'
GeekTech['instagram'] = '@geektech__kg'

GeekTech2 = {
    'courses': ['Android', 'Backend', 'Frontend', 'iOS', 'UX/UI designer', 'English'],
    'phone_number': '+996507052018',
    'instagram': '@geektech_kg'
}
GeekTech.update(GeekTech2)
GeekTech["courses"] = tuple(GeekTech["courses"])
for key, value in GeekTech.items():
    print(f'{key}: {value}')