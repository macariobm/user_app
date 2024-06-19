drop tabe if exists users;
create table users (
    id integer primary key autoincrement,
    name text not null,
    location text not null,
)