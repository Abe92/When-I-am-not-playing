'''
Author  : Aldy Rasyid Abe
Email   : aldyrabe@gmail.com
Title   : Python script visualization with Plotly Express
Purpose : Building visualization of Government COVID-19 Respond Tracker
'''

import psycopg2
import pandas as pd
import plotly.express as px

''' PostgreSQL Variables '''
PGHOST = 'localhost'  
PGDATABASE = 'your_database'
PGUSER = 'your_username' 
PGPASSWORD = 'your_password'

''' PostgreSQL Connection '''
conn_string = "host=" + PGHOST + " port=" + '5432' + " dbname=" + PGDATABASE + " user=" + PGUSER + " password=" \
              + PGPASSWORD
conn = psycopg2.connect(conn_string)
print("Connection is successfully established to " + PGDATABASE)

''' SQL Query '''
World_Query = pd.read_sql_query(
    '''
    SELECT
    *
    FROM govt_respond_tracker
    ORDER BY countryname, datec ASC
    ''', conn
)

African_Query = pd.read_sql_query(
    '''
    SELECT
    *
    FROM govt_respond_tracker
    WHERE countryname in ('african_countries')
    ORDER BY countryname ASC,
    datec ASC;
    ''', conn
)

Asian_Query = pd.read_sql_query(
    '''
    SELECT
    *
    FROM govt_respond_tracker
    WHERE countryname in ('asian_countries')
    ORDER BY countryname ASC,
    datec ASC;
    ''', conn
)

Americas_Query = pd.read_sql_query(
    '''
    SELECT
    *
    FROM govt_respond_tracker
    WHERE countryname in ('americas_countries')
    ORDER BY countryname, datec ASC
    ''', conn
)

Europe_Query = pd.read_sql_query(
    '''
    SELECT
    *
    FROM govt_respond_tracker
    WHERE countryname in ('european_countries')
    ORDER BY countryname, datec ASC
    ''', conn
)

Transcontinental_Query = pd.read_sql_query(
    '''
    SELECT
    *
    FROM govt_respond_tracker
    WHERE countryname in ('transcontinental_countries')
    ORDER BY countryname, datec ASC
    ''', conn
)

RestOfWorld_Query = pd.read_sql_query(
    '''
    SELECT
    *
    FROM govt_respond_tracker
    WHERE countryname in ('rest_of_world')
    ORDER BY countryname, datec ASC
    ''', conn
)

''' Load SQL Queries into Pandas DataFrame '''
World = pd.DataFrame(World_Query,
                     columns=
                     [
                         'countryname',
                         'countrycode',
                         'datec',
                         'c1_school_closing',
                         'c1_flag',
                         'c2_workspace_closing',
                         'c2_flag',
                         'c3_cancel_public_events',
                         'c3_flag',
                         'c4_restrictions_on_gatherings',
                         'c4_flag',
                         'c5_close_public_transport',
                         'c5_flag',
                         'c6_stay_at_home_requirements',
                         'c6_flag',
                         'c7_restrictions_on_internal_movement',
                         'c7_flag',
                         'c8_international_travel_controls',
                         'e1_income_support',
                         'e1_flag',
                         'e2_debt_contract_relief',
                         'e3_fiscal_measures',
                         'e4_international_support',
                         'h1_public_information_campaigns',
                         'h1_flag',
                         'h2_testing_policy',
                         'h3_contact_tracing',
                         'h4_emergency_investment_in_healthcare',
                         'h5_investment_in_vaccines',
                         'confirmedcases',
                         'confirmeddeaths',
                         'stringencyindex',
                         'stringencyindexfordisplay',
                         'stringencylegacyindex',
                         'stringencylegacyindexfordisplay',
                         'governmentresponseindex',
                         'governmentresponsendexfordisplay',
                         'containmenthealthindex',
                         'containmenthealthindexfordisplay',
                         'economicsupportindex',
                         'economicsupportindexfordisplay'
                     ])

