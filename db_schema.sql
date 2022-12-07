create table if not exists users(
              id SERIAL,
              phone varchar(12),
              uname varchar(30)
              lastmsg int,
              cart int,
              primary key(id,phone)
)

create table if not exists messages(
    id SERIAL,
    msg varchar(500)
    user int not null,
    primary key(id)
)
