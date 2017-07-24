#!/usr/bin/env python

import argparse
from imdbpie import Imdb


def test(title):
    imdb = Imdb()
    
    try:
        search = imdb.search_for_title(title)[0]
    except IndexError:
        return 'Movie not found.'
    
    #results = imdb.search_for_title(title)[:5]
    #for i in range(len(results)):
    #    movie = results[i]
    #    print('{}. {} ({})'.format(i+1, movie['title'], movie['year']))

    #while True:
    #    prompt = raw_input('> ')
    #    if prompt in ['1','2','3','4','5']:
    #        break
    #    else:
    #        print('Invalid choice.')

    #select = results[int(prompt)-1]
    #movie = imdb.get_title_by_id(select['imdb_id'])


    # checking out all dir(movies)
    #for i in dir(movie):
    #    if i.startswith('_'):
    #        continue
	#x = getattr(movie, i)
    #    print('{} - {}'.format(i, x))

    movie = imdb.get_title_by_id(search['imdb_id'])
    return '{} ({})\n{}\nIMDB: {}'.format(  movie.title, movie.year,
                                            movie.plot_outline, movie.rating )


def test2(actor):
    print(actor)

def get_parser():
    parser = argparse.ArgumentParser(description='movietool')
    parser.add_argument('-t', '--title',
                        help='movie to lookup', type=str)
    parser.add_argument('-a', '--actor',
                        help='actor to lookup', type=str)
    parser.add_argument('-d', '--director',
                        help='director to lookup', type=str)
    parser.add_argument('-s', '--suggest',
                        help='suggestion', type=str)
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    title = args['title']
    if title:
        print(test(title))

    actor = args['actor']
    if actor:
        test2(actor)

if __name__ == '__main__':
    main()

