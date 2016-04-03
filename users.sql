# Users
CREATE TABLE users (username TEXT,
                    password TEXT,
                    email TEXT,
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    instrument TEXT,
                    location_id INT,
                    photo_id INT,
                    user_type INT,
                    FOREIGN KEY(photo_id) REFERENCES photos(id),
                    FOREIGN KEY(location_id) REFERENCES locations(id)); # 0 is Musician, 1 is Audience


###################
INSERT INTO users ("username", "password", "abc@def.com", NULL, "saxophone", NULL, NULL, 0)
