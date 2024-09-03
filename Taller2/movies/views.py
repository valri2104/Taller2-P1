from django.shortcuts import render
import csv
from django.conf import settings
from pathlib import Path
import codecs

def home(request):
    return render(request, 'home.html')

def movies_list(request):
    # Ruta del archivo CSV en el directorio de la aplicación
    csv_file_path = Path(__file__).resolve().parent / 'movies.csv'
    
    movies = []

    try:
        with codecs.open(csv_file_path, 'r', 'utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                movies.append({
                    "imdbID": row.get('imdbID'),
                    "title": row.get('title'),
                    "year": row.get('year'),
                    "rating": row.get('rating'),
                    "runtime": row.get('runtime'),
                    "genre": row.get('genre'),
                    "released": row.get('released'),
                    "director": row.get('director'),
                    "writer": row.get('writer'),
                    "cast": row.get('cast'),
                    "metacritic": row.get('metacritic'),
                    "imdbRating": row.get('imdbRating'),
                    "imdbVotes": row.get('imdbVotes'),
                    "poster": row.get('poster'),
                    "plot": row.get('plot'),
                    "fullplot": row.get('fullplot'),
                    "language": row.get('language'),
                    "country": row.get('country'),
                    "awards": row.get('awards'),
                    "lastupdated": row.get('lastupdated'),
                    "type": row.get('type')
                })
    except FileNotFoundError:
        print("El archivo CSV no se encuentra en la ubicación especificada.")
    
    return render(request, 'movies_list.html', {'movies': movies})
