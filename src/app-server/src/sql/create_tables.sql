/*
TODO:
1. Change schema for hash pwd
*/

create table if not exists users (
  -- user_id uuid default gen_random_uuid() primary key
  user_id bigint generated always as identity primary key, 
  username varchar(50) unique not null,  
  password varchar(50) not null,
  created_at timestamp not null,
  updated_at timestamp,
  last_login_at timestamp
);


create table if not exists objects (
  object_id bigint generated always as identity primary key,
  user_id bigint references users(user_id),
  object_type varchar(6) not null,
  parent_object_id bigint default null,
  name varchar(255) not null,
  created_at timestamp not null,
  updated_at timestamp
);


create table if not exists AccessControlList (
  user_id bigint references users(user_id),
  object_id bigint references objects(object_id),
  created_at timestamp not null,
  updated_at timestamp
);


create table if not exists chunks (
  chunk_id bigint generated always as identity primary key,
  object_id bigint references objects(object_id),
  url varchar not null,
  created_at timestamp not null,
  updated_at timestamp
);

