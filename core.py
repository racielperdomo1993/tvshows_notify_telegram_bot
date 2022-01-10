class WebAbstract:

    def __init__(self):
        self.title = ""

    def scan(self):
        pass

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class WebFactory(metaclass=SingletonMeta):
    def __init__(self):
        self._creators = {}

    def register_web(self, key, builder: WebAbstract):
        self._creators[key] = builder

    def get_web(self, key, **kwargs):
        creator = self._creators.get(key)
        if not creator:
            raise ValueError(key)
        return creator

class Animeflv(WebAbstract):

    def __init__(self):
        self.title = "animeflv"

    def scan(self):
        return "SCAN ANIMEFLV"

class MyWebs(metaclass=SingletonMeta):

    def __init__(self):
        self.web_list = []

    def add_website(self, web: WebAbstract):
        self.web_list.append(web)

    def get_all_website(self):
        return self.web_list

class TvShows:

    def __init__(self, type: str, search_data):
        self.type = type
        self.search_data = search_data