African = pd.DataFrame(African_Query,
                       columns=[
                           'countryname',
                           'countrycode',
                           'datec',
                           'c1_school_closing',
                           'c1_flag',
                           'c2_workspace_closing',
                           'c2_flag',
                           'c3_cancel_public_events',
                           'c3_flag',
                           'c4_restrictions_on_gatherings',
                           'c4_flag',
                           'c5_close_public_transport',
                           'c5_flag',
                           'c6_stay_at_home_requirements',
                           'c6_flag',
                           'c7_restrictions_on_internal_movement',
                           'c7_flag',
                           'c8_international_travel_controls',
                           'e1_income_support',
                           'e1_flag',
                           'e2_debt_contract_relief',
                           'e3_fiscal_measures',
                           'e4_international_support',
                           'h1_public_information_campaigns',
                           'h1_flag',
                           'h2_testing_policy',
                           'h3_contact_tracing',
                           'h4_emergency_investment_in_healthcare',
                           'h5_investment_in_vaccines',
                           'confirmedcases',
                           'confirmeddeaths',
                           'stringencyindex',
                           'stringencyindexfordisplay',
                           'stringencylegacyindex',
                           'stringencylegacyindexfordisplay',
                           'governmentresponseindex',
                           'governmentresponsendexfordisplay',
                           'containmenthealthindex',
                           'containmenthealthindexfordisplay',
                           'economicsupportindex',
                           'economicsupportindexfordisplay'
                       ])

Asian = pd.DataFrame(Asian_Query,
                     columns=[
                         'countryname',
                         'countrycode',
                         'datec',
                         'c1_school_closing',
                         'c1_flag',
                         'c2_workspace_closing',
                         'c2_flag',
                         'c3_cancel_public_events',
                         'c3_flag',
                         'c4_restrictions_on_gatherings',
                         'c4_flag',
                         'c5_close_public_transport',
                         'c5_flag',
                         'c6_stay_at_home_requirements',
                         'c6_flag',
                         'c7_restrictions_on_internal_movement',
                         'c7_flag',
                         'c8_international_travel_controls',
                         'e1_income_support',
                         'e1_flag',
                         'e2_debt_contract_relief',
                         'e3_fiscal_measures',
                         'e4_international_support',
                         'h1_public_information_campaigns',
                         'h1_flag',
                         'h2_testing_policy',
                         'h3_contact_tracing',
                         'h4_emergency_investment_in_healthcare',
                         'h5_investment_in_vaccines',
                         'confirmedcases',
                         'confirmeddeaths',
                         'stringencyindex',
                         'stringencyindexfordisplay',
                         'stringencylegacyindex',
                         'stringencylegacyindexfordisplay',
                         'governmentresponseindex',
                         'governmentresponsendexfordisplay',
                         'containmenthealthindex',
                         'containmenthealthindexfordisplay',
                         'economicsupportindex',
                         'economicsupportindexfordisplay'
                     ])

Americas = pd.DataFrame(Americas_Query,
                        columns=[
                            'countryname',
                            'countrycode',
                            'datec',
                            'c1_school_closing',
                            'c1_flag',
                            'c2_workspace_closing',
                            'c2_flag',
                            'c3_cancel_public_events',
                            'c3_flag',
                            'c4_restrictions_on_gatherings',
                            'c4_flag',
                            'c5_close_public_transport',
                            'c5_flag',
                            'c6_stay_at_home_requirements',
                            'c6_flag',
                            'c7_restrictions_on_internal_movement',
                            'c7_flag',
                            'c8_international_travel_controls',
                            'e1_income_support',
                            'e1_flag',
                            'e2_debt_contract_relief',
                            'e3_fiscal_measures',
                            'e4_international_support',
                            'h1_public_information_campaigns',
                            'h1_flag',
                            'h2_testing_policy',
                            'h3_contact_tracing',
                            'h4_emergency_investment_in_healthcare',
                            'h5_investment_in_vaccines',
                            'confirmedcases',
                            'confirmeddeaths',
                            'stringencyindex',
                            'stringencyindexfordisplay',
                            'stringencylegacyindex',
                            'stringencylegacyindexfordisplay',
                            'governmentresponseindex',
                            'governmentresponsendexfordisplay',
                            'containmenthealthindex',
                            'containmenthealthindexfordisplay',
                            'economicsupportindex',
                            'economicsupportindexfordisplay'
                        ])

