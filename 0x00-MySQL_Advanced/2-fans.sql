-- A  SQL script that ranks country origins of bands, ordered
-- by the number of (non-unique) fans

SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP by origin
ORDER BY nb_fans DESC;