from core import MyWebs, TvShows
import pelisenhd


if __name__ == "__main__":


    tvshows = []
    #for testing purpose in prod replace with redis
    tvshows.append(TvShows(type='tvshow', search_data={
        "keywords": ["The Mandalorian"],
        'current_season': 2,
        'last_episode': 1,
    }))
    web_list = MyWebs()
    for web in web_list.get_all_website():
        web.scan(tvshows)
