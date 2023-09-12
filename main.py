import music_tag
import eel
import os

eel.init('web')


@eel.expose
def ejemplo():
    return "Hola..."

# get track path
@eel.expose
def get_track_path():
    file_path = "music\example.mp3"
    return file_path

# get filename
@eel.expose
def get_file_name():
    file_path = get_track_path()
    full_name = os.path.basename(file_path)
    return full_name

# load track
def load_track():
    file_path = get_track_path()
    # assign track path
    f = music_tag.load_file(file_path)
    return f

# get title
@eel.expose
def get_title():
    f = load_track()
    title = f['title']
    return str(title)

# get artist
@eel.expose
def get_artist():
    f = load_track()
    artist = f['artist']
    return str(artist)

# get album
@eel.expose
def get_album():
    f = load_track()
    album = f['album']
    return str(album)

# save data to file
def save(data):
    f = load_track()
    f['title'] = data[0]
    f['artist'] = data[1]
    f['album'] = data[2]

    f.save()

# get data from javascript
@eel.expose
def get_data():
    data = eel.obtenerDatos()()
    print(data)
    save(data)
    return data

 



def main():
    
    f = load_track()
    # dict access returns a MetadataItem
    title_song = f['title']

    # reading
    print("Antes de modificar:")
    print(f'Titulo: {title_song}')
    print("---------")

    # modifying
    f['title'] = 'Solín'
    title_song = f['title']


    print("Después de modificar:")
    print(f'Titulo: {title_song}')
    print("---------")

    # deleting
    del f['title']
    title_song = f['title']

    print("Después de eliminar:")
    print(f'Titulo: {title_song}')

    # save changes
    f.save()



eel.start('index.html')