-- SQLite
DROP TABLE tasks

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    title text,
    description text,
    date text,
    done INTEGER DEFAULT 0,
    tag text
)

-- INSERT INTO posts VALUES(
--     0,
--     0,
--     'Test Tasks',
--     '2019-09-07',
--     '00-57',
--     'これはテストです',
--     'test-init-tag'
-- );

-- INSERT INTO posts(title,date,time,content,tag) VALUES(
--     'PCKの練習',
--     '2019-09-07',
--     '01-12',
--     '幅優先探索をできるように...',
--     'test-競プロ'
-- );

SELECT * FROM tasks