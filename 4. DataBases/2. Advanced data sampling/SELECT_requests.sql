--select задание 2
--Название и продолжительность самого длительного трека.
SELECT song_name, song_duration FROM song s
ORDER BY song_duration DESC
LIMIT 1;

--Название треков, продолжительность которых не менее 3,5 минут.
SELECT song_name, song_duration FROM song s
WHERE song_duration >= 210
ORDER BY song_duration desc

--Названия сборников, вышедших в период с 2018 по 2020 год включительно.
SELECT album_name FROM album c 
WHERE c.album_release_year >= 2018 AND c.album_release_year <=2020

--Исполнители, чьё имя состоит из одного слова.
SELECT artist_name FROM artist
WHERE artist_name NOT LIKE '% %'

--Название треков, которые содержат слово «мой» или «my».
SELECT song_name FROM song
WHERE lower(song_name) LIKE '%my%'


--select задание 3
--Количество исполнителей в каждом жанре.
SELECT g.genre_name, count(a.artist_name) count FROM genre g 
LEFT JOIN genre_artist ga ON g.genre_id = ga.genre_id
LEFT JOIN artist a ON ga.artist_id = a.artist_id 
GROUP BY g.genre_name 
ORDER BY count desc

--Количество треков, вошедших в альбомы 2019–2020 годов.
SELECT count(so.song_name) count FROM song so
LEFT JOIN album al ON so.album_id = al.album_id 
WHERE al.album_release_year >= 2019 AND al.album_release_year <= 2020


--Средняя продолжительность треков по каждому альбому.
SELECT al.album_name, sum(so.song_duration)/count(so.song_duration) middle_duration FROM album al
LEFT JOIN song so ON al.album_id = so.album_id 
GROUP BY al.album_name 

--Все исполнители, которые не выпустили альбомы в 2020 году.
SELECT ar.artist_name FROM artist ar
LEFT JOIN artist_album al ON ar.artist_id = al.artist_id 
left JOIN album alb ON al.album_id = alb.album_id
WHERE alb.album_release_year != 2020

--Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).
SELECT co.collection_name FROM collection co
LEFT JOIN song_collection sc ON co.collection_id = sc.collection_id 
LEFT JOIN song s ON sc.song_id = s.song_id 
LEFT JOIN album alb ON s.album_id =alb.album_id 
LEFT JOIN artist_album al ON alb.album_id = al.album_id 
LEFT JOIN artist a ON al.artist_id = a.artist_id 
WHERE a.artist_name = 'Sting'
GROUP BY co.collection_name

