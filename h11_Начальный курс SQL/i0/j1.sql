CREATE TABLE band (
	band_id	INTEGER NOT NULL PRIMARY KEY,
	name	VARCHAR,
	year	SMALLINT
	comment	VARCHAR
);

CREATE TABLE album (
	album_id	INTEGER,
	name		VARCHAR,
	band_id		INTEGER REFERENCES band(band_id),
	year		SMALLINT
);