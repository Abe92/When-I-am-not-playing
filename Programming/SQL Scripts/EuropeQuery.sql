/*
SQL Query to call all available European countries from 'govt_respond_tracker' table.
*/

SELECT * FROM govt_respond_tracker
WHERE countryname IN ('Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium',
		      'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic',
		      'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece',
		      'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia',
		      'Lithuania', 'Luxembourg', 'Moldova', 'Netherlands', 'Norway',
		      'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia',
		      'Slovak Republic', 'Slovenia', 'Spain', 'Sweden', 'Switzerland',
		      'Ukraine', 'United Kingdom')
ORDER BY 
countryname ASC,
datec ASC;
