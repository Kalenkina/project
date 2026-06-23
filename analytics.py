import psycopg2

conn = psycopg2.connect(
    database="project2",
    user="postgres",
    password="05251119",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
SELECT
    l.city_name,
    AVG(p.price) AS avg_price
FROM PriceHistory p
JOIN Items i ON p.item_id = i.item_id
JOIN Locations l ON i.location_id = l.location_id
GROUP BY l.city_name;
""")

cur.execute("""
SELECT
    i.title,
    p.price
FROM PriceHistory p
JOIN Items i ON p.item_id = i.item_id
ORDER BY p.price ASC
LIMIT 5;
""")

cur.execute("""
SELECT
    i.title,
    p.price
FROM PriceHistory p
JOIN Items i ON p.item_id = i.item_id
ORDER BY p.price DESC
LIMIT 5;
""")

cur.execute("""
SELECT COUNT(*)
FROM PriceHistory
WHERE record_date >= CURRENT_DATE - INTERVAL '7 days';
""")

cur.execute("""
SELECT
CASE
    WHEN EXTRACT(YEAR FROM CURRENT_DATE) - year < 5
         THEN '0-5 жыл'
    WHEN EXTRACT(YEAR FROM CURRENT_DATE) - year BETWEEN 5 AND 10
         THEN '5-10 жыл'
    ELSE '10 жылдан жоғары'
END AS age_group,
AVG(price) AS avg_price
FROM Items i
JOIN PriceHistory p
ON i.item_id = p.item_id
GROUP BY age_group;
""")

cur.execute("""
SELECT
    i.title,
    l.city_name,
    p.price
FROM PriceHistory p
JOIN Items i ON p.item_id = i.item_id
JOIN Locations l ON i.location_id = l.location_id
WHERE p.price <
(
    SELECT AVG(p2.price) * 0.85
    FROM PriceHistory p2
    JOIN Items i2 ON p2.item_id = i2.item_id
    WHERE i2.location_id = i.location_id
);
""")

print(cur.fetchone())

conn.close()