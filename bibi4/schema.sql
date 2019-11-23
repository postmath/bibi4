DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS ugroup;
DROP TABLE IF EXISTS membership;

CREATE TABLE user (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       email TEXT UNIQUE NOT NULL,
       fullname TEXT UNIQUE NOT NULL,
       password TEXT NOT NULL
);

CREATE TABLE ugroup (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       owner_id INTEGER NOT NULL,
       FOREIGN KEY (owner_id) REFERENCES user (id)
);

CREATE TABLE membership (
       ugroup_id INTEGER NOT NULL,
       user_id INTEGER NOT NULL,
       FOREIGN KEY (ugroup_id) REFERENCES ugroup (id),
       FOREIGN KEY (user_id) REFERENCES user (id)
);
