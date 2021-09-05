create extension dblink;

-- create database if not exists
do $$
begin
  if exists (select from pg_database where datname = 'fsmetadata') then
    raise notice 'Database already exists';
  else
    perform dblink_exec('dbname=' || current_database(), 'create database fsmetadata');
  end if;
end $$;

