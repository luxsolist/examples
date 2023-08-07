drop table users;

create table users (
    id int not null auto_increment,
    user_id varchar(100) not null,
    password varchar(100) not null,
    name varchar(100),
    email varchar(100),
    is_active int default 1,
    primary key (id)
);
create unique index idx_user_name on users(user_id);