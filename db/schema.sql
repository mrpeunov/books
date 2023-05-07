CREATE TABLE author (
	id serial PRIMARY KEY,
	name VARCHAR (32) NOT NULL,
	born INTEGER,
	died INTEGER
);

CREATE TABLE book (
	id serial PRIMARY KEY,
	title VARCHAR (64) NOT NULL,
	year INTEGER,
	author_id INTEGER,

	FOREIGN KEY (author_id) REFERENCES author(Id)
);


CREATE TABLE tag (
	id serial PRIMARY KEY,
	title VARCHAR ( 50 ) NOT NULL
);


CREATE TABLE tags_to_book(
    id serial PRIMARY KEY,
    book_id INTEGER,
    tag_id INTEGER,

    FOREIGN KEY (book_id) REFERENCES book(id),
    FOREIGN KEY (tag_id) REFERENCES tag(id)
);
