class BaseQuery(object):
    def __init__(self):
        self._timeout = 3

    def artists(self, first_symbol: str) -> {str: str}:
        pass

    def compositions(self, artist: str, find_pages: bool = True) -> {str: str}:
        pass

    def text(self, composition_link: str) -> {str: [str]}:
        pass

    def all_texts(self, compositions: {str: str}) -> {str: str}:
        for key in compositions.keys():
            text = self.text(compositions[key])
            if text:
                compositions[key] = text
        return compositions
