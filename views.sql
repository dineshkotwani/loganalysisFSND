create or replace view popularposts as 
select a.title,Stats.reads from (select substr(path,10) as sluglog,count(path) as reads  from log group by path ) as Stats join articles a on a.slug = Stats.sluglog order by Stats.reads desc LIMIT 3 ;


create or replace view popularauthors as 
select authortest.name,sum(authortest.reads) as viewcounts  from (select Stats.sluglog,Stats.reads,a.author,au.name from (select substr(path,10) as sluglog,count(path) as reads  from log group by path ) as Stats join articles a on a.slug = Stats.sluglog
join authors au on au.id =a.author order by Stats.reads desc) as authortest group by authortest.name order by viewcounts desc LIMIT 3 ;


create or replace view failureday as 
select t1.day , round((t2.errorrequests * 100.0)/t1.totalrequests, 2) as percent from (select date_trunc('day',time) as day,count(*) as totalrequests from log  group by date_trunc('day',time) order by day) 
as t1 join 
(select foo.day,foo.errorrequests from (select date_trunc('day',time) as day,count(*) as errorrequests from log where status<>'200 OK' group by date_trunc('day',time) order by day)as foo) as t2
on t1.day = t2.day where ((t2.errorrequests * 100.0)/t1.totalrequests) > 1 ;

