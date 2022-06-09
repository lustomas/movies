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
  
pulp_fiction = Movies(title='Pulp Fiction', year='1994', genre='crime, drama')

simpsons_1 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='01', season='01')
simpsons_2 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='02', season='01')
simpsons_3 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='03', season='01')
simpsons_4 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='04', season='01')
simpsons_5 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='05', season='01')

library = [pulp_fiction, simpsons_1, simpsons_2, simpsons_3, simpsons_4, simpsons_5]

def get_movies():
    for movie in library:
        movies = []
        if isinstance(movie, Movies) == True:
            movies.append(movie)
    return sorted(movies)

def get_series():
    for serie in library:
        series = []
        if isinstance(serie, Series) == True:
            series.append(serie)
    return sorted(series)


def search(search_fraze):
    for element in library:
        if element.title == search_fraze:
            print(element)

def generate_views():
    item = random.choice(list(library))
    number = random.choice(range(1, 101))
    item.play(number)

def ten_times():
    for i in range(10):
        generate_views()

def top_titles(n):
    print("Top titles:")
    print(sorted(library, key=lambda x:x.views, reverse = True) [:n])

print(pulp_fiction.views)
pulp_fiction.play()
print(pulp_fiction.views)

print(pulp_fiction)
print(simpsons_5)
simpsons_5.play()
print(simpsons_5.views)

print(get_movies())

generate_views()

ten_times()

top_titles(3)

search('Pulp Fiction')
