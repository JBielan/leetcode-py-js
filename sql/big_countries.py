query = '''
/* The easiest and the fastest way is to just use SELECT FROM WHERE syntax. Its very intuitive and further explanation isnt needed. */
SELECT name, population, area
FROM World
WHERE area > 3000000 or population > 25000000
'''