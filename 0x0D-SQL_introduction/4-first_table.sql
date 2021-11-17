-- Write a script that creates a table called first_table
-- in the current database in your MySQL server.
create table first_table if not exists(
    id int,
    name varchar(256)
);
