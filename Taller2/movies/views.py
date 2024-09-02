import csv
from django.shortcuts import render
from django.conf import settings
from pathlib import Path

def home(request):
    # Ruta del archivo CSV en el directorio de la aplicación
    csv_file_path = Path(__file__).resolve().parent / 'archivo.csv'
    
    movies = []
    
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                movies.append({
                    "imdbID":row['imdbID'],
                    "title": row['title'],
                    "year": row['year'],
                    "rating":row['rating'],
                    "runtime":row['runtime'],
                    'genre':row['genre'],
                    'released':row['released'],
                    'director':row['director'],
                    'writer':row['writer'],
                    'cast':row['cast'],
                    'metacritic':row['metacritic'],
                    'imdbRating':row['imdbRating'],
                    'imdbVotes':row['imdbVotes'],
                    'poster':row['poster'],
                    'plot':row['plot'],
                    'fullplot':row['fullplot'],
                    'language':row['languge'],
                    'country':row['country'],
                    'awards':row['awards'],
                    'lastupdated':row['lastupdated'],
                    'type':row['type']
                })
    except FileNotFoundError:
        print("El archivo CSV no se encuentra en la ubicación especificada.")
    
    return render(request, 'home.html', {'movies': movies})
