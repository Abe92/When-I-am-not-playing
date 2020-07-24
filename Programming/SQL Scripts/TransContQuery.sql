/*
SQL Query to call all available Transcontinental countries from 'govt_respond_tracker' table.
*/

SELECT * FROM govt_respond_tracker
WHERE countryname IN ('Azerbaijan',
		      'Cyprus',
		      'Georgia',
		      'Kazakhstan',
		      'Turkey')
ORDER BY 
countryname ASC,
datec ASC;
