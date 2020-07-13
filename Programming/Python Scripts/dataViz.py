import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load file; in this case a CSV file from Oxford Uni on DD/MM/YY
# Syntax: df = pd.read_csv('file/path/file_name.csv')
df = pd.read_csv('file/path/file_name.csv')

# List of the column names from flat file (CSV file)
# Begins with the countries name, its code and the date when information was collected
CountryName = df['CountryName']
CountryCode = df['CountryCode']
DateC = df['DateC']

# 'C' section
# = Containment and Closure Policies
c1_SchoolClosing = df['C1_School_closing']
c1_Flag = df['C1_Flag']
c2_WorkplaceClosing = df['C2_Workplace_closing']
c2_Flag = df['C2_Flag']
c3_CancelPubEvent = df['C3_Cancel public_events']
c3_Flag = df['C3_Flag']
c4_RestrictionOnGatherings = df['C4_Restrictions_on_gatherings']
c4_Flag = df['C4_Flag']
c5_ClosePubTransport = df['C5_Close_public_transport']
c5_Flag = df['C5_Flag']
c6_StayAtHome = df['C6_Stay_at_home_requirements']
c6_Flag = df['C6_Flag']
c7_RestrictionOnInternMove = df['C7_Restrictions_on_internal_movement']
c7_Flag = df['C7_Flag']
c8_InternationalTravelControl = df['C8_International_travel_controls']

# 'E' section
# = Economic Policies
e1_IncomeSupp = df['E1_Income_support']
e1_Flag = df['E1_Flag']
e2_DebtContractRelief = df['E2_Debt_contract_relief']
e3_FiscalMeasures = df['E3_Fiscal_measures']
e4_IntSupp = df['E4_International_support']

# 'H' section
# = Health System Policies
h1_PubInfoCampaigns = df['H1_Public_information_campaigns']
h1_Flag = df['H1_Flag']
h2_TestingPolicy = df['H2_Testing_policy']
h3_ContactTracing = df['H3_Contact_tracing']
h4_EmergencyInvestInHealth = df['H4_Emergency_investment_in_healthcare']
h5_InvestInVaccine = df['H5_Investment_in_vaccines']

# 'M' section
# = Miscellaneous Policies
m1_Wildcard = df['M1_Wildcard']

# Other:
# Other column used in the University of Oxford Government Respond Tracker
ConfCases = df['ConfirmedCases']
ConfDeaths = df['ConfirmedDeaths']
StringencyIndex = df['StringencyIndex']
StringencyIndexForDisplay = df['StringencyIndexForDisplay']
StringencyLegacyIndex = df['StringencyLegacyIndex']
StringencyLegacyIndexForDisplay = df['StringencyLegacyIndexForDisplay']
GovernmentResponseIndex = df['GovernmentResponseIndex']
GovernmentResponseIndexForDisplay = df['GovernmentResponseIndexForDisplay']
ContainmentHealthIndex = df['ContainmentHealthIndex']
ContainmentHealthIndexForDisplay = df['ContainmentHealthIndexForDisplay']
EconomicSuppIndex = df['EconomicSupportIndex']
EconomicSuppIndexForDisplay = df['EconomicSupportIndexForDisplay']

# Masking missing data - OPTIONAL
m_ConfCases = np.isfinite(ConfCases)  # NaN: 10412
m_ConfDeaths = np.isfinite(ConfDeaths)  # NaN: 10412

# Plot 1 - Country by Code and Confirmed Cases
# Syntax: plt.plot_name(x_axis, y_axis)
plt.bar(CountryCode, ConfCases / 10**6)
plt.xlabel('CountryCode')
plt.ylabel('ConfirmedCases \n (in Millions)')
plt.title('COVID-19 Confirmed Cases \n 01-01-2020 to 09-07-20')
plt.xticks(rotation=90)  # Rotate the value of X-axis points into 90 degree
plt.tick_params(axis='x', which='major', labelsize=6.15)  # Increase space between points on X-axis
plt.rc('grid', linestyle="-", color='lightblue')
plt.grid(True)
plt.show()

# Plot 2 - Country by Code and Confirmed Deaths
# Syntax: plt.plot_name(x_axis, y_axis)
plt.bar(CountryCode, ConfDeaths)
plt.xlabel('CountryCode')
plt.ylabel('ConfirmedDeaths \n (in Thousands)')
plt.title('COVID-19 Confirmed Deaths \n 01-01-2020 to 09-07-20')
plt.xticks(rotation=90)  # Rotate the value of X-axis points into 90 degree
plt.tick_params(axis='x', which='major', labelsize=6.15)  # Increase the size of points label on X-axis
plt.rc('grid', linestyle="-", color='lightblue')
plt.grid(True)
plt.show()

# Plot 3 - Date and Confirmed Cases
# Syntax: plt.plot_name(x_axis, y_axis)
f_DateC = DateC.apply(lambda x: pd.to_datetime(str(x), format='%Y %m %d'))  # parse the date format in DataFrame to
# 'datetime'
plt.bar(f_DateC, ConfCases / 10**6)
plt.xlabel('Dates \n (YYYY-MM)')
plt.ylabel('ConfirmedCases \n (in Millions)')
plt.title('COVID-19 Confirmed Cases \n 01-01-2020 to 09-07-20')
plt.xticks(rotation=45)  # Rotate the value of X-axis points into 45 degree
plt.tick_params(axis='x', which='major', labelsize=8)  # Increase the size of points label on X-axis
plt.rc('grid', linestyle="-", color='lightblue')
plt.grid(True)
plt.show()

# Plot 4 - Date and Confirmed Deaths
# Syntax: plt.plot_name(x_axis,y_axis)
plt.bar(f_DateC, ConfDeaths)
plt.xlabel('Dates \n (YYYY-MM)')
plt.ylabel('ConfirmedDeaths \n (in Thousands)')
plt.title('COVID-19 Confirmed Deaths \n 01-01-2020 to 09-07-20')
plt.xticks(rotation=45)  # Rotate the value of X-axis points into 45 degree
plt.tick_params(axis='x', which='major', labelsize=8)  # Increase the size of points label on X-axis
plt.rc('grid', linestyle="-", color="lightblue")
plt.grid(True)
plt.show()

# Plot 5 - Date and School Closing
# Syntax: plt.plot_name(x_axis, y_axis)
plt.bar(f_DateC, c1_SchoolClosing)
plt.xlabel('Dates \n (YYYY-MM)')
plt.ylabel('Containment and Closure Policies \n [School Closing]')
plt.title('COVID-19 Governments Respond \n School Closing \n 01-01-2020 to 09-07-2020')
plt.xticks(rotation=45)  # Rotate the value of X-axis points into 45 degree
plt.tick_params(axis='x', which='major', labelsize=8)  # Increase the size of points label on X-axis
plt.rc('grid', linestyle="-", color="lightblue")
plt.grid(True)
plt.show()
