class lists():
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        print('[CircularDoublyLinkedList] [init] Object Constrcuted', self)
    
    def add(self,song):
        self.size +=1
        if self.head==None:
            self.head=song
            self.tail=song
        else:
            self.tail.next_song=song
            self.head.previous_song=song
            song.previous_song=self.tail
            song.next_song=self.head
            self.tail=song

    def show(self, traverse=True):
        if traverse == True:
            song = self.head
            while True:
                song.show_song()
                song = song.next_song

                if song == self.head:
                    break
        
        else:

            song = self.tail

            while True:
                song.show_song()
                song = song.previous_song

                if song == self.tail:
                    break

        
