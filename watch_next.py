import spacy

nlp = spacy.load('en_core_web_md')

def sim_movie(user_film, file):
    nlp_user_film = nlp(user_film)
    sim_total = []
    movie_list = []
    with open(file,'r') as movies:
        for movie in movies:
            movie_split = movie.split(':')
            desc = nlp(movie_split[1])
            similarity = nlp(desc).similarity(nlp_user_film)
            sim_total.append(similarity)
            movie_list.append(movie_split[0])
            print(movie_split[0], '-', similarity)
        max_sim = sim_total.index(max(sim_total))
        print(f'The movie that is most similar to the hulk is {movie_list[max_sim]}')

hulk = '''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

sim_movie(hulk, 'movies.txt')
