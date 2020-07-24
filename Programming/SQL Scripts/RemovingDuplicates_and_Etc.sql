-- Remove duplicates, using the in-built Postgres CTID
DELETE FROM govt_respond_tracker T1
USING govt_respond_tracker T2
WHERE T1.ctid < T2.ctid
AND T1.datec = T2.datec
AND T1.countryname = T2.countryname;

-- Confirm if it succeed, by viewing the content
SELECT * FROM govt_respond_tracker;

-- Print the content by its order of countryname and datec in ascending order
SELECT *
FROM govt_respond_tracker
ORDER BY
countryname ASC,
datec ASC;

-- Count the total rows of a column
SELECT datec, count(*)
FROM govt_respond_tracker
GROUP BY datec
HAVING COUNT(*) > 1
ORDER BY datec ASC;

-- Print the content from table for a specific value and ordered it by another column in ascending order
SELECT * FROM govt_respond_tracker
WHERE countryname = 'Aruba'
ORDER BY datec ASC;

-- Print the content from selected columns from a table exactly, ordered it by another column in ascending order
SELECT DISTINCT countryname, countrycode, confirmedcases, confirmeddeaths
FROM govt_respond_tracker
ORDER BY countryname ASC;