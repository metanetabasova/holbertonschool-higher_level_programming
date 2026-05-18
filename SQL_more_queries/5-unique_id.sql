-- 'unique_id' cədvəlini yaradır, id sütununa default 1 və bənzərsizlik (UNIQUE) şərti qoyur
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
