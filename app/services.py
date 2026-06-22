# Lógica

songs = []  # Es una lista, y cada item de la lista es un diccionario que representa una canción y su artista

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