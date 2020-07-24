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
# HTML/HEx code : '#4c5c73'
# RGB code      : rgb(76, 92, 115)
my_color_scale = [[0.0, '#4c5c73'], [0.1, '#5D6C81'], [0.2, '#6F7C8F'], [0.3, '#818C9D'], [0.4, '#939DAB'],
                  [0.5, '#A5ADB9'], [0.6, '#B7BDC7'], [0.7, '#C9CED5'], [0.8, '#DBDEE3'], [0.9, '#EDEEF1'],
                  [1.0, '#FFFFFF']]

''' Plotly graph '''
# Government Respond - School Closing
african_figure1 = px.choropleth(African,
                                locations='countrycode',
                                color='c1_school_closing',
                                color_continuous_scale=my_color_scale,
                                range_color=[0, 3],
                                hover_data={'c1_school_closing': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c1_school_closing': 'SCALE'})

african_figure1.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title_text='Government Respond - SCHOOL CLOSING <br> '
                                         'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                         '/coronavirus-government-response-tracker#data"> Oxford University '
                                         'CORONAVIRUS '
                                         'Government Respond Tracker</a>')

# african_figure1.show()
# african_figure1.write_html('file/path/filename.html')

asian_figure1 = px.choropleth(Asian,
                              locations='countrycode',
                              color='c1_school_closing',
                              color_continuous_scale=my_color_scale,
                              range_color=[0, 3],
                              hover_data={'c1_school_closing': False,
                                          'countrycode': False,
                                          'countryname': False},
                              hover_name='countryname',
                              labels={'c1_school_closing': 'SCALE'})

asian_figure1.update_layout(geo_scope='asia',
                            coloraxis_reversescale=True,
                            title_text='Government Respond - SCHOOL CLOSING <br> '
                                       'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker</a>')

# asian_figure1.show()
# asian_figure1.write_html('file/path/filename.html')

# Government Respond - Workplace Closing
african_figure2 = px.choropleth(African,
                                locations='countrycode',
                                color='c2_workspace_closing',
                                color_continuous_scale=my_color_scale,
                                range_color=[0, 3],
                                hover_data={'c2_workspace_closing': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c2_workspace_closing': 'SCALE'})

african_figure2.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title_text='Government Respond - WORKSPACE CLOSING <br> '
                                         'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                         '/coronavirus-government-response-tracker#data"> Oxford University '
                                         'CORONAVIRUS '
                                         'Government Respond Tracker</a>')

# african_figure2.show()
# african_figure2.write_html('file/path/file_name.html')

asian_figure2 = px.choropleth(Asian,
                              locations='countrycode',
                              color='c2_workspace_closing',
                              color_continuous_scale=my_color_scale,
                              range_color=[0, 3],
                              hover_data={'c2_workspace_closing': False,
                                          'countrycode': False,
                                          'countryname': False},
                              hover_name='countryname',
                              labels={'c2_workspace_closing': 'SCALE'})

asian_figure2.update_layout(geo_scope='asia',
                            coloraxis_reversescale=True,
                            title_text='Government Respond - WORKSPACE CLOSING <br> '
                                       'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker</a>')

# asian_figure2.show()
# asian_figure2.write_html('file/path/file_name.html')

# Government Respond - Cancel Public Events
african_figure3 = px.choropleth(African,
                                locations='countrycode',
                                color='c3_cancel_public_events',
                                color_continuous_scale=my_color_scale,
                                range_color=[0, 2],
                                hover_data={'c3_cancel_public_events': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c3_cancel_public_events': 'SCALE'})

african_figure3.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title_text='Government Respond - PUBLIC EVENT CANCELLED <br> '
                                         'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                         '/coronavirus-government-response-tracker#data"> Oxford University '
                                         'CORONAVIRUS '
                                         'Government Respond Tracker</a>')

# african_figure3.show()
# african_figure3.write_html('file/path/file_name.html')

asian_figure3 = px.choropleth(Asian,
                              locations='countrycode',
                              color='c3_cancel_public_events',
                              color_continuous_scale=my_color_scale,
                              range_color=[0, 2],
                              hover_data={'c3_cancel_public_events': False,
                                          'countrycode': False,
                                          'countryname': False},
                              hover_name='countryname',
                              labels={'c3_cancel_public_events': 'SCALE'})

asian_figure3.update_layout(geo_scope='asia',
                            coloraxis_reversescale=True,
                            title_text='Government Respond - PUBLIC EVENT CANCELLED <br> '
                                       'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker</a>')

# asian_figure3.show()
# asian_figure3.write_html('file/path/file_name.html')

# Government Respond - Restrictions on Gatherings
african_figure4 = px.choropleth(African,
                                locations='countrycode',
                                color='c4_restrictions_on_gatherings',
                                color_continuous_scale=my_color_scale,
                                range_color=[0, 4],
                                hover_data={'c4_restrictions_on_gatherings': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c4_restrictions_on_gatherings': 'SCALE'})

african_figure4.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title_text='Government Respond - RESTRICTIONS ON GATHERINGS <br> '
                                         'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                         '/coronavirus-government-response-tracker#data"> Oxford University '
                                         'CORONAVIRUS '
                                         'Government Respond Tracker</a>')

# african_figure4.show()
# african_figure4.write_html('file/path/file_name.html')

asian_figure4 = px.choropleth(Asian,
                              locations='countrycode',
                              color='c4_restrictions_on_gatherings',
                              color_continuous_scale=my_color_scale,
                              range_color=[0, 4],
                              hover_data={'c4_restrictions_on_gatherings': False,
                                          'countrycode': False,
                                          'countryname': False},
                              hover_name='countryname',
                              labels={'c4_restrictions_on_gatherings': 'SCALE'})

asian_figure4.update_layout(geo_scope='asia',
                            coloraxis_reversescale=True,
                            title_text='Government Respond - RESTRICTIONS ON GATHERINGS <br> '
                                       'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker</a>')

# asian_figure4.show()
# asian_figure4.write_html('file/path/file_name.html')

# Government Respond - Close Public Transport
african_figure5 = px.choropleth(African,
                                locations='countrycode',
                                color='c5_close_public_transport',
                                color_continuous_scale=my_color_scale,
                                range_color=[0, 2],
                                hover_data={'c5_close_public_transport': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c5_close_public_transport': 'SCALE'})

african_figure5.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title_text='Government Respond - Close Public Transport <br> '
                                         'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                         '/coronavirus-government-response-tracker#data"> Oxford University '
                                         'CORONAVIRUS '
                                         'Government Respond Tracker</a>')

# african_figure5.show()
# african_figure5.write_html('file/path/file_name.html')

asian_figure5 = px.choropleth(Asian,
                              locations='countrycode',
                              color='c5_close_public_transport',
                              color_continuous_scale=my_color_scale,
                              range_color=[0, 2],
                              hover_data={'c5_close_public_transport': False,
                                          'countrycode': False,
                                          'countryname': False},
                              hover_name='countryname',
                              labels={'c5_close_public_transport': 'SCALE'})

asian_figure5.update_layout(geo_scope='asia',
                            coloraxis_reversescale=True,
                            title_text='Government Respond - Close Public Transport <br> '
                                       'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker</a>')

# asian_figure5.show()
# asian_figure5.write_html('file/path/file_name.html')

# Government Respond - Stay at Home Requirements
african_figure6 = px.choropleth(African,
                                locations='countrycode',
                                color='c6_stay_at_home_requirements',
                                color_continuous_scale=my_color_scale,
                                range_color=[0, 3],
                                hover_data={'c6_stay_at_home_requirements': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c6_stay_at_home_requirements': 'SCALE'})

african_figure6.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title_text='Government Respond - Stay at Home Requirements <br> '
                                         'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                         '/coronavirus-government-response-tracker#data"> Oxford University '
                                         'CORONAVIRUS '
                                         'Government Respond Tracker</a>')

# african_figure6.show()
# african_figure6.write_html('file/path/file_name.html')

asian_figure6 = px.choropleth(Asian,
                              locations='countrycode',
                              color='c6_stay_at_home_requirements',
                              color_continuous_scale=my_color_scale,
                              range_color=[0, 3],
                              hover_data={'c6_stay_at_home_requirements': False,
                                          'countrycode': False,
                                          'countryname': False},
                              hover_name='countryname',
                              labels={'c6_stay_at_home_requirements': 'SCALE'})

asian_figure6.update_layout(geo_scope='asia',
                            coloraxis_reversescale=True,
                            title_text='Government Respond - Stay at Home Requirements <br> '
                                       'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker</a>')

# asian_figure6.show()
# asian_figure6.write_html('file/path/file_name.html')

# Government Respond - Restrictions on Internal Movement
african_figure7 = px.choropleth(African,
                                locations='countrycode',
                                color='c7_restrictions_on_internal_movement',
                                color_continuous_scale=my_color_scale,
                                range_color=[0, 2],
                                hover_data={'c7_restrictions_on_internal_movement': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c7_restrictions_on_internal_movement': 'SCALE'})

african_figure7.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title_text='Government Respond - Internal Movement Restrictions <br> '
                                         'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                         '/coronavirus-government-response-tracker#data"> Oxford University '
                                         'CORONAVIRUS '
                                         'Government Respond Tracker</a>')

# african_figure7.show()
# african_figure7.write_html('file/path/file_name.html')

asian_figure7 = px.choropleth(Asian,
                              locations='countrycode',
                              color='c7_restrictions_on_internal_movement',
                              color_continuous_scale=my_color_scale,
                              range_color=[0, 2],
                              hover_data={'c7_restrictions_on_internal_movement': False,
                                          'countrycode': False,
                                          'countryname': False},
                              hover_name='countryname',
                              labels={'c7_restrictions_on_internal_movement': 'SCALE'})

asian_figure7.update_layout(geo_scope='asia',
                            coloraxis_reversescale=True,
                            title_text='Government Respond - Internal Movement Restrictions <br> '
                                       'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker</a>')

# asian_figure7.show()
# asian_figure7.write_html('file/path/file_name.html')

# Government Respond - International Travel Controls
african_figure8 = px.choropleth(African,
                                locations='countrycode',
                                color='c8_international_travel_controls',
                                color_continuous_scale=my_color_scale,
                                range_color=[0, 4],
                                hover_data={'c8_international_travel_controls': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'c8_international_travel_controls': 'SCALE'})

african_figure8.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title_text='Government Respond - International Travel Controls <br> '
                                         'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                         '/coronavirus-government-response-tracker#data"> Oxford University '
                                         'CORONAVIRUS '
                                         'Government Respond Tracker</a>')

# african_figure8.show()
# african_figure8.write_html('file/path/file_name.html')

asian_figure8 = px.choropleth(Asian,
                              locations='countrycode',
                              color='c8_international_travel_controls',
                              color_continuous_scale=my_color_scale,
                              range_color=[0, 4],
                              hover_data={'c8_international_travel_controls': False,
                                          'countrycode': False,
                                          'countryname': False},
                              hover_name='countryname',
                              labels={'c8_international_travel_controls': 'SCALE'})

asian_figure8.update_layout(geo_scope='asia',
                            coloraxis_reversescale=True,
                            title_text='Government Respond - International Travel Controls <br> '
                                       'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker</a>')

# asian_figure8.show()
# asian_figure8.write_html('file/path/file_name.html')

# Government Respond - Income Support
african_figure9 = px.choropleth(African,
                                locations='countrycode',
                                color='e1_income_support',
                                color_continuous_scale=my_color_scale,
                                range_color=[0, 2],
                                hover_data={'e1_income_support': False,
                                            'countrycode': False,
                                            'countryname': False},
                                hover_name='countryname',
                                labels={'e1_income_support': 'SCALE'})

african_figure9.update_layout(geo_scope='africa',
                              coloraxis_reversescale=True,
                              title_text='Government Respond - Income Support <br> '
                                         'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                         '/coronavirus-government-response-tracker#data"> Oxford University '
                                         'CORONAVIRUS '
                                         'Government Respond Tracker</a>')

# african_figure9.show()
# african_figure9.write_html('file/path/file_name.html')

asian_figure9 = px.choropleth(Asian,
                              locations='countrycode',
                              color='e1_income_support',
                              color_continuous_scale=my_color_scale,
                              range_color=[0, 2],
                              hover_data={'e1_income_support': False,
                                          'countrycode': False,
                                          'countryname': False},
                              hover_name='countryname',
                              labels={'e1_income_support': 'SCALE'})

asian_figure9.update_layout(geo_scope='asia',
                            coloraxis_reversescale=True,
                            title_text='Government Respond - Income Support <br> '
                                       'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                       '/coronavirus-government-response-tracker#data"> Oxford University '
                                       'CORONAVIRUS '
                                       'Government Respond Tracker</a>')

# asian_figure9.show()
# asian_figure9.write_html('file/path/file_name.html')

# Government Respond - Debt/Contract Relief
african_figure10 = px.choropleth(African,
                                 locations='countrycode',
                                 color='e2_debt_contract_relief',
                                 color_continuous_scale=my_color_scale,
                                 range_color=[0, 2],
                                 hover_data={'e2_debt_contract_relief': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'e2_debt_contract_relief': 'SCALE'})

african_figure10.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title_text='Government Respond - Debt/Contract Relief <br> '
                                          'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                          '/coronavirus-government-response-tracker#data"> Oxford University '
                                          'CORONAVIRUS '
                                          'Government Respond Tracker</a>')

# african_figure10.show()
# african_figure10.write_html('file/path/file_name.html')

asian_figure10 = px.choropleth(Asian,
                               locations='countrycode',
                               color='e2_debt_contract_relief',
                               color_continuous_scale=my_color_scale,
                               range_color=[0, 2],
                               hover_data={'e2_debt_contract_relief': False,
                                           'countrycode': False,
                                           'countryname': False},
                               hover_name='countryname',
                               labels={'e2_debt_contract_relief': 'SCALE'})

asian_figure10.update_layout(geo_scope='asia',
                             coloraxis_reversescale=True,
                             title_text='Government Respond - Debt/Contract Relief <br> '
                                        'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker</a>')

# asian_figure10.show()
# asian_figure10.write_html('file/path/file_name.html')

# Government Respond - Fiscal Measures
african_figure11 = px.choropleth(African,
                                 locations='countrycode',
                                 color='e3_fiscal_measures',
                                 color_continuous_scale=my_color_scale,
                                 hover_data={'e3_fiscal_measures': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'e3_fiscal_measures': 'in US$'})

african_figure11.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title_text='Government Respond - Fiscal Measures <br> '
                                          'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                          '/coronavirus-government-response-tracker#data"> Oxford University '
                                          'CORONAVIRUS '
                                          'Government Respond Tracker</a>')

# african_figure11.show()
# african_figure11.write_html('file/path/file_name.html')

asian_figure11 = px.choropleth(Asian,
                               locations='countrycode',
                               color='e3_fiscal_measures',
                               color_continuous_scale=my_color_scale,
                               hover_data={'e3_fiscal_measures': False,
                                           'countrycode': False,
                                           'countryname': False},
                               hover_name='countryname',
                               labels={'e3_fiscal_measures': 'in US$'})

asian_figure11.update_layout(geo_scope='asia',
                             coloraxis_reversescale=True,
                             title_text='Government Respond - Fiscal Measures <br> '
                                        'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker</a>')

# asian_figure11.show()
# asian_figure11.write_html('file/path/file_name.html')

# Government Respond - International Support
african_figure12 = px.choropleth(African,
                                 locations='countrycode',
                                 color='e4_international_support',
                                 color_continuous_scale=my_color_scale,
                                 hover_data={'e4_international_support': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'e4_international_support': 'in US$'})

african_figure12.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title_text='Government Respond - International Support <br> '
                                          'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                          '/coronavirus-government-response-tracker#data"> Oxford University '
                                          'CORONAVIRUS '
                                          'Government Respond Tracker</a>')

# african_figure12.show()
# african_figure12.write_html('file/path/file_name.html')

asian_figure12 = px.choropleth(Asian,
                               locations='countrycode',
                               color='e4_international_support',
                               color_continuous_scale=my_color_scale,
                               hover_data={'e4_international_support': False,
                                           'countrycode': False,
                                           'countryname': False},
                               hover_name='countryname',
                               labels={'e4_international_support': 'in US$'})

asian_figure12.update_layout(geo_scope='asia',
                             coloraxis_reversescale=True,
                             title_text='Government Respond - International Support <br> '
                                        'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker</a>')

# asian_figure12.show()
# asian_figure12.write_html('file/path/file_name.html')

# Government Respond - Public Information Campaigns
african_figure13 = px.choropleth(African,
                                 locations='countrycode',
                                 color='h1_public_information_campaigns',
                                 color_continuous_scale=my_color_scale,
                                 range_color=[0, 2],
                                 hover_data={'h1_public_information_campaigns': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'h1_public_information_campaigns': 'SCALE'})

african_figure13.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title_text='Government Respond - Public Information Campaigns <br> '
                                          'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                          '/coronavirus-government-response-tracker#data"> Oxford University '
                                          'CORONAVIRUS '
                                          'Government Respond Tracker</a>')

# african_figure13.show()
# african_figure13.write_html('file/path/file_name.html')

asian_figure13 = px.choropleth(Asian,
                               locations='countrycode',
                               color='h1_public_information_campaigns',
                               color_continuous_scale=my_color_scale,
                               range_color=[0, 2],
                               hover_data={'h1_public_information_campaigns': False,
                                           'countrycode': False,
                                           'countryname': False},
                               hover_name='countryname',
                               labels={'h1_public_information_campaigns': 'SCALE'})

asian_figure13.update_layout(geo_scope='asia',
                             coloraxis_reversescale=True,
                             title_text='Government Respond - Public Information Campaigns <br> '
                                        'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker</a>')

# asian_figure13.show()
# asian_figure13.write_html('file/path/file_name.html')

# Government Respond - Testing Policy
african_figure14 = px.choropleth(African,
                                 locations='countrycode',
                                 color='h2_testing_policy',
                                 color_continuous_scale=my_color_scale,
                                 range_color=[0, 3],
                                 hover_data={'h2_testing_policy': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'h2_testing_policy': 'SCALE'})

african_figure14.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title_text='Government Respond - Testing Policy <br> '
                                          'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                          '/coronavirus-government-response-tracker#data"> Oxford University '
                                          'CORONAVIRUS '
                                          'Government Respond Tracker</a>')

# african_figure14.show()
# african_figure14.write_html('file/path/file_name.html')

asian_figure14 = px.choropleth(Asian,
                               locations='countrycode',
                               color='h2_testing_policy',
                               color_continuous_scale=my_color_scale,
                               range_color=[0, 3],
                               hover_data={'h2_testing_policy': False,
                                           'countrycode': False,
                                           'countryname': False},
                               hover_name='countryname',
                               labels={'h2_testing_policy': 'SCALE'})

asian_figure14.update_layout(geo_scope='asia',
                             coloraxis_reversescale=True,
                             title_text='Government Respond - Testing Policy <br> '
                                        'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker</a>')

# asian_figure14.show()
# asian_figure14.write_html('file/path/file_name.html')

# Government Respond - Contact Tracing
african_figure15 = px.choropleth(African,
                                 locations='countrycode',
                                 color='h3_contact_tracing',
                                 color_continuous_scale=my_color_scale,
                                 range_color=[0, 2],
                                 hover_data={'h3_contact_tracing': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'h3_contact_tracing': 'SCALE'})

african_figure15.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title_text='Government Respond - Contact Tracing <br> '
                                          'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                          '/coronavirus-government-response-tracker#data"> Oxford University '
                                          'CORONAVIRUS '
                                          'Government Respond Tracker</a>')

