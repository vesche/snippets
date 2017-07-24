#!/usr/bin/env python

import argparse
import imdbpie
import wikipedia


def mt_movie(movie):
    imdb = imdbpie.Imdb()

    try:
        search = imdb.search_for_title(movie)[0]
    except IndexError:
        return 'Movie not found.'

    movie = imdb.get_title_by_id(search['imdb_id'])
    return '{} ({})\n{}\nIMDB: {}'.format( movie.title, movie.year,
                                           movie.plot_outline, movie.rating )


def mt_actor(actor):
    # imdb = imdbpie.Imdb()

    #try:
    #    search = imdb.search_for_person(actor)[0]
    #except IndexError:
    #    return 'Actor not found.'

    #actor = imdb.get_person_by_id(search['imdb_id'])

    #return '{} {} {}'.format( actor.name, actor.roles, actor.imdb_id )

    search = wikipedia.search('{} filmography'.format(actor))[0]
    return wikipedia.page(search).summary


def mt_director(director):
    return

def mt_suggest(foo):
    return 'Suggestions for {} go here.'.format(foo)


def get_parser():
    parser = argparse.ArgumentParser(description='movietool')
    parser.add_argument('-m', '--movie',
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

    if not (args['movie'] or args['actor'] or args['director']):
        return parser.print_help()

    movie = args['movie']
    if movie and args['suggest']:
        return mt_suggest(movie)
    elif movie:
        return mt_movie(movie)

    actor = args['actor']
    if actor and args['suggest']:
        return mt_suggest(actor)
    elif actor:
        return mt_actor(actor)

    director = args['director']
    if director and args['suggest']:
        return mt_suggest(director)
    elif director:
        return mt_director(director)


if __name__ == '__main__':
    print(main())
