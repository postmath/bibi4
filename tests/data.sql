INSERT INTO user (id, username, email, password)
VALUES
  -- password: test
  (1, 'test', 'test@foo.bar', 'pbkdf2:sha256:150000$E5C6Back$99a97c047748587bb21130a9c94d5c9199d6a18db9da1e23724fb400f4db22be'),
  -- password: xyz
  (2, 'xyz', 'abc@xyz.net', 'pbkdf2:sha256:150000$8jBkOKEa$6e8b40190a01c585d7a5f545980e25cf193a51fdc5842008b14a7203d7f892cf'),
  -- password: 123
  (5, 'abc', 'abc@gmail.com', 'pbkdf2:sha256:150000$7VIhxSxX$ecf09a25b6bda05c5b73c8da53323713aaee68f58fc3a935ced51da68238963d');

INSERT INTO ugroup (id, owner_id)
VALUES
  (1, 1),
  (2, 1),
  (3, 5);

INSERT INTO membership (ugroup_id, user_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 1),
  (2, 2),
  (2, 5),
  (3, 2),
  (3, 5);
