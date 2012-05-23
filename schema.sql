drop table if exists posts;
create table posts (
    id integer primary key autoincrement,
    title string not null,
    post string not null,
    author string not null,
    posted date not null,
    modified date not null,
    tags string not null
);
