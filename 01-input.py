name = input('Please input city name: ')
distance_km = input('Please input distance in KM: ')
mile = int(distance_km) * 1.609

msg = f'Hello! {name.capitalize()}, The distance you covered in KM is {distance_km} and in miles it is {mile}'

print(msg)
