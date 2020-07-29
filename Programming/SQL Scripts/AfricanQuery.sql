/*
SQL Query to call all available African countries from 'govt_respond_tracker' table.
*/

SELECT * FROM govt_respond_tracker
WHERE countryname IN ('Algeria', 'Angola', 'Benin', 'Botswana',
		      'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde',
		      'Central African Republic', 'Chad', 'Congo', 'Cote d''Ivoire',
		      'Democratic Republic of Congo', 'Djibouti', 'Egypt',
		      'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia',
		      'Ghana', 'Guinea', 'Kenya', 'Lesotho', 'Liberia', 'Libya',
		      'Madagascar', 'Mali', 'Malawi', 'Mauritania', 'Mauritius', 'Morocco',
		      'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Seychelles',
		      'Sierra Leone', 'Senegal','Somalia', 'South Africa', 'South Sudan', 'Sudan',
		      'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe')
ORDER BY 
countryname ASC,
datec ASC;
