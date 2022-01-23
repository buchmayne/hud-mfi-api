sql_queries = (
    """
        create table mficlean as
    select
        raw_mfi_2021.state_alpha,
        raw_mfi_2021.state_name,
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
        raw_mfi_2021.metro_area_name,
        raw_mfi_2021.county_name,
        "median2021" as mfi2021,
        "median2020" as mfi2020,
        "median2019" as mfi2019,
        "median2018" as mfi2018,
        "median2017" as mfi2017,
        "median2016" as mfi2016,
        "median2015" as mfi2015,
        "median2014" as mfi2014,
        "median2013" as mfi2013,
        "median2012" as mfi2012,
        "median2011" as mfi2011,
        "median2010" as mfi2010,
        "median2009" as mfi2009,
        "median2008" as mfi2008,
        "median2007" as mfi2007,
        "median2006" as mfi2006,
        "median2005" as mfi2005,
        "median2004" as mfi2004,
        "median2003" as mfi2003,
        "median2002" as mfi2002,
        "median2001" as mfi2001,
        "median2000" as mfi2000
    from raw_mfi_2021
    inner join (
        with row_number_idx_2020 as (
            select
                "state_name",
                "county_name",
                row_number() over(partition by state_name, county_name order by median2020 desc) as idx,
                "median2020"
            from raw_mfi_2020
            where state_name = 'New York'
        )
        select 
            "state_name",
            "county_name",
            "median2020"
        from row_number_idx_2020
        where idx = 1
        
        union all
        
        select 
            "state_name",
            "county_name",
            "median2020"
        from raw_mfi_2020
        where state_name != 'New York'
        ) mfi2020
        on (raw_mfi_2021.state_name = mfi2020.state_name and raw_mfi_2021.county_name = mfi2020.county_name)
    inner join (
        with row_number_idx_2019 as (
            select
                "state_name",
                "county_name",
                row_number() over(partition by state_name, county_name order by median2019 desc) as idx,
                "median2019"
            from raw_mfi_2019
            where state_name = 'New York'
        )
        select 
            "state_name",
            "county_name",
            "median2019"
        from row_number_idx_2019
        where idx = 1
        
        union all
        
        select 
            "state_name",
            "county_name",
            "median2019"
        from raw_mfi_2019
        where state_name != 'New York'
        ) mfi2019
        on (raw_mfi_2021.state_name = mfi2019.state_name and raw_mfi_2021.county_name = mfi2019.county_name)
    inner join (
        with row_number_idx_2018 as (
            select
                "state_name",
                "county_name",
                row_number() over(partition by state_name, county_name order by median2018 desc) as idx,
                "median2018"
            from raw_mfi_2018
            where state_name = 'New York'
        )
        select 
            "state_name",
            "county_name",
            "median2018"
        from row_number_idx_2018
        where idx = 1
        
        union all
        
        select 
            "state_name",
            "county_name",
            "median2018"
        from raw_mfi_2018
        where state_name != 'New York'
        ) mfi2018
        on (raw_mfi_2021.state_name = mfi2018.state_name and raw_mfi_2021.county_name = mfi2018.county_name)
    inner join (
        with row_number_idx_2017 as (
            select
                "state_name",
                "county_name",
                row_number() over(partition by state_name, county_name order by median2017 desc) as idx,
                "median2017"
            from raw_mfi_2017
            where state_name = 'New York'
        )
        select 
            "state_name",
            "county_name",
            "median2017"
        from row_number_idx_2017
        where idx = 1
        
        union all
        
        select 
            "state_name",
            "county_name",
            "median2017"
        from raw_mfi_2017
        where state_name != 'New York'
        ) mfi2017
        on (raw_mfi_2021.state_name = mfi2017.state_name and raw_mfi_2021.county_name = mfi2017.county_name)
    inner join (
        with row_number_idx_2016 as (
            select
                "state_name",
                "county_town_name",
                row_number() over(partition by state_name, county_town_name order by median2016 desc) as idx,
                "median2016"
            from raw_mfi_2016
            where state_name = 'New York'
        )
        select 
            "state_name",
            "county_town_name",
            "median2016"
        from row_number_idx_2016
        where idx = 1
        
        union all
        
        select 
            "state_name",
            "county_town_name",
            "median2016"
        from raw_mfi_2016
        where state_name != 'New York'
        ) mfi2016
        on (raw_mfi_2021.state_name = mfi2016.state_name and raw_mfi_2021.county_name = mfi2016.county_town_name)
    inner join (
        with row_number_idx_2015 as (
            select
                "state_name",
                "county_town_name",
                row_number() over(partition by state_name, county_town_name order by median2015 desc) as idx,
                "median2015"
            from raw_mfi_2015
            where state_name = 'New York'
        )
        select 
            "state_name",
            "county_town_name",
            "median2015"
        from row_number_idx_2015
        where idx = 1
        
        union all
        
        select 
            "state_name",
            "county_town_name",
            "median2015"
        from raw_mfi_2015
        where state_name != 'New York'
        ) mfi2015
        on (raw_mfi_2021.state_name = mfi2015.state_name and raw_mfi_2021.county_name = mfi2015.county_town_name)
    inner join (
        with row_number_idx_2014 as (
            select
                "state_name",
                "county_town_name",
                row_number() over(partition by state_name, county_town_name order by median2014 desc) as idx,
                "median2014"
            from raw_mfi_2014
            where state_name = 'New York'
        )
        select 
            "state_name",
            "county_town_name",
            "median2014"
        from row_number_idx_2014
        where idx = 1
        
        union all
        
        select 
            "state_name",
            "county_town_name",
            "median2014"
        from raw_mfi_2014
        where state_name != 'New York'
        ) mfi2014
        on (raw_mfi_2021.state_name = mfi2014.state_name and raw_mfi_2021.county_name = mfi2014.county_town_name)
    inner join (
        with row_number_idx_2013 as (
            select
                "state_name",
                "county_town_name",
                row_number() over(partition by state_name, county_town_name order by median2013 desc) as idx,
                "median2013"
            from raw_mfi_2013
            where state_name = 'New York'
        )
        select 
            "state_name",
            "county_town_name",
            "median2013"
        from row_number_idx_2013
        where idx = 1
        
        union all
        
        select 
            "state_name",
            "county_town_name",
            "median2013"
        from raw_mfi_2013
        where state_name != 'New York'
        ) mfi2013
        on (raw_mfi_2021.state_name = mfi2013.state_name and raw_mfi_2021.county_name = mfi2013.county_town_name)
    inner join (
        with row_number_idx_2012 as (
            select
                "state_name",
                "county_town_name",
                row_number() over(partition by state_name, county_town_name order by median2012 desc) as idx,
                "median2012"
            from raw_mfi_2012
            where state_name = 'New York'
        )
        select 
            "state_name",
            "county_town_name",
            "median2012"
        from row_number_idx_2012
        where idx = 1
        
        union all
        
        select 
            "state_name",
            "county_town_name",
            "median2012"
        from raw_mfi_2012
        where state_name != 'New York'
        ) mfi2012
        on (raw_mfi_2021.state_name = mfi2012.state_name and raw_mfi_2021.county_name = mfi2012.county_town_name)
    inner join (
        with row_number_idx_2011 as (
            select
                "state_name",
                "county_town_name",
                row_number() over(partition by state_name, county_town_name order by median2011 desc) as idx,
                "median2011"
            from raw_mfi_2011
            where state_name = 'New York'
        )
        select 
            "state_name",
            "county_town_name",
            "median2011"
        from row_number_idx_2011
        where idx = 1
        
        union all
        
        select 
            "state_name",
            "county_town_name",
            "median2011"
        from raw_mfi_2011
        where state_name != 'New York'
        ) mfi2011
        on (raw_mfi_2021.state_name = mfi2011.state_name and raw_mfi_2021.county_name = mfi2011.county_town_name)
    inner join (
        with row_number_idx_2010 as (
            select
                "state_name",
                "county_town_name",
                row_number() over(partition by state_name, county_town_name order by median2010 desc) as idx,
                "median2010"
            from raw_mfi_2010
            where state_name = 'New York'
        )
        select 
            "state_name",
            "county_town_name",
            "median2010"
        from row_number_idx_2010
        where idx = 1
        
        union all
        
        select 
            "state_name",
            "county_town_name",
            "median2010"
        from raw_mfi_2010
        where state_name != 'New York'
        ) mfi2010
        on (raw_mfi_2021.state_name = mfi2010.state_name and raw_mfi_2021.county_name = mfi2010.county_town_name)
    inner join (
        with row_number_idx_2009 as (
            select
                "state_name",
                "county_town_name",
                row_number() over(partition by state_name, county_town_name order by median2009 desc) as idx,
                "median2009"
            from raw_mfi_2009
            where state_name = 'New York'
        )
        select 
            "state_name",
            "county_town_name",
            "median2009"
        from row_number_idx_2009
        where idx = 1
        
        union all
        
        select 
            "state_name",
            "county_town_name",
            "median2009"
        from raw_mfi_2009
        where state_name != 'New York'
        ) mfi2009
        on (raw_mfi_2021.state_name = mfi2009.state_name and raw_mfi_2021.county_name = mfi2009.county_town_name)
    inner join (
        with row_number_idx_2008 as (
            select
                "state_name",
                "county_town_name",
                row_number() over(partition by state_name, county_town_name order by median2008 desc) as idx,
                "median2008"
            from raw_mfi_2008
            where state_name = 'New York'
        )
        select 
            "state_name",
            "county_town_name",
            "median2008"
        from row_number_idx_2008
        where idx = 1
        
        union all
        
        select 
            "state_name",
            "county_town_name",
            "median2008"
        from raw_mfi_2008
        where state_name != 'New York'
        ) mfi2008
        on (raw_mfi_2021.state_name = mfi2008.state_name and raw_mfi_2021.county_name = mfi2008.county_town_name)
    inner join (
        with row_number_idx_2007 as (
            select
                "state_name",
                "county_town_name",
                row_number() over(partition by state_name, county_town_name order by median2007 desc) as idx,
                "median2007"
            from raw_mfi_2007
            where state_name = 'New York'
        )
        select 
            "state_name",
            "county_town_name",
            "median2007"
        from row_number_idx_2007
        where idx = 1
        
        union all
        
        select 
            "state_name",
            "county_town_name",
            "median2007"
        from raw_mfi_2007
        where state_name != 'New York'
        ) mfi2007
        on (raw_mfi_2021.state_name = mfi2007.state_name and raw_mfi_2021.county_name = mfi2007.county_town_name)
    inner join (select
                    "state_name",
                    "state_alpha",
                    "county_town_name",
                    "median2006"
                from raw_mfi_2006
                ) mfi2006
        on (raw_mfi_2021.state_name = mfi2006.state_name and raw_mfi_2021.county_name = mfi2006.county_town_name and raw_mfi_2021.state_alpha = mfi2006.state_alpha)
    inner join (select
                    "state_alpha",
                    "countyname",
                    "median2005"
                from raw_mfi_2005
                ) mfi2005
        on (raw_mfi_2021.state_alpha = mfi2005.state_alpha and raw_mfi_2021.county_name = mfi2005.countyname)
    inner join (select
                    "state_alpha",
                    "countyname",
                    "median2004"
                from raw_mfi_2004
                ) mfi2004
        on (raw_mfi_2021.state_alpha = mfi2004.state_alpha and raw_mfi_2021.county_name = mfi2004.countyname)
    inner join (select
                    "state_alpha",
                    "countyname",
                    "median2003"
                from raw_mfi_2003
                ) mfi2003
        on (raw_mfi_2021.state_alpha = mfi2003.state_alpha and raw_mfi_2021.county_name = mfi2003.countyname)
    inner join (select
                    "statealpha",
                    INITCAP("county_name") as county_name,
                    "median" as median2002
                from raw_mfi_2002
                ) mfi2002
        on (raw_mfi_2021.state_alpha = mfi2002.statealpha and raw_mfi_2021.county_name = mfi2002.county_name)
    inner join (select
                    "state_abrev." as statealpha,
                    "county_name",
                    "fy_2001_median_family_income" as median2001
                from raw_mfi_2001
                ) mfi2001
        on (raw_mfi_2021.state_alpha = mfi2001.statealpha and raw_mfi_2021.county_name = mfi2001.county_name)
    inner join (select
                    "state_abrev." as statealpha,
                    "county_name",
                    "fy_2000_median_family_income" as median2000
                from raw_mfi_2000
                ) mfi2000
        on (raw_mfi_2021.state_alpha = mfi2000.statealpha and raw_mfi_2021.county_name = mfi2000.county_name)
    where raw_mfi_2021.state_alpha not in ('VI', 'UM', 'PR', 'MP', 'GU', 'AS')
    ;
    """,
    """
        create table mfifinal as
        select 
            "state_alpha",
            "state_name",
            "state_code",
            "county_code",
            "geoid",
            "metro_area_name",
            replace("county_name", ' County', '') as "county_name",
            "mfi2021",
            "mfi2020",
            "mfi2019",
            "mfi2018",
            "mfi2017",
            "mfi2016",
            "mfi2015",
            "mfi2014",
            "mfi2013",
            "mfi2012",
            "mfi2011",
            "mfi2010",
            "mfi2009",
            "mfi2008",
            "mfi2007",
            "mfi2006",
            "mfi2005",
            "mfi2004",
            "mfi2003",
            "mfi2002",
            "mfi2001",
            "mfi2000"
        from mficlean 
        ;
    """,
    """
        drop table 
            raw_mfi_2021,
            raw_mfi_2020,
            raw_mfi_2019,
            raw_mfi_2018,
            raw_mfi_2017,
            raw_mfi_2016,
            raw_mfi_2015,
            raw_mfi_2014,
            raw_mfi_2013,
            raw_mfi_2012,
            raw_mfi_2011,
            raw_mfi_2010,
            raw_mfi_2009,
            raw_mfi_2008,
            raw_mfi_2007,
            raw_mfi_2006,
            raw_mfi_2005,
            raw_mfi_2004,
            raw_mfi_2003,
            raw_mfi_2002,
            raw_mfi_2001,
            raw_mfi_2000,
            mficlean
        ;
    """,
)