Europe = pd.DataFrame(Europe_Query,
                      columns=[
                          'countryname',
                          'countrycode',
                          'datec',
                          'c1_school_closing',
                          'c1_flag',
                          'c2_workspace_closing',
                          'c2_flag',
                          'c3_cancel_public_events',
                          'c3_flag',
                          'c4_restrictions_on_gatherings',
                          'c4_flag',
                          'c5_close_public_transport',
                          'c5_flag',
                          'c6_stay_at_home_requirements',
                          'c6_flag',
                          'c7_restrictions_on_internal_movement',
                          'c7_flag',
                          'c8_international_travel_controls',
                          'e1_income_support',
                          'e1_flag',
                          'e2_debt_contract_relief',
                          'e3_fiscal_measures',
                          'e4_international_support',
                          'h1_public_information_campaigns',
                          'h1_flag',
                          'h2_testing_policy',
                          'h3_contact_tracing',
                          'h4_emergency_investment_in_healthcare',
                          'h5_investment_in_vaccines',
                          'confirmedcases',
                          'confirmeddeaths',
                          'stringencyindex',
                          'stringencyindexfordisplay',
                          'stringencylegacyindex',
                          'stringencylegacyindexfordisplay',
                          'governmentresponseindex',
                          'governmentresponsendexfordisplay',
                          'containmenthealthindex',
                          'containmenthealthindexfordisplay',
                          'economicsupportindex',
                          'economicsupportindexfordisplay'
                      ])

Transcontinental = pd.DataFrame(Transcontinental_Query,
                                columns=[
                                    'countryname',
                                    'countrycode',
                                    'datec',
                                    'c1_school_closing',
                                    'c1_flag',
                                    'c2_workspace_closing',
                                    'c2_flag',
                                    'c3_cancel_public_events',
                                    'c3_flag',
                                    'c4_restrictions_on_gatherings',
                                    'c4_flag',
                                    'c5_close_public_transport',
                                    'c5_flag',
                                    'c6_stay_at_home_requirements',
                                    'c6_flag',
                                    'c7_restrictions_on_internal_movement',
                                    'c7_flag',
                                    'c8_international_travel_controls',
                                    'e1_income_support',
                                    'e1_flag',
                                    'e2_debt_contract_relief',
                                    'e3_fiscal_measures',
                                    'e4_international_support',
                                    'h1_public_information_campaigns',
                                    'h1_flag',
                                    'h2_testing_policy',
                                    'h3_contact_tracing',
                                    'h4_emergency_investment_in_healthcare',
                                    'h5_investment_in_vaccines',
                                    'confirmedcases',
                                    'confirmeddeaths',
                                    'stringencyindex',
                                    'stringencyindexfordisplay',
                                    'stringencylegacyindex',
                                    'stringencylegacyindexfordisplay',
                                    'governmentresponseindex',
                                    'governmentresponsendexfordisplay',
                                    'containmenthealthindex',
                                    'containmenthealthindexfordisplay',
                                    'economicsupportindex',
                                    'economicsupportindexfordisplay'
                                ])

