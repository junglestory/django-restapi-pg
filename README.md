# django-restapi-pg

This application is a Django Rest API with PostgreSQL.

## Requirements
- [Python](https://www.python.org/downloads/) 3.6+
- [VS Code](https://code.visualstudio.com/download)
- [Postman](https://www.postman.com/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- Board Table

```sql
CREATE SEQUENCE board_board_no_seq;

CREATE TABLE IF NOT EXISTS public.board
(
    board_no bigint NOT NULL DEFAULT nextval('board_board_no_seq'::regclass),
    title character varying(200) COLLATE pg_catalog."default" NOT NULL,
    contents text COLLATE pg_catalog."default" NOT NULL,
    writer character varying(50) COLLATE pg_catalog."default" NOT NULL,
    view_count integer NOT NULL,
    link_url character varying(200) COLLATE pg_catalog."default" NOT NULL,
    create_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    update_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT board_pkey PRIMARY KEY (board_no)
)

CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.update_date = CURRENT_TIMESTAMP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER board_update_timestamp_trigger
BEFORE UPDATE ON public.board
FOR EACH ROW
EXECUTE PROCEDURE update_timestamp();
```
