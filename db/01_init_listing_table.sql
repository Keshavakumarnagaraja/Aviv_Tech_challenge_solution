CREATE USER postgres;

CREATE TABLE IF NOT EXISTS public.listing
(
    id                   serial           primary key,
    name                 varchar          not null,
    description          varchar          not null,
    building_type        varchar          not null,
    street_address       varchar          not null,
    postal_code          varchar          not null,
    city                 varchar          not null,
    country              varchar          not null,
    surface_area_m2      double precision not null,
    rooms_count          integer          not null,
    bedrooms_count       integer          not null,
    price                double precision not null,
    contact_phone_number varchar,
    created_date         timestamp,
    updated_date         timestamp
);




CREATE TABLE IF NOT EXISTS public.listing_price_log 
(
	id serial4 NOT NULL,
	listing_id int4 NULL,
	price float8 NULL,
	updated_time timestamp NULL,
	CONSTRAINT listing_price_log_pkey PRIMARY KEY (id)
);


-- public.listing_price_log foreign keys

ALTER TABLE public.listing_price_log ADD CONSTRAINT listing_price_log_listing_id_fkey FOREIGN KEY (listing_id) REFERENCES public.listing(id);


CREATE OR REPLACE FUNCTION public.insert_listing_price_log()
 RETURNS TRIGGER
 LANGUAGE plpgsql
AS $function$
BEGIN
    -- Check if the price has been modified before insertion
    IF TG_OP = 'UPDATE' THEN
        IF OLD.price <> NEW.price THEN
            INSERT INTO public.listing_price_log (listing_id, price, updated_time)
            VALUES (NEW.id, NEW.price, NEW.updated_date);
        END IF;
    ELSIF TG_OP = 'INSERT' THEN
        INSERT INTO public.listing_price_log (listing_id, price, updated_time)
        VALUES (NEW.id, NEW.price, NEW.updated_date);
    END IF;
    RETURN NEW;
END;
$function$;


CREATE TRIGGER insert_listing_price_log_trigger
AFTER INSERT OR UPDATE ON public.listing
FOR EACH ROW
EXECUTE FUNCTION insert_listing_price_log();