RestOfWorld = pd.DataFrame(RestOfWorld_Query,
                           columns=[
                               'countryname',
                               'countrycode',
                               'datec',
                               'c1_school_closing',
                               'c1_flag',
                               'c2_workspace_closing',
                               'c2_flag',
                               'c3_cancel_public_events',
                               'c3_flag',
                               'c4_restrictions_on_gatherings',
                               'c4_flag',
                               'c5_close_public_transport',
                               'c5_flag',
                               'c6_stay_at_home_requirements',
                               'c6_flag',
                               'c7_restrictions_on_internal_movement',
                               'c7_flag',
                               'c8_international_travel_controls',
                               'e1_income_support',
                               'e1_flag',
                               'e2_debt_contract_relief',
                               'e3_fiscal_measures',
                               'e4_international_support',
                               'h1_public_information_campaigns',
                               'h1_flag',
                               'h2_testing_policy',
                               'h3_contact_tracing',
                               'h4_emergency_investment_in_healthcare',
                               'h5_investment_in_vaccines',
                               'confirmedcases',
                               'confirmeddeaths',
                               'stringencyindex',
                               'stringencyindexfordisplay',
                               'stringencylegacyindex',
                               'stringencylegacyindexfordisplay',
                               'governmentresponseindex',
                               'governmentresponsendexfordisplay',
                               'containmenthealthindex',
                               'containmenthealthindexfordisplay',
                               'economicsupportindex',
                               'economicsupportindexfordisplay'
                           ])

''' Print the content of the Pandas DataFrame 
    Pick any variables from the Load SQL Queries section
'''
# print('variables')

''' Global Variable for Colours '''
# HTML/HEX code : '#4c5c73'
# RGB code      : rgb(76, 92, 115)
faux_black = [[0.0, '#4c5c73'], [0.1, '#5D6C81'], [0.2, '#6F7C8F'], [0.3, '#818C9D'], [0.4, '#939DAB'],
              [0.5, '#A5ADB9'], [0.6, '#B7BDC7'], [0.7, '#C9CED5'], [0.8, '#DBDEE3'], [0.9, '#EDEEF1'],
              [1.0, '#FFFFFF']]

