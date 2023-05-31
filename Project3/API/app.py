from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# load the data once when server starts
df = pd.read_csv('net_migration.csv')

# convert columns from string to numeric if possible, ignore errors
for year in range(2018, 2023):
    df[str(year)] = pd.to_numeric(df[str(year)], errors='coerce')

@app.route("/" , methods=['GET'])
def welcome():
    return f"""
        <html>
            <head>
                <title> Net Migration API</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        font-size: 16px;
                        line-height: 1.5;
                    }}
                    
                    .route {{
                        margin: 10px 0;
                        padding: 10px;
                        background-color: #f0f0f0;
                        border-radius: 5px;
                    }}
                    
                    .route a {{
                        color: #333;
                        text-decoration: none;
                        font-weight: bold;
                    }}
                    
                    .route a:hover {{
                        text-decoration: underline;
                    }}
                </style>
            </head>
             <body>
                <h1>Welcome to the Migration API!</h1>
                <p>Here's a couple links you can utilize:</p>
                <p>
                <a href="http://127.0.0.1:8080/NetMigration">Visit The Net Migration API!</a>
                </p>
                <p>
                <a href="http://127.0.0.1:8080/HappinessFactor">Visit The Happiness Factor API!</a>
                </p>
               
"""
######################################################

# HTML for Net Migration

######################################################

@app.route("/NetMigration", methods=['GET'])
def welcome2():
    return f"""
        <html>
            <head>
                <title> Net Migration API</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        font-size: 16px;
                        line-height: 1.5;
                    }}
                    
                    .route {{
                        margin: 10px 0;
                        padding: 10px;
                        background-color: #f0f0f0;
                        border-radius: 5px;
                    }}
                    
                    .route a {{
                        color: #333;
                        text-decoration: none;
                        font-weight: bold;
                    }}
                    
                    .route a:hover {{
                        text-decoration: underline;
                    }}
                </style>
            </head>
            <body>
                <h1>Welcome to the Net Migration API!</h1>
                <p>Here's how you can use it:</p>
                <div class="route">
                    <a href="/migration/total/COUNTRY_NAME">/migration/total/COUNTRY_NAME</a>
                    <p>Replace COUNTRY_NAME with a country's name to get the total net migration from 2018 through 2022 for that country.</p>
                </div>
                <div class="route">
                    <a href="/migration/average/COUNTRY_NAME">/migration/average/COUNTRY_NAME</a>
                    <p>Replace COUNTRY_NAME with a country's name to get the average net migration from 2018 through 2022 for that country.</p>
                </div>
                <div class="route">
                    <a href="/migration/yearly_change/COUNTRY_NAME">/migration/yearly_change/COUNTRY_NAME</a>
                    <p>Replace COUNTRY_NAME with a country's name to get the yearly increase or decrease in net migration for that country.</p>
                </div>
                <div class="route">
                    <a href="/migration/top/YEAR">/migration/top/YEAR</a>
                    <p>Replace YEAR with a year from 2018 through 2022 to get the top 25 countries for that year.</p>
                </div>
                <div class="route">
                    <a href="/migration/bottom/YEAR">/migration/bottom/YEAR</a>
                    <p>Replace YEAR with a year from 2018 through 2022 to get the bottom 25 countries for that year.</p>
                </div>
                <div class="route">
                    <a href="/migration/percentage_increase?year_range=START_YEAR-END_YEAR">/migration/percentage_increase?year_range=START_YEAR-END_YEAR</a>
                    <p>Replace START_YEAR-END_YEAR with a range of years to get the top 25 countries with the highest percentage increase in net migration over that period.</p>
                </div>
            </body>
        </html>
    """

######################################################

# HTML for Happiness

######################################################

