/* 
Date created 3rd August 2020
Date updated 1st September 2020
By Aldy Rasyid Abe
*/

/*
OPTIONAL
*/
VACUUM FULL;

/*
1. Create new table called govt_response_tracker
*/
CREATE TABLE govt_response_tracker
(
	CountryName varchar,
	CountryCode varchar,
	RegionName varchar,
	RegionCode varchar,
	DateC varchar,
	C1_School_closing varchar,	
	C1_Flag varchar,
	C2_Workplace_closing varchar,
	C2_Flag	varchar,
	C3_Cancel_public_events varchar,
	C3_Flag varchar,
	C4_Restrictions_on_gatherings varchar,
	C4_Flag varchar,
	C5_Close_public_transport varchar,
	C5_Flag varchar,
	C6_Stay_at_home_requirements varchar,
	C6_Flag varchar,
	C7_Restrictions_on_internal_movement varchar,
	C7_Flag varchar,
	C8_international_travel_controls varchar,
	E1_Income_support varchar,
	E1_Flag varchar,
	E2_Debt_contract_relief varchar,
	E3_Fiscal_measures varchar,
	E4_international_support varchar,
	H1_Public_information_campaigns varchar,
	H1_Flag varchar,
	H2_Testing_policy varchar,
	H3_Contact_tracing varchar,
	H4_Emergency_investment_in_healthcare varchar,
	H5_Investment_in_vaccines varchar,
	M1_Wildcard varchar,
	ConfirmedCases varchar,
	ConfirmedDeaths varchar,
	StringencyIndex varchar,
	StringencyIndexForDisplay varchar,
	StringencyLegacyIndex varchar,
	StringencyLegacyIndexForDisplay varchar,
	GovernmentResponseIndex varchar,
	GovernmentResponseIndexForDisplay varchar,
	ContainmentHealthIndex varchar,
	ContainmentHealthIndexForDisplay varchar,
	EconomicSupportIndex varchar,
	EconomicSupportIndexForDisplay varchar
);

/*
2. Alter datatype inside Govt_Response_Tracker
*/
ALTER TABLE govt_response_tracker
ALTER COLUMN DateC TYPE date USING dateC::date,
ALTER COLUMN C1_School_closing TYPE int USING c1_school_closing::integer,	
ALTER COLUMN C1_Flag TYPE SMALLINT USING c1_flag::smallint,
ALTER COLUMN C2_Workplace_closing TYPE int USING c2_workplace_closing::integer,
ALTER COLUMN C2_Flag TYPE SMALLINT USING c2_flag::smallint,
ALTER COLUMN C3_Cancel_public_events TYPE int USING c3_cancel_public_events::integer,
ALTER COLUMN C3_Flag TYPE SMALLINT USING c3_flag::smallint,
ALTER COLUMN C4_Restrictions_on_gatherings TYPE int USING c4_restrictions_on_gatherings::integer,
ALTER COLUMN C4_Flag TYPE SMALLINT USING c4_flag::smallint,
ALTER COLUMN C5_Close_public_transport TYPE int USING c5_close_public_transport::integer,
ALTER COLUMN C5_Flag TYPE SMALLINT USING c5_flag::smallint,
ALTER COLUMN C6_Stay_at_home_requirements TYPE int USING c6_stay_at_home_requirements::integer,
ALTER COLUMN C6_Flag TYPE SMALLINT USING c6_flag::smallint,
ALTER COLUMN c7_restrictions_on_internal_movement TYPE int USING c7_restrictions_on_internal_movement::integer,
ALTER COLUMN C7_Flag TYPE SMALLINT USING c7_flag::smallint,
ALTER COLUMN c8_international_travel_controls TYPE int USING c8_international_travel_controls::integer,
ALTER COLUMN E1_Income_support TYPE int USING e1_income_support::integer,
ALTER COLUMN E1_Flag TYPE SMALLINT USING e1_flag::smallint,
ALTER COLUMN E2_Debt_contract_relief TYPE int USING e2_debt_contract_relief::integer,
ALTER COLUMN E3_Fiscal_measures TYPE decimal USING e3_fiscal_measures::numeric,
ALTER COLUMN e4_international_support TYPE decimal USING e4_international_support::numeric,
ALTER COLUMN H1_Public_information_campaigns TYPE int USING h1_public_information_campaigns::integer,
ALTER COLUMN H1_Flag TYPE SMALLINT USING h1_flag::smallint,
ALTER COLUMN H2_Testing_policy TYPE int USING h2_testing_policy::integer,
ALTER COLUMN H3_Contact_tracing TYPE int USING h3_contact_tracing::integer,
ALTER COLUMN H4_Emergency_investment_in_healthcare TYPE decimal USING h4_emergency_investment_in_healthcare::numeric,
ALTER COLUMN H5_Investment_in_vaccines TYPE decimal USING h5_investment_in_vaccines::numeric,
ALTER COLUMN ConfirmedCases TYPE int USING ConfirmedCases::integer,
ALTER COLUMN ConfirmedDeaths TYPE int USING ConfirmedDeaths::integer,
ALTER COLUMN StringencyIndex TYPE decimal USING StringencyIndex::numeric,
ALTER COLUMN StringencyIndexForDisplay TYPE decimal USING StringencyIndexForDisplay::numeric,
ALTER COLUMN StringencyLegacyIndex TYPE decimal USING StringencyLegacyIndex::numeric,
ALTER COLUMN StringencyLegacyIndexForDisplay TYPE decimal USING StringencyLegacyIndexForDisplay::numeric,
ALTER COLUMN GovernmentResponseIndex TYPE decimal USING GovernmentResponseIndex::numeric,
ALTER COLUMN GovernmentResponseIndexForDisplay TYPE decimal USING GovernmentResponseIndexForDisplay::numeric,
ALTER COLUMN ContainmentHealthIndex TYPE decimal USING ContainmentHealthIndex::numeric,
ALTER COLUMN ContainmentHealthIndexForDisplay TYPE decimal USING ContainmentHealthIndexForDisplay::numeric,
ALTER COLUMN EconomicSupportIndex TYPE decimal USING EconomicSupportIndex::numeric,
ALTER COLUMN EconomicSupportIndexForDisplay TYPE decimal USING EconomicSupportIndexForDisplay::numeric;

/*
3. Populate the table using CSV file
*/
COPY govt_response_tracker FROM 'file/path/file_name.csv' DELIMITER ',' CSV HEADER;