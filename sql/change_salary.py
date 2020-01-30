query = '''
/* Use UPDATE table_name SET column = sth + CASE WHEN a THEN b WHEN c THEN d  etc */
UPDATE salary SET sex = 
	CASE sex
	WHEN 'm' THEN 'f'
	WHEN 'f' THEN 'm'
END
'''