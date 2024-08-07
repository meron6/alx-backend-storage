-- Import the table dump
SOURCE metal_bands.sql;

-- Create a query that ranks country origins of bands by the number of fans
SELECT origin, SUM(nb_fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
