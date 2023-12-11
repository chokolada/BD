USE db_lab;
DROP PROCEDURE IF EXISTS InsertDataIntoTable;
DROP PROCEDURE IF EXISTS GetAvgUserBank;
DROP PROCEDURE IF EXISTS InsertDataIntoFarm;
DROP PROCEDURE IF EXISTS ShowTableNames;
DROP TRIGGER IF EXISTS farm_trigger;
DROP TRIGGER IF EXISTS before_insert_farm_trigger;
DROP TRIGGER IF EXISTS after_update_farm_trigger;
DROP TRIGGER IF EXISTS before_delete_farm_trigger;
DROP FUNCTION IF EXISTS GetColumnStats;
DROP FUNCTION IF EXISTS GetAvgUserBank;
DELIMITER //
CREATE TRIGGER farm_trigger
AFTER INSERT ON product
FOR EACH ROW
BEGIN
    -- Вставка значень в таблицю farm при додаванні запису в таблицю product
    INSERT INTO farm (farm_name, product_serial_number)
    VALUES ('Default Farm Name', NEW.serial_number);
END;
//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE InsertDataIntoTable(IN farm_name VARCHAR(255), IN goods_id INT)
BEGIN
    SET @query = CONCAT('INSERT INTO farm (farm_name, goods_id) VALUES (?, ?)');
    PREPARE statement FROM @query;
    SET @farm_name = farm_name;
    SET @goods_id = goods_id;
    EXECUTE statement USING @farm_name, @goods_id;
    DEALLOCATE PREPARE statement;
END;
//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE InsertDataIntoFarm()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 10 DO
        -- Insert data into the 'farm' table
        INSERT INTO farm (farm_name, goods_id, created_at, status) 
        VALUES (CONCAT('Farm', i), i, NOW(), 'Active');
        SET i = i + 1;
    END WHILE;
END;
//
DELIMITER ;


DELIMITER //
CREATE FUNCTION GetAvgUserBank() RETURNS DOUBLE DETERMINISTIC
BEGIN
    DECLARE avg_value DOUBLE;

    -- Використовуємо простий SQL-запит для обчислення середнього значення
    SELECT AVG(user_bank) INTO avg_value FROM user;

    -- Повернення результату
    RETURN avg_value;
END;
//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE ShowTableNames()
BEGIN
    -- Оголошення змінних
    DECLARE done INT DEFAULT FALSE;
    DECLARE tableName VARCHAR(255);

    -- Оголошення курсору для вибору імен таблиць
    DECLARE tableCursor CURSOR FOR
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = DATABASE();

    -- Обробка помилок
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Відкриття курсору
    OPEN tableCursor;

    -- Цикл отримання імен таблиць
    read_loop: LOOP
        -- Читання імені таблиці
        FETCH tableCursor INTO tableName;

        -- Вихід з циклу, якщо курсор порожній
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Виведення імені таблиці
        SELECT tableName AS TableName;
    END LOOP;

    -- Закриття курсору
    CLOSE tableCursor;
END;
//

DELIMITER ;
DELIMITER //
CREATE TRIGGER before_insert_farm_trigger
BEFORE INSERT ON farm
FOR EACH ROW
SET NEW.created_at = NOW();
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER after_update_farm_trigger
AFTER UPDATE ON farm
FOR EACH ROW
BEGIN
    INSERT INTO log_table (log_message) VALUES ('Запис оновлено');
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER before_delete_farm_trigger
BEFORE DELETE ON farm
FOR EACH ROW
BEGIN
    IF OLD.status = 'locked' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Нє, видалення неможливе, бо таблиця заблокована';
    END IF;
END;
//
DELIMITER ;

-- Виклики процедур та функцій
CALL InsertDataIntoTable('Cool Farm', 2);
-- CALL InsertDataIntoFarm();
SELECT GetAvgUserBank() AS 'AverageUserBank';
-- CALL ShowTableNames();

