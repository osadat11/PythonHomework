-- SQLite
DROP TABLE tasks;

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    title text[40] NOT NULL,
    due_d text[10],
    due_t text[5],
    priority INTEGER,
    description text[180],
    done INTEGER NOT NULL
);

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