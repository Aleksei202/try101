class Songs:
    def __init__(self, lyric=('And', 'a', 'day', 'lasts', 'longer', 'than', 'a', 'century')):
        self.lyric = lyric

    def sing_me_a_song(self):
        for word in self.lyric:
            print(word)


sing = Songs()
sing.sing_me_a_song()
