def make_album(artist_name, album_title):
    """Build a dict containing artist name and album"""
    album = {'artist': artist_name, 'album': album_title}
    return album


while True:
    print("\nPlease enter the name of the artist and album: ")
    print("\nPress 'q' at anytime to quit. ")
    in_artist = input("Artist: ")
    if in_artist == 'q':
        break
    in_album = input("Album: ")
    if in_album == 'q':
        break

album_dict = make_album(in_artist, in_album)
print(album_dict)
