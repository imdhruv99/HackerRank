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

**8. Weather Observation Station 3**

```
SELECT DISTINCT CITY FROM STATION WHERE MOD(STATION.ID,2)=0 ORDER BY CITY;
```

**9. Weather Observation Station 4**

```
SELECT (count(CITY) - count(DISTINCT CITY)) FROM STATION;
```