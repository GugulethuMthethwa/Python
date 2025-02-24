def make_album(artist, title, num_songs=None):
    # Create the album dictionary with artist and title
    album = {
        'artist': artist,
        'title': title
    }
    
    # If num_songs is provided, add it to the dictionary
    if num_songs:
        album['num_songs'] = num_songs
    
    return album

# Create three albums
album1 = make_album('The Beatles', 'Abbey Road', 17)  # Including number of songs
album2 = make_album('Pink Floyd', 'The Dark Side of the Moon')  # No number of songs
album3 = make_album('Adele', '21', 11)  # Including number of songs

# Print the album dictionaries
print(album1)
print(album2)
print(album3)


