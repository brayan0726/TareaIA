import json
data = {} #dicionario 
data['Calificaciones'] = [] #lista
data['Calificaciones'].append({
    'periodo': 1,
    'nombre': 'luis',
    'clase':'matematicas' ,
    'seccion': 7,
    'notas': 87})
data['Calificaciones'].append({
    'periodo': 2,
    'nombre': 'ariana',
    'clase':'dibujo' ,
    'seccion': 1,
    'notas': 67})
data['Calificaciones'].append({
    'periodo': 1,
    'nombre': 'nicol',
    'clase':'programacion' ,
    'seccion': 3,
    'notas': 78})
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)