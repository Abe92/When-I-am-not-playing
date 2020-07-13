import pandas as pd

# Pandas setting to display output messages maximum rows
pd.options.display.max_rows = 1500
pd.options.display.max_colwidth = 1500

# Load file; in this case a CSV file from Oxford Uni on DD/MM/YY
# Syntax: df = pd.read_csv('file/path/file_name.csv')
# Also, show file name in use
df = pd.read_csv('file/path/file_name.csv')
file_name = os.path.basename('file/path/file_name.csv')

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

# Counting NaNs inside the DataFrame
# Syntax: count=df.isna().sum()
#         print("NaNs count for this DataFrame is: " + str(count))
count = df.isna().sum()
# print("The DataFrame is using " + file_name)
# print("NaN counts for this DataFrame is:\n" + str(count))

# CountrySpecific: - Ethiopia
Ethiopia = df[(df.CountryName == 'Ethiopia') & ConfCases]
print([df[df.CountryName == 'Ethiopia'], ConfCases.where(df.CountryName == 'Ethiopia', inplace=True)])
