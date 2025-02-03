
CREATE TABLE IF NOT EXISTS Genre ( 
	genre_id serial PRIMARY KEY,
	genre_name varchar(40) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Artist (
	artist_id serial PRIMARY KEY,
	artist_name varchar(40) UNIQUE NOT NULL
);

--связной Genre и Artist
CREATE TABLE IF NOT EXISTS Genre_Artist ( 
	genre_id integer REFERENCES Genre(genre_id),
	artist_id integer REFERENCES Artist(artist_id),
	CONSTRAINT relation_Genre_Artist PRIMARY KEY (genre_id, artist_id)
);

CREATE TABLE IF NOT EXISTS Album (
	album_id serial PRIMARY KEY,
	album_name varchar(40) UNIQUE NOT NULL,
	album_release_year integer NOT NULL
	CONSTRAINT album_release_year_check CHECK (album_release_year >= 1900)
);

--'связной Artist и Album'
CREATE TABLE IF NOT EXISTS Artist_Album ( 
	artist_id integer REFERENCES Artist(artist_id),
	album_id integer REFERENCES Album(album_id),
	CONSTRAINT relation_Artist_Album PRIMARY KEY (artist_id, album_id)
);

CREATE TABLE IF NOT EXISTS Song ( --один к многим
	song_id serial PRIMARY KEY,
	song_name varchar(40) NOT NULL,
	song_duration integer NOT NULL,
	album_id integer NOT NULL REFERENCES Album(album_id)
);

CREATE TABLE IF NOT EXISTS album (
	album_id serial PRIMARY KEY,
	album_name varchar(40) UNIQUE NOT NULL,
	album_release_year integer NOT NULL,
	CONSTRAINT album_release_year_check CHECK (album_release_year >= 1900)
);

--связной Song и album
CREATE TABLE IF NOT EXISTS Song_album ( 
	song_id integer REFERENCES Song(song_id),
	album_id integer REFERENCES album(album_id),
	CONSTRAINT relation_Song_album PRIMARY KEY (song_id, album_id)
);
