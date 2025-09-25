create database webappmusic;

use webappmusic;

create table if not exists music(
	id int primary key auto_increment not null,
    name varchar(30) not null,
    artist varchar(50) not null,
    genre varchar(20) not null
);

create table if not exists user(
	id int primary key auto_increment not null,
    name varchar(50) not null,
    login varchar(20) not null,
    password varchar(15) not null
);

insert into music(name, artist, genre)
values("O Sol", "Vitor Kley", "Pop"),
("solteiro Não Trai", "Tayrone", "Arroche"),
("Dependente", "Silvanno Salles", "Arocha"),
("Meu Abrido", "Melim", "Pop");

insert into user(name, login, password)
values("Felipe Venas", "felipe.venas", "admin");

select * from user;
select * from music;

update music set genre = "Arrocha" where id = 2;
update music set name = "Solteiro Não Trai" where id = 2;
update music set name = "Meu Abrigo" where id = 4;

select * from music where genre like "A%";







