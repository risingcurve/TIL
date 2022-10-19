CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

SELECT column1, column2 FROM table_name;

SELECT first_name, age FROM users;

SELECT * FROM users;

SELECT rowid, first_name FROM users;

SELECT first_name, age FROM users ORDER BY age ASC;

SELECT first_name, age FROM users ORDER BY age;

SELECT first_name, age FROM users ORDER BY age DESC;

SELECT first_name, age, balance FROM users ORDER BY age ASC, balance DESC;

SELECT country FROM users;

SELECT DISTINCT country FROM users;

SELECT DISTINCT country FROM users ORDER BY country;

SELECT DISTINCT first_name, country FROM users;

SELECT DISTINCT first_name, country FROM users ORDER BY country ASC;

SELECT first_name, age, balance FROM users WHERE age >= 30;

SELECT first_name, age, balance FROM users WHERE age >= 30 AND balance > 500000;

SELECT first_name, last_name FROM users WHERE first_name LIKE '%호%';

SELECT first_name, last_name FROM users WHERE first_name LIKE '%준';

SELECT first_name, last_name, phone FROM users WHERE phone LIKE '02-%';

SELECT first_name, last_name, age FROM users WHERE age LIKE '2_';

SELECT first_name, last_name, phone FROM users WHERE phone LIKE '%-51__-%';

SELECT first_name, country FROM users WHERE country in ('경기도', '강원도');

SELECT first_name, country FROM users WHERE country = '경기도' or country = '강원도';

SELECT first_name, country FROM users WHERE country NOT IN ('경기도', '강원도');

SELECT first_name, age FROM users WHERE age BETWEEN 20 AND 30;

SELECT first_name, age FROM users WHERE age >= 20 and age <= 30;

SELECT first_name, age FROM users WHERE age NOT BETWEEN 20 and 30;

SELECT first_name, age FROM users WHERE age < 20 OR age > 30;

SELECT rowid, first_name FROM users LIMIT 10;

SELECT first_name, balance FROM users ORDER BY balance DESC LIMIT 10;

SELECT first_name, age FROM users ORDER BY age LIMIT 5;

SELECT rowid, first_name FROM users LIMIT 10 OFFSET 10;

SELECT count(*) FROM users;

SELECT avg(age) FROM users WHERE age >= 30;

SELECT country, count(*) FROM users GROUP BY country;




create table classmates (
    name text not null,
    age integer not null,
    address text not null
);

DROP TABLE classmate;

INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES
    ('김철수', 30, '경기'),
    ('이영미', 31, '강원');

UPDATE classmates
SET name='김철수한무두루미',
    address='제주도'
WHERE rowid = 2;
