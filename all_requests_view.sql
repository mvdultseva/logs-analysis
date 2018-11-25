CREATE OR REPLACE VIEW public.all_requests_stats AS
select 
to_char(time, 'FMMonth DD, YYYY') as request_date,
cast(count(id) as decimal) as requests_count
from log
group by request_date
order by request_date;

ALTER TABLE public.all_requests_stats
    OWNER TO vagrant;