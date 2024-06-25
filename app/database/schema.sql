create table if not exists users (
    id serial primary key,
    name text not null,
    location text not null
);
