# SQL
----

**1. Revising the Select Query I**

```
SELECT * FROM CITY WHERE COUNTRYCODE = 'USA' AND POPULATION > 100000;
```

**2. Revising the Select Query II**

```
SELECT NAME FROM CITY WHERE COUNTRYCODE = 'USA' AND POPULATION > 120000;
```

**3. Select All**

```
SELECT * FROM CITY;
```

**4. Select By ID**

```
SELECT * FROM CITY WHERE ID = 1661;
```

**5. Japanese Cities' Attributes**

```
SELECT * FROM CITY WHERE COUNTRYCODE = 'JPN';
```

**6. Japanese Cities' Names**

```
SELECT NAME FROM CITY WHERE COUNTRYCODE = 'JPN';
```

**7. Weather Observation Station 1**

```
SELECT CITY, STATE FROM STATION;
```

**8. Weather Observation Station 2**
```
SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2) FROM STATION;
```


**9. Weather Observation Station 3**

```
SELECT DISTINCT CITY FROM STATION WHERE MOD(STATION.ID,2)=0 ORDER BY CITY;
```

**10. Weather Observation Station 4**

```
SELECT (COUNT(CITY) - COUNT(DISTINCT CITY)) FROM STATION;
```

**11. Weather Observation Station 5**
```
SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY), CITY LIMIT 1;


SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY) DESC, CITY LIMIT 1;
```

**12. Weather Observation Station 6**
```
SELECT DISTINCT CITY FROM STATION WHERE REGEXP_LIKE(CITY,'^[aeiou]');
```

**13. Weather Observation Station 7**
```
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '[aeiou]$';
```

**14. Weather Observation Station 8**
```
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[aeiou].*[aeiou]$';
```

**15. Weather Observation Station 9**
```
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP '^[aeiou].*$';
```

**16. Weather Observation Station 10**
```
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP '^*[aeiou]$';
```

**17. Weather Observation Station 11**
```
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP '^[aeiou].*[aeiou]$';
```

**18. Weather Observation Station 12**
```
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[^aeiouAEIOU]' AND CITY REGEXP '[^aeiouAEIOU]$';
```

**19. Higher Than 75 Marks**
```
SELECT Name FROM STUDENTS WHERE Marks > 75 ORDER BY RIGHT(Name, 3), ID;
```

**20. Employee Names**
```
SELECT name FROM Employee ORDER BY name ASC;
```

**21. Employee Salaries**
```
SELECT name FROM Employee WHERE salary > 2000 AND months < 10 ORDER BY employee_id ASC;
```

**22. The PADS**
```
SELECT CONCAT(NAME,'(',SUBSTR(OCCUPATION,1,1),')') AS N FROM OCCUPATIONS ORDER BY N;

SELECT CONCAT('There are a total of ',COUNT(OCCUPATION),' ',LOWER(OCCUPATION),'s.') FROM OCCUPATIONS GROUP BY OCCUPATION ORDER BY COUNT(OCCUPATION), OCCUPATION;
```

**23. Types of Triangle**
```
SELECT 
    CASE
        WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
        WHEN A = B AND B = C THEN 'Equilateral'
        WHEN A = B OR B = C OR A = C THEN 'Isosceles'
        ELSE 'Scalene'
    END
FROM TRIANGLES;
```

**24. Binary Tree Nodes**
```
SELECT N, 
	IF(P IS NULL, 'Root', 
		IF(B.N IN (SELECT P FROM BST), 'Inner', 'Leaf')) 
	FROM BST AS B ORDER BY N;
```