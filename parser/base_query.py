class BaseQuery(object):
    def __init__(self):
        self._timeout = 3

    def artists(self, first_symbol: str) -> {str: str}:
        pass

    def compositions(self, artist: str, find_pages: bool = True) -> {str: str}:
        pass

    def text(self, composition_link: str) -> str:
        pass

    def all_texts(self, compositions_: {str: str}) -> {str: str}:
        for key in compositions_.keys():
            compositions_[key] = self.text(compositions_[key])
        return compositions_
