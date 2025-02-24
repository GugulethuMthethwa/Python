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

# Start the while loop to collect album information
while True:
    print("\nEnter the album details:")
    
    # Get the artist name from the user
    artist = input("Artist name (or type 'quit' to stop): ")
    if artist.lower() == 'quit':
        break  # Exit the loop if the user types 'quit'
    
    # Get the album title from the user
    title = input("Album title: ")
    
    # Ask for the number of songs (optional)
    num_songs_input = input("Number of songs (press Enter to skip): ")
    num_songs = None
    if num_songs_input:
        num_songs = int(num_songs_input)  # Convert the input to an integer if provided
    
    # Call the make_album function with the input data
    album = make_album(artist, title, num_songs)
    
    # Print the album dictionary
    print("\nAlbum created:", album)

print("Program ended.")
