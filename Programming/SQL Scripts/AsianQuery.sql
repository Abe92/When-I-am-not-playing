/*
SQL Query to call all available Asian countries from 'govt_respond_tracker' table.
*/

SELECT * FROM govt_respond_tracker
WHERE countryname IN ('Afghanistan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei',
					 'Cambodia', 'China', 'Hong Kong', 'India', 'Indonesia', 'Iran',
					 'Iraq', 'Japan', 'Jordan', 'Kuwait', 'Kyrgyz Republic', 'Laos',
					 'Lebanon', 'Macao', 'Malaysia', 'Mongolia', 'Myanmar', 'Nepal',
					 'Oman', 'Pakistan', 'Philippines', 'Qatar', 'Saudi Arabia',
					 'Singapore', 'South Korea', 'Sri Lanka', 'Palestine', 'Syria',
					 'Taiwan', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkey', 
					 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam',
					 'Yemen')
ORDER BY 
countryname ASC,
datec ASC;