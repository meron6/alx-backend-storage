-- Task 2: Best band ever! - Rank the countries of origin of bands,
-- ordered by the total number of (non-unique) fans
SELECT `origin`, SUM(`fans`) AS `nb_fans` FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;
