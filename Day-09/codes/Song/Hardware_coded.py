class songs():
    def __init__(self,name,artists,duration):
        self.name=name
        self.artists=artists
        self.duration=duration
        self.next_song=None
        self.previous_song=None
    def show_songs(self):
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Name: ',self.name)
        print('artists: ',self.artists)
        print('duration: ',self.duration)
        print('next_song: ',self.next_song)
        print('previous_song: ',self.previous_song)
        print('id: ',self)
        print('~~~~~~~~~~~~~~~~~~~~~~~~')

song1=songs('1.Me vs Me','Arjan Dhillon,Mrxci',3)
song2=songs('2.Low fade','karan aujhla',4)
song3=songs('3.Definition','dulla',3.5)
song4=songs('4.Unbothered','Navaan Sandhu',3.5)
song5=songs('5.Culture','Arjan Dhillon,Mrxci',3)

song1.next_song=song2
song2.next_song=song3
song3.next_song=song4
song4.next_song=song5
song5.next_song=song1

song1.previous_song=song5
song2.previous_song=song1
song3.previous_song=song2
song4.previous_song=song3
song5.previous_song=song4



song1.show_songs()
song2.show_songs()
song3.show_songs()
song4.show_songs()
song5.show_songs()