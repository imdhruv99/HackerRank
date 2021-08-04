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

**18. Higher Than 75 Marks**
```
SELECT Name FROM STUDENTS WHERE Marks > 75 ORDER BY RIGHT(Name, 3), ID;
```

**19. Employee Names**
```
SELECT name FROM Employee ORDER BY name ASC;
```

**20. Employee Salaries**
```
SELECT name FROM Employee WHERE salary > 2000 AND months < 10 ORDER BY employee_id ASC;
```