-- auto-generated definition
create table albert_data
(
    id       serial not null
        constraint albert_data_pkey
            primary key,
    datetime timestamp with time zone,
    when_run text
);

alter table albert_data
    owner to albert;

-- auto-generated definition
create table albert_sploits
(
    id       serial not null
        constraint albert_sploits_pkey
            primary key,
    datetime timestamp with time zone,
    tech     text,
    version  text,
    cve      text
        constraint albert_sploits_cve_key
            unique,
    path     text
        constraint albert_sploits_path_key
            unique
);

alter table albert_sploits
    owner to albert;

-- auto-generated definition
create table albert_loots
(
    id               serial not null
        constraint albert_loots_pkey
            primary key,
    datetime         timestamp with time zone,
    operating_system text,
    host             text,
    local_path       text,
    type_of_loot     text,
    persist          boolean
);

alter table albert_loots
    owner to albert;

-- auto-generated definition
create table albert_tools
(
    id               serial not null
        constraint albert_tools_pkey
            primary key,
    datetime         timestamp with time zone,
    operating_system text,
    path             text
        constraint albert_tools_path_key
            unique,
    type             text,
    purpose          text
);

alter table albert_tools
    owner to albert;

