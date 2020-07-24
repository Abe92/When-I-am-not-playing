/*
SQL Query to call all available African countries from 'govt_respond_tracker' table.
*/

SELECT * FROM govt_respond_tracker
WHERE countryname IN ('Algeria', 'Angola', 'Benin', 'Bostwana',
					 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde',
					 'Central African Republic', 'Chad', 'Congo', 'Cote d''Ivoire',
					 'Democratic Republic of the Congo', 'Djibouti', 'Egypt',
					 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia',
					 'Ghana', 'Guinea', 'Kenya', 'Lesotho', 'Liberia', 'Libya',
					 'Madagascar', 'Malawi', 'Mauritania', 'Mauritius', 'Morocco',
					 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Seychelles',
					 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan',
					 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia')
ORDER BY 
countryname ASC,
datec ASC;