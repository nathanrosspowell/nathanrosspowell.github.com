drop table if exists posts;
create table posts (
    id integer primary key autoincrement,
    title string not null,
    post string not null,
    author string not null,
    posted date not null,
    tags string not null
);

drop table if exists tags;
create table tags (
    id integer primary key autoincrement,
    tag string not null
);
