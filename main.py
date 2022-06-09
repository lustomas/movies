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

    __repr__ = __str__

class Series(Movies):

    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{self.season}E{self.episode}'

    __repr__ = __str__
  
pulp_fiction = Movies(title='Pulp Fiction', year='1994', genre='crime, drama')

simpsons_1 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='01', season='01')
simpsons_2 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='02', season='01')
simpsons_3 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='03', season='01')
simpsons_4 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='04', season='01')
simpsons_5 = Series(title='The Simpsons', year='1989', genre='animation, comedy', episode='05', season='01')

library = [pulp_fiction, simpsons_1, simpsons_2, simpsons_3, simpsons_4, simpsons_5]

def get_movies():
    movies = []
    print("Movies:")
    for movie in library:
        if isinstance(movie, Series) == False:
            movies.append(movie)
    return movies

def get_series():
    series = []
    print("Series:")
    for serie in library:
        if isinstance(serie, Series) == True:
            series.append(serie)
    return series


def search(search_fraze):
    for element in library:
        if element.title == search_fraze:
            return element

def generate_views():
    item = random.choice(list(library))
    number = random.choice(range(1, 101))
    item.play(number)

def ten_times():
    for i in range(10):
        generate_views()

def top_titles(n):
    print("Top titles:")
    return sorted(library, key=lambda x:x.views, reverse = True) [:n]

print(pulp_fiction)
print(pulp_fiction.views)
pulp_fiction.play()
print(pulp_fiction.views)


print(simpsons_5)
print(simpsons_5.views)
simpsons_5.play()
print(simpsons_5.views)

generate_views()
ten_times()

for i in library:
    print(i)
    print(i.views)

print(search('Pulp Fiction'))

movies = movies = get_movies()
for movie in movies:
    print(movie)

series = series = get_series()
for serie in series:
    print(serie)

print(top_titles(3))

