import requests
import pandas as pd

url = "https://vocadb.net/api/songs"

# Parámetros para filtrar canciones (modifica según lo que necesites)
params = {
    #'query': 'Miku',  # Filtra por nombre de canción o artista
    'sort': 'RatingScore'  # Ordenar por puntaje
    #'fields': 'MainPicture,Tags'  # Campos adicionales
    #'maxResults': 50  # Número de resultados a obtener
}

# Hacer la solicitud a la API
response = requests.get(url, params=params)
data = response.json()

songs = []
for song in data['items']:
    songs.append([song['artistString'], song['name'], song['ratingScore'], song['publishDate']])

df = pd.DataFrame(songs, columns=["Artist", "Song", "Score", "Date"])


file_name = "DBVocaloid.xlsx"
df.to_excel(file_name, index=False)  # index=False evita que se guarde el índice de pandas

print(f"Archivo guardado como {file_name}")