class EmojiMixin:
    EMOJIS = {'grass': '🌳', 'fire': '🔥', 'water': '🌊', 'electric': '🌩️'}

    def emojify(self, poketype: str):
        return EmojiMixin.EMOJIS[poketype]


class Pokemon(EmojiMixin):

    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __repr__(self):
        return f'{self.name}/{EmojiMixin.emojify(self, self.poketype)}'


def main():
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur)


if __name__ == '__main__':
    main()
