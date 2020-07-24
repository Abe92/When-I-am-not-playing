/*
SQL Query to call all available Americas countries from 'govt_respond_tracker' table.
*/

SELECT * FROM govt_respond_tracker
WHERE countryname IN ('Argentina', 'Barbados', 'Belize', 'Bolivia', 'Brazil',
					 'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominica',
					 'Dominican Republic', 'Ecuador', 'El Salvador', 'Guatemala', 'Guyana',
					 'Haiti', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama',
					 'Paraguay', 'Peru', 'Suriname', 'Trinidad and Tobago', 'United States',
					 'Uruguay', 'Venezuela')
ORDER BY 
countryname ASC,
datec ASC;