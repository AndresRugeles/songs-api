# Lógica

# Lista predeterminada de canciones.
songs = [
    {"artist": "Superfunk", "title": "Joung MC"},
    {"artist": "Phikey", "title": "Beach party Set | Rufus Du Sol, Lane 8"},
    {"artist": "Andrés Arizmendi", "title": "Nena&Copito | Bogotá -Platzi Conf 2024"}
]

def update_song(index, new_data):
    # Verificar que canción exista
    if index < len(songs):
        # Reemplaza la canción
        songs[index] = new_data
        return True
    return False

def delete_song(index):
    if index < len(songs):
        songs.pop(index)
        return True
    return False


'''
def get_all_songs():
    return songs

def add_song(song):
    songs.append(song)

def update_song(index, song):
    if index < len(songs):
        songs[index] = song
        return True
    return False

def delete_song(index):
    if index < len(songs):
        songs.pop(index)
        return True
    return False
'''