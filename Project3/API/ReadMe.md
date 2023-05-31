# The Pursuit of Happiness API

Welcome to The Pursuit of Happiness API! This API provides various endpoints to retrieve data related to net migration and happiness factors of different countries. 

## Getting Started

To use the API, follow these steps:

1. Install the required dependencies using `pip install -r requirements.txt`.
2. Start the API server by running `python app.py`.
3. Access the API endpoints using the provided URLs.

## API Endpoints

### Net Migration API

The Net Migration API allows you to retrieve information related to net migration.

- **Endpoint:** `/migration/total/COUNTRY_NAME`
  - Replace `COUNTRY_NAME` with a country's name to get the total net migration from 2018 through 2022 for that country.

- **Endpoint:** `/migration/average/COUNTRY_NAME`
  - Replace `COUNTRY_NAME` with a country's name to get the average net migration from 2018 through 2022 for that country.

- **Endpoint:** `/migration/yearly_change/COUNTRY_NAME`
  - Replace `COUNTRY_NAME` with a country's name to get the yearly increase or decrease in net migration for that country.

- **Endpoint:** `/migration/top/YEAR`
  - Replace `YEAR` with a year from 2018 through 2022 to get the top 25 countries for that year.

- **Endpoint:** `/migration/bottom/YEAR`
  - Replace `YEAR` with a year from 2018 through 2022 to get the bottom 25 countries for that year.

- **Endpoint:** `/migration/percentage_increase?year_range=START_YEAR-END_YEAR`
  - Replace `START_YEAR` and `END_YEAR` with a range of years to get the top 25 countries with the highest percentage increase in net migration over that period.

### Happiness Factor API

The Happiness Factor API provides information on happiness factors of different countries.

- **Endpoint:** `/happiness_score/COUNTRY`
  - Replace `COUNTRY` with the name of a country to get the correlating happiness score for that country.

- **Endpoint:** `/country_factors/COUNTRY/FACTOR`
  - Replace `COUNTRY` with the name of a country and `FACTOR` with a valid factor to retrieve the corresponding factor value.
  - Valid factors are: `corruption`, `freedom_score`, `trade`, `business`, `government_spending`.

### Additional Links

- **Endpoint:** `/`
  - Visit the homepage of The Pursuit of Happiness API.
  - Provides links to the Net Migration API and Happiness Factor API.

- **Endpoint:** `/NetMigration`
  - Provides details and explanations on how to use the Net Migration API.
  - Includes links to different endpoints with their descriptions.

- **Endpoint:** `/HappinessFactor`
  - Provides details and explanations on how to use the Happiness Factor API.
  - Includes links to different endpoints with their descriptions.

## Contributing

Contributions to The Pursuit of Happiness API are welcome! If you find any issues or have suggestions for improvements, please feel free to create a pull request or open an issue in the GitHub repository.

## License

The Pursuit of Happiness API is open-source and released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as per the terms of the license.