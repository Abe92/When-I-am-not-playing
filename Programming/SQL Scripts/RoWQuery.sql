/*
SQL Query to call all available Rest of the World countries from 'govt_respond_tracker' table.
*/

SELECT * FROM govt_respond_tracker
WHERE countryname IN ('Aruba', 'Bermuda',
		      'Fiji', 'Gibraltar',
		      'Greenland', 'Guam',
		      'Papua New Guinea',
		      'Puerto Rico',
	              'Vanuatu')
ORDER BY 
countryname ASC,
datec ASC;