''' Plotly graph '''
# Government Respond - School Closing
african_figure1 = px.choropleth(African,
                                locations='countrycode',
                                color='c1_school_closing',
                                color_continuous_scale=faux_black,
                                range_color=[0, 3],
                                hover_data={'c1_school_closing': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c1_school_closing': ''})

african_figure1.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title={'text': 'Government Response - School Closing'},
                              font_family="Raleway",
                              coloraxis_colorbar=dict(ticks='inside',
                                                      tickvals=[0, 1, 2, 3],
                                                      ticktext=["0. no measures",
                                                                "1. recommend <br> "
                                                                "closing",
                                                                "2. require closing <br> (only some levels)",
                                                                "3. require closing <br> "
                                                                "all levels"],
                                                      dtick=4),
                              annotations=[dict(
                                  x=0.55,
                                  y=0.02,
                                  xref='paper',
                                  yref='paper',
                                  text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker </sub> </a>',
                                  showarrow=False)])

# african_figure1.show()
# african_figure1.write_html('file/path/file_name.html')

# Government Respond - Workplace Closing
african_figure2 = px.choropleth(African,
                                locations='countrycode',
                                color='c2_workspace_closing',
                                color_continuous_scale=faux_black,
                                range_color=[0, 3],
                                hover_data={'c2_workspace_closing': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c2_workspace_closing': ''})

african_figure2.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              font_family="Raleway",
                              title={'text': 'Government Response - Workspace Closing'},
                              coloraxis_colorbar=dict(ticks='inside',
                                                      tickvals=[0, 1, 2, 3],
                                                      ticktext=["0. no measures",
                                                                "1. recommend closing",
                                                                "2. require closing <br> "
                                                                "(or work from home) <br> "
                                                                "for some sectors or <br>"
                                                                "categories of workers",
                                                                "3. require closing <br>"
                                                                "all levels"],
                                                      dtick=4),
                              annotations=[dict(
                                  x=0.55,
                                  y=0.02,
                                  xref='paper',
                                  yref='paper',
                                  text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker </sub> </a>',
                                  showarrow=False)])

# african_figure2.show()
# african_figure2.write_html('file/path/file_name.html')

# Government Respond - Cancel Public Events
african_figure3 = px.choropleth(African,
                                locations='countrycode',
                                color='c3_cancel_public_events',
                                color_continuous_scale=faux_black,
                                range_color=[0, 2],
                                hover_data={'c3_cancel_public_events': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c3_cancel_public_events': ''})

african_figure3.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              font_family="Raleway",
                              title={'text': 'Government Response - Cancel Public Events'},
                              coloraxis_colorbar=dict(ticks='inside',
                                                      tickvals=[0, 1, 2],
                                                      ticktext=["0. no measures",
                                                                "1. recommend <br> "
                                                                "cancelling",
                                                                "2. require <br> "
                                                                "cancelling"],
                                                      dtick=3),
                              annotations=[dict(
                                  x=0.55,
                                  y=0.02,
                                  xref='paper',
                                  yref='paper',
                                  text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker </sub> </a>',
                                  showarrow=False)])
# african_figure3.show()
# african_figure3.write_html('file/path/file_name.html')

# Government Respond - Restrictions on Gatherings
african_figure4 = px.choropleth(African,
                                locations='countrycode',
                                color='c4_restrictions_on_gatherings',
                                color_continuous_scale=faux_black,
                                range_color=[0, 4],
                                hover_data={'c4_restrictions_on_gatherings': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c4_restrictions_on_gatherings': ''})

african_figure4.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title={'text': 'Government Response - Restrictions on Gatherings'},
                              font_family="Raleway",
                              coloraxis_colorbar=dict(ticks='inside',
                                                      tickvals=[0, 1, 2, 3, 4],
                                                      ticktext=["0. no restrictions",
                                                                "1. restrictions on <br> "
                                                                "very large gatherings <br>"
                                                                "(limit > 1000 people)",
                                                                "2. restrictions on gatherings <br> "
                                                                "between 101 - 1000 people",
                                                                "3. restrictions on gatherings <br> "
                                                                "between 11 - 100 people",
                                                                "4. restrictions on gatherings <br> "
                                                                "of 10 people or less"],
                                                      dtick=5),
                              annotations=[dict(
                                  x=0.55,
                                  y=0.02,
                                  xref='paper',
                                  yref='paper',
                                  text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker </sub> </a>',
                                  showarrow=False)])

# african_figure4.show()
# african_figure4.write_html('file/path/file_name.html')

# Government Respond - Close Public Transport
african_figure5 = px.choropleth(African,
                                locations='countrycode',
                                color='c5_close_public_transport',
                                color_continuous_scale=faux_black,
                                range_color=[0, 2],
                                hover_data={'c5_close_public_transport': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c5_close_public_transport': ''})

african_figure5.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title={'text': 'Government Response - Close Public Transport'},
                              font_family="Raleway",
                              coloraxis_colorbar=dict(ticks='inside',
                                                      tickvals=[0, 1, 2],
                                                      ticktext=["0. no measures",
                                                                "1. recommended closing <br>"
                                                                "(or significantly reduce volume/ <br>"
                                                                "route/means of <br> "
                                                                "transport available)",
                                                                "2. require closing <br>"
                                                                "(or prohibit most citizens <br> "
                                                                "from using it)"],
                                                      dtick=3),
                              annotations=[dict(
                                  x=0.55,
                                  y=0.02,
                                  xref='paper',
                                  yref='paper',
                                  text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker </sub> </a>',
                                  showarrow=False)])

# african_figure5.show()
# african_figure5.write_html('file/path/file_name.html')

# Government Respond - Stay at Home Requirements
african_figure6 = px.choropleth(African,
                                locations='countrycode',
                                color='c6_stay_at_home_requirements',
                                color_continuous_scale=faux_black,
                                range_color=[0, 3],
                                hover_data={'c6_stay_at_home_requirements': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c6_stay_at_home_requirements': ''})

african_figure6.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title={'text': 'Government Response - Stay At Home Requirements'},
                              font_family="Raleway",
                              coloraxis_colorbar=dict(ticks='inside',
                                                      tickvals=[0, 1, 2, 3],
                                                      ticktext=["0. no measures",
                                                                "1. recommend not <br> "
                                                                "leaving house",
                                                                "2. require not leaving house <br>"
                                                                "with exception for: <br>"
                                                                "- daily exercise <br>"
                                                                "- grocery shopping and <br>"
                                                                "- 'essential' trips",
                                                                "3. require not leaving house <br>"
                                                                "with minimal exceptions <br>"
                                                                "- allowed to leave <br> "
                                                                "once a week or <br>"
                                                                "- only one person can leave "
                                                                "<br> at a time, etc)"],
                                                      dtick=4),
                              annotations=[dict(
                                  x=0.55,
                                  y=0.02,
                                  xref='paper',
                                  yref='paper',
                                  text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker </sub> </a>',
                                  showarrow=False)])

# african_figure6.show()
# african_figure6.write_html('file/path/file_name.html')

# Government Respond - Restrictions on Internal Movement
african_figure7 = px.choropleth(African,
                                locations='countrycode',
                                color='c7_restrictions_on_internal_movement',
                                color_continuous_scale=faux_black,
                                range_color=[0, 2],
                                hover_data={'c7_restrictions_on_internal_movement': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c7_restrictions_on_internal_movement': ''})

african_figure7.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title={'text': 'Government Response - Internal Movement Restrictions'},
                              font_family="Raleway",
                              coloraxis_colorbar=dict(ticks='inside',
                                                      tickvals=[0, 1, 2],
                                                      ticktext=["0. no measures",
                                                                "1. recommend not to <br> "
                                                                "travel between <br> "
                                                                "regions/cities",
                                                                "2. internal movement <br> "
                                                                "restrictions in place"],
                                                      dtick=3),
                              annotations=[dict(
                                  x=0.55,
                                  y=0.02,
                                  xref='paper',
                                  yref='paper',
                                  text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker </sub> </a>',
                                  showarrow=False)])

# african_figure7.show()
# african_figure7.write_html('file/path/file_name.html')

# Government Respond - International Travel Controls
african_figure8 = px.choropleth(African,
                                locations='countrycode',
                                color='c8_international_travel_controls',
                                color_continuous_scale=faux_black,
                                range_color=[0, 4],
                                hover_data={'c8_international_travel_controls': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c8_international_travel_controls': ''})

african_figure8.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title={'text': 'Government Response - International Travel Controls'},
                              font_family="Raleway",
                              coloraxis_colorbar=dict(ticks='inside',
                                                      tickvals=[0, 1, 2, 3, 4],
                                                      ticktext=["0. no restrictions",
                                                                "1. screening arrivals",
                                                                "2. quarantine arrivals <br>"
                                                                "from some or all regions",
                                                                "3. ban arrivals <br> "
                                                                "from some regions",
                                                                "4. ban on all regions or <br>"
                                                                "total border closure"],
                                                      dtick=5),
                              annotations=[dict(
                                  x=0.55,
                                  y=0.02,
                                  xref='paper',
                                  yref='paper',
                                  text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker </sub> </a>',
                                  showarrow=False)])

# african_figure8.show()
# african_figure8.write_html('file/path/file_name.html')

# Government Respond - Income Support
african_figure9 = px.choropleth(African,
                                locations='countrycode',
                                color='e1_income_support',
                                color_continuous_scale=faux_black,
                                range_color=[0, 2],
                                hover_data={'e1_income_support': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'e1_income_support': ''})

african_figure9.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title={'text': 'Government Response - Income Support'},
                              font_family="Raleway",
                              coloraxis_colorbar=dict(ticks='inside',
                                                      tickvals=[0, 1, 2],
                                                      ticktext=["0. no income support",
                                                                "1. government is replacing <br>"
                                                                "less than 50% of lost salary <br>"
                                                                "(or if a flat sum, <br> "
                                                                "it is < 50% median salary)",
                                                                "2. government is replacing <br>"
                                                                "50% or more of lost salary <br>"
                                                                "(or if a flat sum, <br> "
                                                                "it is > 50% median salary)"],
                                                      dtick=3),
                              annotations=[dict(
                                  x=0.55,
                                  y=0.02,
                                  xref='paper',
                                  yref='paper',
                                  text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker </sub> </a>',
                                  showarrow=False)])

# african_figure9.show()
# african_figure9.write_html('file/path/file_name.html')

# Government Respond - Debt/Contract Relief
african_figure10 = px.choropleth(African,
                                 locations='countrycode',
                                 color='e2_debt_contract_relief',
                                 color_continuous_scale=faux_black,
                                 range_color=[0, 2],
                                 hover_data={'e2_debt_contract_relief': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'e2_debt_contract_relief': ''})

african_figure10.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title={'text': 'Government Response - Debt/Contract Relief'},
                               font_family="Raleway",
                               coloraxis_colorbar=dict(ticks='inside',
                                                       tickvals=[0, 1, 2],
                                                       ticktext=["0. no debt <br>"
                                                                 "or contract relief",
                                                                 "1. narrow relief, <br>"
                                                                 "specific to one <br> "
                                                                 "kind of contract",
                                                                 "2. broad debt/contract relief"],
                                                       dtick=3),
                               annotations=[dict(
                                   x=0.55,
                                   y=0.02,
                                   xref='paper',
                                   yref='paper',
                                   text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker </sub> </a>',
                                   showarrow=False)])

# african_figure10.show()
# african_figure10.write_html('file/path/file_name.html')

# Government Respond - Fiscal Measures
african_figure11 = px.choropleth(African,
                                 locations='countrycode',
                                 color='e3_fiscal_measures',
                                 color_continuous_scale=faux_black,
                                 hover_data={'e3_fiscal_measures': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'e3_fiscal_measures': 'in US$'})

african_figure11.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title={'text': 'Government Response - Fiscal Measures'},
                               font_family="Raleway",
                               coloraxis_colorbar=dict(ticks='inside'),
                               annotations=[dict(
                                   x=0.55,
                                   y=0.02,
                                   xref='paper',
                                   yref='paper',
                                   text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker </sub> </a>',
                                   showarrow=False)])

# african_figure11.show()
# african_figure11.write_html('file/path/file_name.html')

# Government Respond - International Support
african_figure12 = px.choropleth(African,
                                 locations='countrycode',
                                 color='e4_international_support',
                                 color_continuous_scale=faux_black,
                                 hover_data={'e4_international_support': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'e4_international_support': 'in US$'})

african_figure12.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title={'text': 'Government Response - International Support'},
                               font_family="Raleway",
                               coloraxis_colorbar=dict(ticks='inside'),
                               annotations=[dict(
                                   x=0.55,
                                   y=0.02,
                                   xref='paper',
                                   yref='paper',
                                   text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker </sub> </a>',
                                   showarrow=False)])

# african_figure12.show()
# african_figure12.write_html('file/path/file_name.html')

# Government Respond - Public Information Campaigns
african_figure13 = px.choropleth(African,
                                 locations='countrycode',
                                 color='h1_public_information_campaigns',
                                 color_continuous_scale=faux_black,
                                 range_color=[0, 2],
                                 hover_data={'h1_public_information_campaigns': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'h1_public_information_campaigns': ''})

african_figure13.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title={'text': 'Government Response - Public Information Campaign'},
                               font_family="Raleway",
                               coloraxis_colorbar=dict(ticks='inside',
                                                       tickvals=[0, 1, 2],
                                                       ticktext=["0. no COVID-19 public <br> "
                                                                 "information campaign",
                                                                 "1. public officials urging caution <br>"
                                                                 "about COVID-19",
                                                                 "2. coordinated public <br>"
                                                                 "information campaign <br>"
                                                                 "(e.g. across traditional <br> "
                                                                 "and social media)"],
                                                       dtick=3),
                               annotations=[dict(
                                   x=0.55,
                                   y=0.02,
                                   xref='paper',
                                   yref='paper',
                                   text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker </sub> </a>',
                                   showarrow=False)])

# african_figure13.show()
# african_figure13.write_html('file/path/file_name.html')

# Government Respond - Testing Policy
african_figure14 = px.choropleth(African,
                                 locations='countrycode',
                                 color='h2_testing_policy',
                                 color_continuous_scale=faux_black,
                                 range_color=[0, 3],
                                 hover_data={'h2_testing_policy': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'h2_testing_policy': ''})

african_figure14.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title={'text': 'Government Response - Testing Policy'},
                               font_family="Raleway",
                               coloraxis_colorbar=dict(ticks='inside',
                                                       tickvals=[0, 1, 2, 3],
                                                       ticktext=["0. no testing policy",
                                                                 "1. only those who both <br>"
                                                                 "(a) have symptoms AND <br>"
                                                                 "(b) meet specific criteria <br>"
                                                                 "(e.g. key workers, <br> "
                                                                 "admitted to hospital, <br> "
                                                                 "came into contact with <br>"
                                                                 "a known case, <br>"
                                                                 "returned from overseas)",
                                                                 "2. testing of anyone <br>"
                                                                 "showing COVID-19 symptoms",
                                                                 "3. open public testing <br>"
                                                                 "(e.g. 'drive through' testing <br> "
                                                                 "available to <br>"
                                                                 "asymptomatic people)"],
                                                       dtick=4),
                               annotations=[dict(
                                   x=0.30,
                                   y=0.02,
                                   xref='paper',
                                   yref='paper',
                                   text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker </sub> </a>',
                                   showarrow=False)])

# african_figure14.show()
# african_figure14.write_html('file/path/file_name.html')

# Government Respond - Contact Tracing
african_figure15 = px.choropleth(African,
                                 locations='countrycode',
                                 color='h3_contact_tracing',
                                 color_continuous_scale=faux_black,
                                 range_color=[0, 2],
                                 hover_data={'h3_contact_tracing': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'h3_contact_tracing': ''})

african_figure15.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title={'text': 'Government Response - Contact Tracing'},
                               font_family="Raleway",
                               coloraxis_colorbar=dict(ticks='inside',
                                                       tickvals=[0, 1, 2],
                                                       ticktext=["0. no contact tracing",
                                                                 "1. limited contact tracing; <br>"
                                                                 "not done for all cases",
                                                                 "2. comprehensive contact <br>"
                                                                 "tracing; done for <br> "
                                                                 "all identified cases"],
                                                       dtick=3),
                               annotations=[dict(
                                   x=0.55,
                                   y=0.02,
                                   xref='paper',
                                   yref='paper',
                                   text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker </sub> </a>',
                                   showarrow=False)])

# african_figure15.show()
# african_figure15.write_html('file/path/file_name.html')

# Government Respond - Emergency Investment in Healthcare
african_figure16 = px.choropleth(African,
                                 locations='countrycode',
                                 color='h4_emergency_investment_in_healthcare',
                                 color_continuous_scale=faux_black,
                                 hover_data={'h4_emergency_investment_in_healthcare': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'h4_emergency_investment_in_healthcare': 'in US$'})

african_figure16.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title={'text': 'Government Response - Emergency Investment in Healthcare'},
                               coloraxis_colorbar=dict(ticks='inside'),
                               font_family="Raleway",
                               annotations=[dict(
                                   x=0.55,
                                   y=0.02,
                                   xref='paper',
                                   yref='paper',
                                   text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker </sub> </a>',
                                   showarrow=False)])

# african_figure16.show()
# african_figure16.write_html('file/path/file_name.html')

# Government Respond - Investment in Vaccines
african_figure17 = px.choropleth(African,
                                 locations='countrycode',
                                 color='h5_investment_in_vaccines',
                                 color_continuous_scale=faux_black,
                                 hover_data={'h5_investment_in_vaccines': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'h5_investment_in_vaccines': 'in US$'})

african_figure17.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title={'text': 'Government Response - Investment in Vaccines'},
                               font_family="Raleway",
                               coloraxis_colorbar=dict(ticks='inside'),
                               annotations=[dict(
                                   x=0.55,
                                   y=0.02,
                                   xref='paper',
                                   yref='paper',
                                   text='<sub> Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker </sub> </a>',
                                   showarrow=False)])

# african_figure17.show()
# african_figure17.write_html('file/path/file_name.html')
