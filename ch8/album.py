def make_album(artist_name, album_title):
    """Build a dict containing artist name and album"""
    album = {'artist': artist_name, 'album': album_title}
    return album


album_dict = make_album('lil boosie', 'bad azz vol. 2')
print(album_dict)
album_dict = make_album('ugk', 'super tight')
print(album_dict)
album_dict = make_album('pimp c', 'pimpin ain\'t dead')
print(album_dict)
