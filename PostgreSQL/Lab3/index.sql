-- Btree
CREATE INDEX or_index ON “Author”(origin);
DROP INDEX if exists or_index;

explain analyze select * from “Author” where origin  = ’Mali’ ;

explain analyze select * from “Author” where origin  = ’Mali’ and origin  = ’Chile’ and origin  = ’Panama’;

explain analyze select * from “Author” where origin  != ’Mali’ and origin  != ’Chile’ and origin  != ’Panama’ and origin  != ’Ukraine’;

explain analyze select * from “Author” where author_id < 10000 ORDER BY origin;



--BRIN
CREATE INDEX or_brin_index on “Author” using brin (origin) with(pages_per_range=128);
DROP INDEX if exists or_brin_index;

explain analyze select * from “Author” where origin  = ’Mali’ ;

explain analyze select count(name) from “Author” where origin  != ’Mali’;

explain analyze select count(name) from “Author” where origin  = ’Mali’ and origin  = ’Chile’ and origin  = ’Panama’;

explain analyze select count(name) from “Author” where origin  != ’Mali’ and origin  != ’Chile’ and origin  != ’Panama’ and origin  != ’Ukraine’;