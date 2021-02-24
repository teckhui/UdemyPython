from nested_data import albums

SONGS_LIST = 3
SONGS_TITLE = 1

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title,artist,year,songs) in enumerate(albums):
        print("{}: {}".format(index+1,title))
    
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice-1][SONGS_LIST]
        #print(songs_list)
    else:
        break
    
    for index, song_name in songs_list:
        print("{}: {}".format(index, song_name))
    song_choice = int(input("Please choose your song:"))   
    if 1 <= song_choice <= len(songs_list):
        print("Playing: {}".format(songs_list[song_choice-1][SONGS_TITLE]))
        print("=" * 40)        
    # else:
    #     break