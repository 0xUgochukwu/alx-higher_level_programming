-- Cities of Carlifonia

SELECT id, name FROM citites WHERE state_id = (SELECT id FROM states WHERE name='California') ORDER BY id ASC;
