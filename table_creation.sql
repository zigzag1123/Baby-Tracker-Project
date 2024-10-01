use baby_tracker;


DROP TABLE IF EXISTS tbl_event_data;
DROP TABLE IF EXISTS tbl_child;
DROP TABLE IF EXISTS tbl_parents;


 CREATE TABLE tbl_parents
	(
		fld_p_username_pk VARCHAR(48),
        fld_p_password VARCHAR(48),
        fld_p_doc TIMESTAMP DEFAULT NOW(),
        CONSTRAINT p_pk PRIMARY KEY(fld_p_username_pk),
        CONSTRAINT p_not_null CHECK(fld_p_username_pk IS NOT NULL AND fld_p_password IS NOT NULL)
	);
CREATE TABLE tbl_child
	(
		fld_c_id_pk INTEGER AUTO_INCREMENT,
        fld_c_fname VARCHAR(48),
        fld_c_lname VARCHAR(48),
        fld_c_p_username_fk VARCHAR(48),
        fld_c_doc TIMESTAMP DEFAULT NOW(),
        CONSTRAINT c_pk PRIMARY KEY(fld_c_id_pk),
        CONSTRAINT c_not_null CHECK(fld_c_fname IS NOT NULL AND fld_c_lname IS NOT NULL),
        CONSTRAINT c_fk FOREIGN KEY(fld_c_p_username_fk) REFERENCES tbl_parents(fld_p_username_pk)
	);
CREATE TABLE tbl_event_data
	(
		fld_e_id_pk INTEGER AUTO_INCREMENT,
		fld_c_id_fk INTEGER,
        fld_event_type VARCHAR(15),
        fld_e_doc TIMESTAMP DEFAULT NOW(),
        CONSTRAINT e_d_fk FOREIGN KEY(fld_c_id_fk) REFERENCES tbl_child(fld_c_id_pk),
        CONSTRAINT e_d_pk PRIMARY KEY(fld_e_id_pk),
        CONSTRAINT e_d_not_null CHECK(fld_c_id_fk IS NOT NULL)
	);
