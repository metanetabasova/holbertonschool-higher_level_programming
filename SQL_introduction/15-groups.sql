-- eyni xalamalik qeydlerin sayini qriplasirir ve sayina gore azalan sira ile duzur
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
