SELECT 
CONCAT(name, '(', LEFT(occupation, 1), ')') as name 
FROM occupations
ORDER BY name, occupation ASC;

SELECT 
CONCAT('There are a total of ', COUNT(occupation), ' ', LOWER(occupation), 's.') as total
FROM occupations
GROUP BY occupation
ORDER BY COUNT(occupation), occupation ASC;