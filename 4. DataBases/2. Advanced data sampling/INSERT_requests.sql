--insert

INSERT INTO artist (artist_name)
VALUES ('QUEEN'), ('AC/DC'), ('Linkin Park'), ('Sting');

INSERT INTO genre (genre_name)
VALUES ('Поп-рок'), ('Хард-рок'), ('Поп')

INSERT INTO album (album_name, album_release_year)
VALUES ('Living Things', 2012), ('Back in Black', 1980), ('A Night at the Opera', 1975), ('My Songs', 2019)

INSERT INTO song (song_name, song_duration, album_id)
VALUES ('Castle of Glass', 205, 1), ('Lost in the Echo', 205, 1), ('Back in Black', 253, 2), ('Bohemian Rhapsody', 355, 3), ('Englishman in New York', 268, 4), ('Shape of My Heart', 283, 4)

INSERT INTO album (album_name, album_release_year)
VALUES ('Studio album', 2013), ('Backtracks', 2009), ('Greatest Hits', 1981), ('The Best of 25 Years', 2011)

INSERT INTO artist_album (artist_id, album_id)
VALUES (1, 3), (2, 2), (3, 1), (4, 4)

INSERT INTO genre_artist (genre_id, artist_id)
VALUES (1, 1), (1, 3), (2, 1), (2, 2), (3, 4)

INSERT INTO song_album (song_id, album_id)
VALUES (1, 1), (2, 1), (3, 2), (4, 3), (5, 4), (6, 4) 


