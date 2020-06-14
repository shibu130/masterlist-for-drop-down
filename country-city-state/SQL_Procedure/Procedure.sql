Delimiter $$

CREATE procedure `new`()
BEGIN
declare ide int default 0;
declare count int default 0;
declare n varchar(100);
declare i int;
declare var varchar(100);
declare stat3 varchar(100);
declare c1 cursor for select id,country_name from country;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET ide = 1;

open c1;
mainLoop:loop

fetch  c1 into i,n;

if ide=1 then
leave mainLoop;
end if;





SET @tbl=n;


SET @SQL=CONCAT('
CREATE TABLE IF NOT EXISTS `', @tbl,'` (id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT, state VARCHAR(10) NOT NULL,PRIMARY KEY (id)) ');

prepare stmt from @SQL;
execute stmt;
deallocate prepare stmt;


SET @query=concat('INSERT INTO ',@tbl,' (state) SELECT state_name FROM state WHERE',' co_id=',i);
prepare stmte from @query;
execute stmte;
deallocate prepare stmte;

-- next procedure to create country tables with the state inside them



end loop mainLoop;
end $$
delimiter ;