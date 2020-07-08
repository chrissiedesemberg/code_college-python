def make_album(name, title, number_songs=None):
    if number_songs:
        album = f"\nArtist name: {name.title()}, Album title: {title.title()}, Number of songs: {number_songs}"
    else:
        album = f"\nArtist name: {name.title()}, Album title: {title.title()}"
    return album

album_1 = make_album("Avenged Sevenfold", "Nightmare", number_songs=12)
album_2 = make_album("Avenged Sevenfold", "Nightmare")
album_3 = make_album("Avenged Sevenfold", "Nightmare")

print(album_1)
print(album_2)
print(album_3)
