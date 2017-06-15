drop database if exists csdb;

create database csdb;

use csdb;

create table tickets (
id int not null auto_increment,
ticket_id bigint,
player_id bigint,
group_id tinytext,
platform tinytext,
ticket_created datetime,
last_update datetime,
location tinytext,
ticket_tags tinytext,

primary key (id),
index (player_id),
index (ticket_id)
);

create table comments (
id int not null auto_increment,
ticket_id bigint,
comment_text	text,
comment_author tinytext,
comment_datetime date,

primary key (id),
index (ticket_id),

foreign key (ticket_id)
references tickets(ticket_id)
);