@app.route("/HappinessFactor", methods=['GET'])
def welcome3():
    return """
        <html>
            <head>
                <title>Happiness Factor API</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        font-size: 16px;
                        line-height: 1.5;
                    }
                    
                    .route {
                        margin: 10px 0;
                        padding: 10px;
                        background-color: #f0f0f0;
                        border-radius: 5px;
                    }
                    
                    .route a {
                        color: #333;
                        text-decoration: none;
                        font-weight: bold;
                    }
                    
                    .route a:hover {
                        text-decoration: underline;
                    }
                </style>
            </head>
            <body>
                <h1>Welcome to the Happiness Factor API!</h1>
                <p>Use this API to find information on Happiness Factor</p>
                <div class="route">
                    <a href="/happiness_score/Country">/happiness_score/Country</a>
                    <p>Replace Country with the Country you would like to see the correlating Happiness Score</p>
                </div>
                <div class="route">
                    <a href="/country_factors/Country/Factor">/country_factors/Country/Factor</a>
                    <p>Replace Country with the Country you would like to select, and a valid factor</p>
                    <p>Valid factors are "corruption', 'freedom_score', 'trade', 'business', 'government_spending"</p>
                </div>
                <div class="route">
                    <iframe src="/happinessfactor/pdf" width="100%" height="600px"></iframe>
                </div>
            </body>
        </html>
"""

######################################################
#        ROUTES
######################################################


@app.route('/migration/total/<country>', methods=['GET'])
def get_migration_total(country):
    data = df.loc[df['Country Name'] == country]
    if data.empty:
        return "Country not found", 404
    total = data.loc[:, '2018':'2022'].sum(axis=1).values[0]
    return jsonify({'country': country, 'total_migration': int(total)})

@app.route('/migration/top/<int:year>', methods=['GET'])
def get_top_countries(year):
    if year not in range(2018, 2023):
        return "Year not found", 404
    top_countries = df.nlargest(25, str(year))
    return jsonify(top_countries[['Country Name', str(year)]].to_dict('records'))

@app.route('/migration/bottom/<int:year>', methods=['GET'])
def get_bottom_countries(year):
    if year not in range(2018, 2023):
        return "Year not found", 404
    bottom_countries = df.nsmallest(25, str(year))
    return jsonify(bottom_countries[['Country Name', str(year)]].to_dict('records'))

@app.route('/migration/percentage_increase', methods=['GET'])
def get_top_percentage_increase():
    year_range = request.args.get('year_range', '').split('-')
    if len(year_range) != 2 or not all(year.isdigit() and int(year) in range(2018, 2023) for year in year_range):
        return "Invalid year range", 404
    start_year, end_year = map(int, year_range)
    df_temp = df.copy()
    df_temp['percentage_increase'] = (df_temp[str(end_year)] - df_temp[str(start_year)]) / df_temp[str(start_year)] * 100
    top_countries = df_temp.nlargest(15, 'percentage_increase')
    return jsonify(top_countries[['Country Name', 'percentage_increase']].to_dict('records'))

@app.route('/migration/average/<country>', methods=['GET'])
def get_average_migration(country):
    data = df.loc[df['Country Name'] == country]
    if data.empty:
        return "Country not found", 404
    average = data.loc[:, '2018':'2022'].mean(axis=1).values[0]
    return jsonify({'country': country, 'average_migration': int(average)})

@app.route('/migration/yearly_change/<country>', methods=['GET'])
def get_yearly_change(country):
    data = df.loc[df['Country Name'] == country]
    if data.empty:
        return "Country not found", 404
    yearly_change = data.loc[:, '2018':'2022'].diff(axis=1).drop(columns='2018').T.to_dict('records')[0]
    return jsonify({'country': country, 'yearly_change': yearly_change})

######################################################
######################################################
#             DF HAPPINESS
######################################################
######################################################

df_happiness = pd.read_csv('happiness_factors.csv')

@app.route("/happiness_score/<country>", methods=['GET'])
def get_happiness_score(country):
    data = df_happiness.loc[df_happiness['Country'] == country]
    if data.empty:
        return "Country not found", 404
    happiness_score = data['Happiness_Score'].values[0]
    return jsonify({'country': country, 'happiness_score': happiness_score})

@app.route("/country_factors/<country>/<factor>", methods=['GET'])
def get_country_factor(country, factor):
    valid_factors = ['corruption', 'freedom_score', 'trade', 'business', 'government_spending']
    if factor.lower() not in valid_factors:
        return "Invalid factor", 400
    factor_column = factor.replace('_', ' ').title()
    if factor_column not in df_happiness.columns:
        return "Factor not found", 404
    data = df_happiness.loc[df_happiness['Country'] == country]
    if data.empty:
        return "Country not found", 404
    factor_value = data[factor_column].values[0]
    return jsonify({'country': country, 'factor': factor_column, 'value': factor_value})


if __name__ == '__main__':
    app.run(port=8080)

