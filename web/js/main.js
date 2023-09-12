console.log("Llamando a Python...")



eel.ejemplo()(function hola (returndepython) {
    console.log(returndepython)
});  

eel.get_file_name()(function getFileName(filename) {
    document.getElementById('filename').innerHTML = filename;
})

eel.get_title()(function getTitle(title) {
    document.getElementById('title').value = title;
    return title
})

eel.get_artist()(function getArtist(artist) {
    document.getElementById('artist').value = artist;
})

eel.get_album()(function getAlbum(album) {
    document.getElementById('album').value = album;
})

eel.expose(guardar);
function guardar () {
    eel.get_data()((data)=>{console.log(data)})
}

eel.expose(obtenerDatos);
function obtenerDatos () {
    var title = document.getElementById('title').value;
    var artist = document.getElementById('artist').value;
    var album = document.getElementById('album').value;
    var data = [title, artist, album]

    return data;
}

