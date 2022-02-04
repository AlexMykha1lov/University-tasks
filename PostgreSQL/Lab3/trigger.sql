--before delete, update

CREATE TABLE "book"(
"book_id" serial PRIMARY KEY,
"book_title" text,
"book_pages" int
);

CREATE TABLE "book_log"(
"id" serial PRIMARY KEY,
"book_log_id" int,
"book_log_name" text
);

INSERT INTO "book"("book_title", "book_pages")
VALUES ('book1' , '100'), ('book2', '200'), ('book3', '300'), ('book4', '400'),
('book5', '500'), ('book6', '600'), ('book7', '700'), ('book8', '800'), 
('book9', '900'), ('book9', '1000') ;




CREATE OR REPLACE FUNCTION before_delete_update_func() RETURNS TRIGGER as $trigger$
DECLARE
	
BEGIN
	IF old."book_pages" <= 500 THEN
		RAISE NOTICE 'book_pages <= 500';
		INSERT INTO "book_log"("book_log_id", "book_log_name") VALUES (old."book_id", old."book_title" || '_short');
		RETURN OLD;
	ELSE
		RAISE NOTICE 'book_pages >= 500';
		INSERT INTO "book_log"("book_log_id", "book_log_name") VALUES (old."book_id", old."book_title" || '_long');
		RETURN OLD;
	END IF;

END;
$trigger$ LANGUAGE plpgsql;

CREATE TRIGGER "before_delete_update_trigger"
BEFORE DELETE OR UPDATE ON "book"
FOR EACH ROW
EXECUTE procedure before_delete_update_func(); 





DELETE FROM "book" where "book_id" = 4;

UPDATE "book" SET "book_title" = "book_title" WHERE "book_pages" = 800;
