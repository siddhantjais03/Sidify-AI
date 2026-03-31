CREATE DATABASE emotion_music;

USE emotion_music;

CREATE TABLE history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    emotion VARCHAR(50),
    song_name VARCHAR(255),
    artist VARCHAR(255),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
-- -------------------------------
-- 1. CREATE DATABASE
-- -------------------------------
CREATE DATABASE IF NOT EXISTS emotion_music;

USE emotion_music;

-- -------------------------------
-- 2. CREATE TABLE
-- -------------------------------
CREATE TABLE IF NOT EXISTS history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    emotion VARCHAR(50),
    song_name VARCHAR(255),
    artist VARCHAR(255),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- -------------------------------
-- 3. INSERT TEST DATA
-- -------------------------------
INSERT INTO history (emotion, song_name, artist) VALUES
('happy', 'Shape of You', 'Ed Sheeran'),
('happy', 'Kala Chashma', 'Badshah'),
('sad', 'Channa Mereya', 'Arijit Singh'),
('sad', 'Let Me Down Slowly', 'Alec Benjamin'),
('angry', 'Believer', 'Imagine Dragons'),
('angry', 'Zinda', 'Siddharth Mahadevan'),
('neutral', 'Closer', 'The Chainsmokers'),
('neutral', 'Perfect', 'Ed Sheeran'),
('happy', 'Senorita', 'Shawn Mendes'),
('sad', 'Tum Hi Ho', 'Arijit Singh');

-- -------------------------------
-- 4. CHECK DATA
-- -------------------------------
SELECT * FROM history;

-- -------------------------------
-- 5. DAILY ANALYSIS
-- -------------------------------
SELECT emotion, COUNT(*) AS count
FROM history
WHERE DATE(timestamp) = CURDATE()
GROUP BY emotion;

-- -------------------------------
-- 6. WEEKLY ANALYSIS
-- -------------------------------
SELECT emotion, COUNT(*) AS count
FROM history
WHERE YEARWEEK(timestamp) = YEARWEEK(NOW())
GROUP BY emotion;

-- -------------------------------
-- 7. MONTHLY ANALYSIS
-- -------------------------------
SELECT emotion, COUNT(*) AS count
FROM history
WHERE MONTH(timestamp) = MONTH(NOW())
GROUP BY emotion;

-- -------------------------------
-- 8. YEARLY ANALYSIS
-- -------------------------------
SELECT emotion, COUNT(*) AS count
FROM history
WHERE YEAR(timestamp) = YEAR(NOW())
GROUP BY emotion;
SELECT * FROM history;
INSERT INTO history (emotion, song_name, artist) VALUES
('happy', 'Shape of You', 'Ed Sheeran'),
('sad', 'Channa Mereya', 'Arijit Singh'),
('angry', 'Believer', 'Imagine Dragons'),
('neutral', 'Closer', 'Chainsmokers');
SELECT * FROM history;
SELECT emotion, COUNT(*) AS count
FROM history
WHERE DATE(timestamp) = CURDATE()
GROUP BY emotion;
SELECT emotion, COUNT(*) AS count
FROM history
WHERE YEARWEEK(timestamp, 1) = YEARWEEK(CURDATE(), 1)
GROUP BY emotion;
SELECT emotion, COUNT(*) AS count
FROM history
WHERE YEAR(timestamp) = YEAR(CURDATE())
AND MONTH(timestamp) = MONTH(CURDATE())
GROUP BY emotion;
INSERT INTO history (emotion, song_name, artist)
VALUES ('happy', 'Auto Song', 'System');
ALTER TABLE history 
MODIFY timestamp DATETIME DEFAULT CURRENT_TIMESTAMP;
SELECT * FROM history ORDER BY timestamp DESC;
USE emotion_music;
SELECT * FROM history;
INSERT INTO history (emotion, song_name, artist)
VALUES ('happy', 'Test Song', 'Test Artist');
SELECT * FROM history ORDER BY timestamp DESC;
SELECT * FROM history ORDER BY timestamp DESC;
WHERE DATE(timestamp) 
SELECT emotion, COUNT(*) AS count
FROM history
WHERE DATE(timestamp) = CURDATE()
GROUP BY emotion;
SELECT emotion, COUNT(*) AS count
FROM history
WHERE YEARWEEK(timestamp, 1) = YEARWEEK(CURDATE(), 1)
GROUP BY emotion;
SELECT emotion, COUNT(*) AS count
FROM history
WHERE YEAR(timestamp) = YEAR(CURDATE())
AND MONTH(timestamp) = MONTH(CURDATE())
GROUP BY emotion;
SELECT emotion, COUNT(*) AS count
FROM history
WHERE YEAR(timestamp) = YEAR(CURDATE())
GROUP BY emotion;
SELECT * FROM history;
INSERT INTO history (emotion, song_name, artist, timestamp)
VALUES ('happy', 'Test1', 'System', NOW() - INTERVAL 1 DAY);

INSERT INTO history (emotion, song_name, artist, timestamp)
VALUES ('sad', 'Test2', 'System', NOW() - INTERVAL 7 DAY);

INSERT INTO history (emotion, song_name, artist, timestamp)
VALUES ('angry', 'Test3', 'System', NOW() - INTERVAL 1 MONTH);

