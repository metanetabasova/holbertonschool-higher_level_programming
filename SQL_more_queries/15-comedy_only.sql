-- Tv soularini elifba sirasi ile siralayir
SELECT  tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_shows_genres.show_id
INNER JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
