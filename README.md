# HUD-MFI-API Documentation

The Department of Housing and Urban Development (HUD) sets income limits that determine eligibility for assisted housing programs including the Public Housing, Section 8 project-based, Section 8 Housing Choice Voucher, Section 202 housing for the elderly, and Section 811 housing for persons with disabilities programs. HUD develops income limits based on Median Family Income estimates and Fair Market Rent area definitions for each metropolitan area, parts of some metropolitan areas, and each non-metropolitan county.

HUD also provides an API (Application Programming Interface) that makes it easy to access median family income estimates for each U.S. county. However, the HUD API only provides access to the most recent year's median family income estimate. Often it is informative to analyze housing affordability through time which requires access to HUD's historical median family income estimates.

The following documentation outlines the usage of a custom built API to solve this problem. This tool is in no way affiliated with HUD but provides a quick way to access HUD data for the years 2000 - 2020. It works as follows:

### Base URL

https://hud-mfi-api.herokuapp.com/

The above URL is the address to access the API. Going to that address currently will bring an empty page, but this address is important because it serves as the prefix for other addresses that will return relevant data.

### getall/

https://hud-mfi-api.herokuapp.com/getall

Going to this URL will return the data for every county.

### Get MFI for every County in a State

The following addresses will return the county median family income estimates for every county within the user entered state. 
get/state/USER_ENTERED_STATE_ABBREVIATION

https://hud-mfi-api.herokuapp.com/get/state/OR

### Get MFI for a single County

Access to data for individual counties is also possible.
get/fips/USER_ENTERED_COUNTY_FIPS_CODE

https://hud-mfi-api.herokuapp.com/get/fips/41051

If you know the five digit county fips code, you can pass that in after the "get/fips/" to access the data. The above example is for Multnomah County ("41051")

get/state/USER_ENTERED_STATE_ABBREVIATION/county/USER_ENTERED_COUNTY_NAME

https://hud-mfi-api.herokuapp.com/get/state/IL/county/Cook

To access county data by county name the user first has to pass in a state. This address is an extension of the get/state/ address. The county name has to be formatted in a specific way to work. It has to be capitalized, and including " County" at the end of the county name will cause the call to fail. 
