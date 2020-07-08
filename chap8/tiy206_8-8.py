def make_album():
    art_alb = {}
    while True:
        print("Please list your favorite artist details here. (Insert 'q' to exit at any stage)")
        artist_name = input("What is the artist name?")
        if artist_name == 'q':
            break
        else:
            art_alb['name'] = artist_name

        album_name = input("What is the album name?")
        if album_name == 'q':
            break
        else:
            art_alb['album'] = album_name

        artists_albums.append(art_alb)


artists_albums = []


make_album()


print(artists_albums)



