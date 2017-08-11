class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

swear_song = Song(["F",
                    "U",
                    "C",
                    "K",
                    " ",
                    "M",
                    "E"])

Word = ['Fuck', 'You', 'I','Won\'t', 'Do', 'What']
Word2 = ['You','TELL','ME']

Rage_Song = Song(Word)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

swear_song.sing_me_a_song()

Rage_Song.sing_me_a_song()