# african_figure15.show()
# african_figure15.write_html('file/path/file_name.html')

asian_figure15 = px.choropleth(Asian,
                               locations='countrycode',
                               color='h3_contact_tracing',
                               color_continuous_scale=my_color_scale,
                               range_color=[0, 2],
                               hover_data={'h3_contact_tracing': False,
                                           'countrycode': False,
                                           'countryname': False},
                               hover_name='countryname',
                               labels={'h3_contact_tracing': 'SCALE'})

asian_figure15.update_layout(geo_scope='asia',
                             coloraxis_reversescale=True,
                             title_text='Government Respond - Contact Tracing <br> '
                                        'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker</a>')

# asian_figure15.show()
# asian_figure15.write_html('file/path/file_name.html')

# Government Respond - Emergency Investment in Healthcare
african_figure16 = px.choropleth(African,
                                 locations='countrycode',
                                 color='h4_emergency_investment_in_healthcare',
                                 color_continuous_scale=my_color_scale,
                                 hover_data={'h4_emergency_investment_in_healthcare': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'h4_emergency_investment_in_healthcare': 'in US$'})

african_figure16.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title_text='Government Respond - Emergency Investment in Healthcare <br> '
                                          'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                          '/coronavirus-government-response-tracker#data"> Oxford University '
                                          'CORONAVIRUS '
                                          'Government Respond Tracker</a>')

