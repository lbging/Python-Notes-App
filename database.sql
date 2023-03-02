CREATE DATABASE IF NOT EXISTS Python1;
use Python1;

CREATE TABLE users(
id          int(25) auto_increment not null,
name        varchar(100),
lastname    varchar(255),
mail        varchar(255) not null,
password    varchar(255) not null,
date        date not null,
CONSTRAINT  pk_users PRIMARY KEY(id),
CONSTRAINT  uq_mail UNIQUE(mail)
)ENGINE=InnoDb;

CREATE TABLE notes(
id          int(25) auto_increment not null,
user_id     int(25) not null,
title       varchar(255) not null,
content     mediumtext,
date        date not null,
CONSTRAINT  pk_notes PRIMARY KEY(id),
CONSTRAINT  fk_note_user FOREIGN KEY(user_id) REFERENCES users(id)
)ENGINE=InnoDb; 