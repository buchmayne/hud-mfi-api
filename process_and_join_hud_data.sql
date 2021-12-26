select
	raw_mfi_2021.state_alpha,
	raw_mfi_2021.state_name,
	case 
		when char_length(cast(fips2010 as varchar(15))) = 9
			then '0' || cast(fips2010 as varchar(15))
		else cast(fips2010 as varchar(15))
		end as fips,
	case 
		when char_length(cast("state" as varchar(2))) = 2
			then cast("state" as varchar(2))
		else '0' || cast("state" as varchar(2))
		end as state_code,
	case
		when char_length(cast("county" as varchar(3))) = 1
			then '00' || cast("county" as varchar(3))
		when char_length(cast("county" as varchar(3))) = 2
			then '0' || cast("county" as varchar(3))
		else cast("county" as varchar(3))
		end as county_code,
	(case 
		when char_length(cast("state" as varchar(2))) = 2
			then cast("state" as varchar(2))
		else '0' || cast("state" as varchar(2))
		end || 
	case
		when char_length(cast("county" as varchar(3))) = 1
			then '00' || cast("county" as varchar(3))
		when char_length(cast("county" as varchar(3))) = 2
			then '0' || cast("county" as varchar(3))
		else cast("county" as varchar(3))
		end) as geoid,
	raw_mfi_2021.county_name,
	raw_mfi_2021.metro_area_name,
	"median2021" as mfi2021,
	"median2020" as mfi2020,
	"median2019" as mfi2019,
	"median2018" as mfi2018,
	"median2017" as mfi2017,
	"median2016" as mfi2016,
	"median2015" as mfi2015,
	"median2014" as mfi2014,
	"median2013" as mfi2013
from raw_mfi_2021
inner join (select
				"state_name",
				"county_name",
				"median2020"
			from raw_mfi_2020
			) mfi2020
	on (raw_mfi_2021.state_name = mfi2020.state_name and raw_mfi_2021.county_name = mfi2020.county_name)
inner join (select
				"state_name",
				"county_name",
				"median2019"
			from raw_mfi_2019
			) mfi2019
	on (raw_mfi_2021.state_name = mfi2019.state_name and raw_mfi_2021.county_name = mfi2019.county_name)
inner join (select
				"state_name",
				"county_name",
				"median2018"
			from raw_mfi_2018
			) mfi2018
	on (raw_mfi_2021.state_name = mfi2018.state_name and raw_mfi_2021.county_name = mfi2018.county_name)
inner join (select
				"state_name",
				"county_name",
				"median2017"
			from raw_mfi_2017
			) mfi2017
	on (raw_mfi_2021.state_name = mfi2017.state_name and raw_mfi_2021.county_name = mfi2017.county_name)
inner join (select
				"state_name",
				"county_town_name",
				"median2016"
			from raw_mfi_2016
			) mfi2016
	on (raw_mfi_2021.state_name = mfi2016.state_name and raw_mfi_2021.county_name = mfi2016.county_town_name)
inner join (select
				"state_name",
				"county_town_name",
				"median2015"
			from raw_mfi_2015
			) mfi2015
	on (raw_mfi_2021.state_name = mfi2015.state_name and raw_mfi_2021.county_name = mfi2015.county_town_name)
inner join (select
				"state_name",
				"county_town_name",
				"median2014"
			from raw_mfi_2014
			) mfi2014
	on (raw_mfi_2021.state_name = mfi2014.state_name and raw_mfi_2021.county_name = mfi2014.county_town_name)
inner join (select
				"state_name",
				"county_town_name",
				"median2013"
			from raw_mfi_2013
			) mfi2013
	on (raw_mfi_2021.state_name = mfi2013.state_name and raw_mfi_2021.county_name = mfi2013.county_town_name)
where "state_alpha" not in ('VI', 'UM', 'PR', 'MP', 'GU', 'AS')
;