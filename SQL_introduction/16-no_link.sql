-- score ve name olaraq, bali azalan sira ile siralayir
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
