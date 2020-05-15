create table public.albert_sploits
(
    id       serial                                             not null
        constraint albert_sploits_pkey
            primary key,
    datetime timestamp with time zone default CURRENT_TIMESTAMP not null,
    tech     text,
    version  text,
    cve      text
        constraint albert_sploits_cve_key
            unique,
    path     text
        constraint albert_sploits_path_key
            unique
);

alter table public.albert_sploits
    owner to albert;

create table public.albert_tools
(
    id               serial                                             not null
        constraint albert_tools_pkey
            primary key,
    datetime         timestamp with time zone default CURRENT_TIMESTAMP not null,
    operating_system text,
    path             text
        constraint albert_tools_path_key
            unique,
    type             text,
    purpose          text
);

alter table public.albert_tools
    owner to albert;

create table public.albert_loots
(
    id               serial                                             not null
        constraint albert_loots_pkey
            primary key,
    datetime         timestamp with time zone default CURRENT_TIMESTAMP not null,
    operating_system text,
    host             text,
    local_path       text,
    type_of_loot     text,
    persist          boolean,
    best_cve         text,
    used_cve         text
);

alter table public.albert_loots
    owner to albert;

create table public.albert_data
(
    id       serial                                             not null
        constraint albert_data_pkey
            primary key,
    dtg      timestamp with time zone default CURRENT_TIMESTAMP not null,
    when_run text
);

alter table public.albert_data
    owner to albert;

