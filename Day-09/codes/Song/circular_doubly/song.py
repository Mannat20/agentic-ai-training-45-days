class songs():
    def __init__(self,name,artists,duration):
        self.name=name
        self.artists=artists
        self.duration=duration
        self.next_song=None
        self.previous_song=None
        print('[Song] [init] Object Constrcuted', self)
    def show_songs(self):
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Name: ',self.name)
        print('artists: ',self.artists)
        print('duration: ',self.duration)
        print('next_song: ',self.next_song)
        print('previous_song: ',self.previous_song)
        print('id: ',self)
        print('~~~~~~~~~~~~~~~~~~~~~~~~')