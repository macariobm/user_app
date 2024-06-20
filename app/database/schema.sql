
create table if not exists users (
    id integer primary key autoincrement,
    name text not null,
    location text not null
);