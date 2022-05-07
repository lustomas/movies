import random

class Movies:
    
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        self.views = 0
    
    def play(self, step=1):
        self.views += step

    def __str__(self):
        return f'{self.title} ({self.year})'

class Series(Movies):

    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{self.season}E{self.episode}'
  
Pulp_Fiction = Movies(title='Pulp Fiction', year='1994', genre='crime, drama')

Simpsons_1 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='01', season='01')
Simpsons_2 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='02', season='01')
Simpsons_3 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='03', season='01')
Simpsons_4 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='04', season='01')
Simpsons_5 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='05', season='01')

library = [Pulp_Fiction, Simpsons_1, Simpsons_2, Simpsons_3, Simpsons_4, Simpsons_5]

def get_movies():
    for movie in library:
        movies = []
        if isinstance(movie, Series) == False:
            movies.append(movie)
    return sorted(movies)

def get_series():
    for serie in library:
        series = []
        if isinstance(serie, Series) == True:
            series.append(serie)
    return sorted(series)

def search():
    pass

def generate_views():
    item = random.choice(list(library))
    number = random.choice(range(1, 101))
    print(item)
    return item.play(number), print(item.views)

def ten_times():
    for i in range(10):
        generate_views()

def top_titles(n):
    print("Top titles:")
    return sorted(library, key=lambda x:x.views, reverse = True) [:n]

print(Pulp_Fiction.views)
Pulp_Fiction.play()
print(Pulp_Fiction.views)

print(Pulp_Fiction)
print(Simpsons_5)
Simpsons_5.play()
print(Simpsons_5.views)

print(get_movies())

generate_views()

ten_times()

top_titles(3)
