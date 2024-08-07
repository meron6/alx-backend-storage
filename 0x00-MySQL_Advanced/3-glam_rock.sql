-- SQL script to list all bands with 'Glam rock' as their main style, sorted by their longevity
--
-- Requirements:
--
-- Import the table dump: metal_bands.sql.zip
-- Required column names: band_name and lifespan (in years)
-- Utilize attributes 'formed' and 'split' to calculate lifespan
-- The script should run on any SQL database
SELECT band_name, (IFNULL(split, YEAR(CURRENT_DATE)) - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;