INSERT INTO history (emotion, song_name, artist, timestamp)
VALUES ('neutral', 'Test4', 'System', NOW() - INTERVAL 1 YEAR);
DELETE FROM history;
INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('happy', 'Song1', 'A', NOW()),
('sad', 'Song2', 'B', NOW()),
('angry', 'Song3', 'C', NOW()),
('neutral', 'Song4', 'D', NOW());
INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('happy', 'Song5', 'A', NOW() - INTERVAL 2 DAY),
('sad', 'Song6', 'B', NOW() - INTERVAL 3 DAY);
INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('angry', 'Song7', 'C', NOW() - INTERVAL 10 DAY),
('neutral', 'Song8', 'D', NOW() - INTERVAL 15 DAY);
INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('happy', 'Song9', 'A', NOW() - INTERVAL 3 MONTH),
('sad', 'Song10', 'B', NOW() - INTERVAL 5 MONTH);
SELECT * FROM history;
DELETE FROM history;

INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('happy', 'Song1', 'A', NOW()),
('sad', 'Song2', 'B', NOW()),
('angry', 'Song3', 'C', NOW()),
('neutral', 'Song4', 'D', NOW());

INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('happy', 'Song5', 'A', NOW() - INTERVAL 2 DAY),
('sad', 'Song6', 'B', NOW() - INTERVAL 3 DAY);

INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('angry', 'Song7', 'C', NOW() - INTERVAL 10 DAY),
('neutral', 'Song8', 'D', NOW() - INTERVAL 15 DAY);

INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('happy', 'Song9', 'A', NOW() - INTERVAL 3 MONTH),
('sad', 'Song10', 'B', NOW() - INTERVAL 5 MONTH);
USE emotion_music;
DELETE FROM history;

INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('happy', 'Song1', 'A', NOW()),
('sad', 'Song2', 'B', NOW()),
('angry', 'Song3', 'C', NOW()),
('neutral', 'Song4', 'D', NOW());

INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('happy', 'Song5', 'A', NOW() - INTERVAL 2 DAY),
('sad', 'Song6', 'B', NOW() - INTERVAL 3 DAY);

INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('angry', 'Song7', 'C', NOW() - INTERVAL 10 DAY),
('neutral', 'Song8', 'D', NOW() - INTERVAL 15 DAY);

INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('happy', 'Song9', 'A', NOW() - INTERVAL 3 MONTH),
('sad', 'Song10', 'B', NOW() - INTERVAL 5 MONTH);
SELECT * FROM history;
DELETE FROM history;
INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('happy', 'Song1', 'A', NOW()),
('sad', 'Song2', 'B', NOW()),
('angry', 'Song3', 'C', NOW()),
('neutral', 'Song4', 'D', NOW()),

('happy', 'Song5', 'A', NOW() - INTERVAL 2 DAY),
('sad', 'Song6', 'B', NOW() - INTERVAL 3 DAY),

('angry', 'Song7', 'C', NOW() - INTERVAL 10 DAY),
('neutral', 'Song8', 'D', NOW() - INTERVAL 15 DAY),

('happy', 'Song9', 'A', NOW() - INTERVAL 3 MONTH),
('sad', 'Song10', 'B', NOW() - INTERVAL 5 MONTH);
SELECT emotion, timestamp FROM history;
USE emotion_music;
DELETE FROM history;

INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('happy', 'Song1', 'A', NOW()),
('sad', 'Song2', 'B', NOW()),
('angry', 'Song3', 'C', NOW()),
('neutral', 'Song4', 'D', NOW()),

('happy', 'Song5', 'A', NOW() - INTERVAL 2 DAY),
('sad', 'Song6', 'B', NOW() - INTERVAL 3 DAY),

('angry', 'Song7', 'C', NOW() - INTERVAL 10 DAY),
('neutral', 'Song8', 'D', NOW() - INTERVAL 15 DAY),

('happy', 'Song9', 'A', NOW() - INTERVAL 3 MONTH),
('sad', 'Song10', 'B', NOW() - INTERVAL 5 MONTH);
SELECT emotion, timestamp FROM history;
USE emotion_music;
SELECT DATABASE();
SHOW TABLES;
CREATE TABLE history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    emotion VARCHAR(50),
    song_name VARCHAR(100),
    artist VARCHAR(100),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO history (emotion, song_name, artist, timestamp) VALUES
('happy', 'Song1', 'A', NOW()),
('sad', 'Song2', 'B', NOW()),
('angry', 'Song3', 'C', NOW()),
('neutral', 'Song4', 'D', NOW()),
('happy', 'Song5', 'A', NOW() - INTERVAL 2 DAY),
('sad', 'Song6', 'B', NOW() - INTERVAL 3 DAY),
('angry', 'Song7', 'C', NOW() - INTERVAL 10 DAY),
('neutral', 'Song8', 'D', NOW() - INTERVAL 15 DAY),
('happy', 'Song9', 'A', NOW() - INTERVAL 3 MONTH),
('sad', 'Song10', 'B', NOW() - INTERVAL 5 MONTH);
SELECT * FROM history;

