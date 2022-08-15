# Задание 1
SELECT model,speed,hd FROM pc
WHERE price < 500

# Задание 2
SELECT DISTINCT maker FROM product
WHERE type = 'Printer'

# Задание 3
SELECT model,ram,screen FROM laptop
WHERE price > 1000

# Задание 4
SELECT * FROM printer
WHERE color = 'y'

# Задание 5
SELECT model,speed,hd FROM pc
WHERE (cd = '12x' AND price < 600) OR (cd = '24x' AND price < 600)

# Задание 7
SELECT t1.model, t1.price FROM pc AS t1
INNER JOIN product AS t2 ON t1.model = t2.model
WHERE maker = 'B'
UNION 
SELECT t3.model, t3.price FROM laptop AS t3
INNER JOIN product AS t2 ON t3.model = t2.model
WHERE maker = 'B'
UNION
SELECT t4.model, t4.price FROM printer AS t4
INNER JOIN product AS t2 ON t4.model = t2.model
WHERE maker = 'B'

# Задание 8
SELECT maker FROM product
WHERE type = 'PC'
EXCEPT
SELECT maker FROM product
WHERE type = 'Laptop'

# Задание 9
SELECT DISTINCT Maker FROM product
INNER JOIN PC ON product.model = pc.model
WHERE speed >= 450

# Задание 10
SELECT model, price FROM printer
WHERE price = (SELECT MAX (price) FROM printer)

# Задание 11
SELECT AVG (speed) FROM pc

# Задание 12
SELECT AVG (speed) FROM laptop
WHERE price > 1000


# Задание 13

# Задание 14

# Задание 8

# Задание 8

# Задание 8

# Задание 8

# Задание 8

# Задание 8

# Задание 8



