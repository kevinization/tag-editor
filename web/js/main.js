console.log("Llamando a Python...")

eel.ejemplo()(function hola (returndepython) {
    console.log(returndepython)
});  

eel.get_file_name()(function getFileName(filename) {
    document.getElementById('filename').innerHTML = filename;
})

eel.get_title()(function getTitle(title) {
    document.getElementById('title').value = title;
})

eel.get_artist()(function getArtist(artist) {
    document.getElementById('artist').value = artist;
})

eel.get_album()(function getAlbum(album) {
    document.getElementById('album').value = album;
})