# african_figure16.show()
# african_figure16.write_html('file/path/file_name.html')

asian_figure16 = px.choropleth(Asian,
                               locations='countrycode',
                               color='h4_emergency_investment_in_healthcare',
                               color_continuous_scale=my_color_scale,
                               hover_data={'h4_emergency_investment_in_healthcare': False,
                                           'countrycode': False,
                                           'countryname': False},
                               hover_name='countryname',
                               labels={'h4_emergency_investment_in_healthcare': 'in US$'})

asian_figure16.update_layout(geo_scope='asia',
                             coloraxis_reversescale=True,
                             title_text='Government Respond - Emergency Investment in Healthcare <br> '
                                        'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker</a>')

# asian_figure16.show()
# asian_figure16.write_html('file/path/file_name.html')

# Government Respond - Investment in Vaccines
african_figure17 = px.choropleth(African,
                                 locations='countrycode',
                                 color='h5_investment_in_vaccines',
                                 color_continuous_scale=my_color_scale,
                                 hover_data={'h5_investment_in_vaccines': False,
                                             'countrycode': False,
                                             'countryname': False},
                                 hover_name='countryname',
                                 labels={'h5_investment_in_vaccines': 'in US$'})

african_figure17.update_layout(geo_scope='africa',
                               coloraxis_reversescale=True,
                               title_text='Government Respond - Investment in Vaccines <br> '
                                          'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                          '/coronavirus-government-response-tracker#data"> Oxford University '
                                          'CORONAVIRUS '
                                          'Government Respond Tracker</a>')

# african_figure17.show()
# african_figure17.write_html('file/path/file_name.html')

asian_figure17 = px.choropleth(Asian,
                               locations='countrycode',
                               color='h5_investment_in_vaccines',
                               color_continuous_scale=my_color_scale,
                               hover_data={'h5_investment_in_vaccines': False,
                                           'countrycode': False,
                                           'countryname': False},
                               hover_name='countryname',
                               labels={'h5_investment_in_vaccines': 'in US$'})

asian_figure17.update_layout(geo_scope='asia',
                             coloraxis_reversescale=True,
                             title_text='Government Respond - Investment in Vaccines <br> '
                                        'Source: <a href="https://www.bsg.ox.ac.uk/research/research-projects'
                                        '/coronavirus-government-response-tracker#data"> Oxford University '
                                        'CORONAVIRUS '
                                        'Government Respond Tracker</a>')

# asian_figure17.show()
# asian_figure17.write_html('file/path/file_name.html')
