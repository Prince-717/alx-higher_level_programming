-- Retrieve all genres of the TV show Dexter from the database.
-- The "tv_shows" table contains only one record where title = Dexter (the id can be different).
-- Display each record as: tv_genres.name
-- Sort the results in ascending order by the genre name.
-- Use only one SELECT statement.
-- The database name will be provided as an argument to the mysql command.

SELECT tv_genres.namei
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name;
