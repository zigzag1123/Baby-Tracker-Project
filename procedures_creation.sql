use baby_tracker;

DROP PROCEDURE IF EXISTS proc_check_password;
DROP PROCEDURE IF EXISTS proc_delete_child;
DROP PROCEDURE IF EXISTS proc_delete_parent;
DROP PROCEDURE IF EXISTS proc_insert_event;
DROP PROCEDURE IF EXISTS proc_insert_child;
DROP PROCEDURE IF EXISTS proc_insert_parent;



DELIMITER $$
CREATE PROCEDURE proc_insert_parent
(
	IN p_username VARCHAR(48),
	IN p_password VARCHAR(48),
	INOUT parm_errlvl SMALLINT
)
LANGUAGE SQL
BEGIN
	SET parm_errlvl := 0;
    IF p_username IS NULL OR LENGTH(p_username) = 0
    OR p_password IS NULL OR LENGTH(p_password) = 0
		THEN SET parm_errlvl := 1;
	ELSEIF EXISTS(SELECT fld_p_username_pk FROM tbl_parents
				  WHERE fld_p_username_pk = p_username)
		THEN SET parm_errlvl := 2;
	ELSE
		INSERT INTO tbl_parents(fld_p_username_pk, fld_p_password)
        VALUES(p_username, p_password);
	END IF;
END $$



DELIMITER $$
CREATE PROCEDURE proc_insert_child
(
	IN c_fname VARCHAR(48),
	IN c_lname VARCHAR(48),
    IN c_p_username VARCHAR(48),
	INOUT parm_errlvl SMALLINT
)
LANGUAGE SQL
BEGIN
	SET parm_errlvl := 0;
    IF c_fname IS NULL OR LENGTH(c_fname) = 0 OR c_lname IS NULL OR LENGTH(c_lname) = 0 OR c_p_username IS NULL OR LENGTH(c_p_username) = 0
    THEN SET parm_errlvl := 1;
    ELSEIF NOT EXISTS (SELECT fld_p_username_pk FROM tbl_parents WHERE fld_p_username_pk = c_p_username)
    THEN SET parm_errlvl := 2;
    ELSE INSERT INTO tbl_child(fld_c_fname, fld_c_lname, fld_c_p_username)
		 VALUES(c_fname, c_lname, c_p_username);
	END IF;
END $$

DELIMITER $$
CREATE PROCEDURE proc_insert_event
(
	IN c_id INTEGER,
    IN e_type VARCHAR(15),
    INOUT parm_errlvl SMALLINT
)
LANGUAGE SQL
BEGIN
	SET parm_errlvl := 0;
    IF e_type != 'sleep' OR e_type != 'awake' OR e_type != 'diaper change'
    THEN SET parm_errlvl := 1;
    ELSEIF NOT EXISTS (SELECT fld_c_id_pk FROM tbl_child WHERE fld_c_id_pk = c_id) 
    THEN SET parm_errlvl := 2;
    ELSE
    INSERT INTO tbl_event_data(fld_c_id_fk, fld_evnet_type)
	VALUES(c_id, e_type);
    END IF;
END $$
    
    
DELIMITER $$
CREATE PROCEDURE proc_delete_parent
(
	IN p_username VARCHAR(48),
    INOUT parm_errlvl SMALLINT
)
LANGUAGE SQL
BEGIN
	SET parm_errlvl := 0;
    IF p_username IS NULL OR LENGTH(p_username) = 0 THEN SET parm_errlvl := 1;
    ELSEIF NOT EXISTS (SELECT fld_p_username_pk FROM tbl_parents WHERE fld_p_username_pk = p_username) THEN SET parm_errlvl := 2;
    ELSEIF EXISTS (SELECT fld_c_p_username FROM tbl_child WHERE fld_c_p_username = p_username) THEN SET parm_errlvl := 3;
    ELSE
		DELETE FROM tbl_parents WHERE fld_p_username_pk = p_username;
    END IF;
END $$


DELIMITER $$
CREATE PROCEDURE proc_delete_child
(
	IN c_id INTEGER,
    INOUT parm_errlvl SMALLINT
)
LANGUAGE SQL
BEGIN
	SET parm_errlvl := 0;
    IF c_id IS NULL OR c_id = 0 THEN SET parm_errlvl := 1;
    ELSEIF NOT EXISTS (SELECT fld_c_id_pk FROM tbl_child WHERE fld_c_id_pk = c_id) THEN SET parm_errlvl := 2;
    ELSE
		DELETE FROM tbl_event_data WHERE fld_c_id_fk = c_id;
		DELETE FROM tbl_child WHERE fld_c_id_pk = c_id;
    END IF;
END $$

DELIMITER $$
CREATE PROCEDURE proc_check_password
(
	IN p_username VARCHAR(48),
    IN p_password VARCHAR(48),
    INOUT parm_errlvl SMALLINT
)
LANGUAGE SQL

BEGIN
	DECLARE temp_pass VARCHAR(48);
    SET parm_errlvl := 0;
	IF NOT EXISTS (SELECT fld_p_password FROM tbl_parents
			       WHERE fld_p_username_pk = p_username)
		THEN
			SET parm_errlvl := 2;
	ELSEIF EXISTS (SELECT fld_p_password FROM tbl_parents
			       WHERE fld_p_username_pk = p_username)
		THEN SELECT fld_p_password FROM tbl_parents
        WHERE fld_p_username_pk = p_username INTO temp_pass;
        IF temp_pass = p_password THEN SET parm_errlvl := 0;
        ELSE SET parm_errlvl := 3;
        END IF;
	END IF;
END $$
