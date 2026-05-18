-- cedvel yaradir, id sutununa default 1 ve benzerdizlik serti qoyur
CREATE TSBLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
