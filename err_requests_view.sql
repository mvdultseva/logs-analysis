CREATE OR REPLACE VIEW public.err_requests_stats AS
select 
to_char(time, 'FMMonth DD, YYYY') as request_date,
cast(count(id) as decimal) err_requests_cnt
from log
where status != '200 OK'
group by request_date
order by request_date;

ALTER TABLE public.err_requests_stats
    OWNER TO vagrant;