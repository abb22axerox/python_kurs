import artist_database

artists = artist_database.list_artists()

print('----------------------------------------')
for artist in artists:
    print(f'- {artist}')
print('----------------------------------------')

selected_artist = input('Artist name > ')

for artist in artists:
    if selected_artist == artist:
        print(f"""----------------------------------------
               {artist}
----------------------------------------
| Members:      {artist_database.get_artist(artist)['members']}
| Genres:       {artist_database.get_artist(artist)['genres']}
| Years Active: {artist_database.get_artist(artist)['years_active']}
----------------------------------------""")