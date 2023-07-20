-- Retrieve all TV shows from the "hbtn_0d_tvshows" database.
-- Display each record as: tv_shows.title - tv_show_genres.genre_id
-- Sort the results in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn't have a genre, display NULL
-- Use only one SELECT statement
-- The database name will be provided as an argument to the mysql command

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
