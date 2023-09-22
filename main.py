# read in different

Reading Data
Relevant imports go here:

[134]
import pandas as pd
from IPython.display import display
Read in the different csv files

[135]
import pandas as pd

routes_df = pd.read_csv('data_output/routes.csv')
planes_df = pd.read_csv('data_output/planes.csv')
countries_df = pd.read_csv('data_output/countries.csv')
airports_df = pd.read_csv('data_output/airports.csv', on_bad_lines='skip')
airlines_df = pd.read_csv('data_output/airlines.csv', on_bad_lines='skip')
Inspect briefly the dataframes

[136]
# display(routes_df.head())
# display(planes_df.head())
# display(countries_df.head())
# display(airports_df.head())
# display(airlines_df.head())
Data Cleaning
Cleaning for All Dataframes
Upon inspecting the dataframes, we find a few fixes that need to be made before proceeding into the data analysis stage. These issues + their relevant fixes will be highlighted in this section.

All the dataframes have their values in the cells within the quotation marks. Here, we will get rid of the quotation marks using the replace function with regular expressions. So, for instance, the name of an airplane will go from "Aerospatiale (Nord) 262" to Aerospatiale (Nord) 262

[137]
routes_df = routes_df.replace('"', '', regex=True)
planes_df = planes_df.replace('"', '', regex=True)
countries_df = countries_df.replace('"', '', regex=True)
airports_df = airports_df.replace('"', '', regex=True)
airlines_df = airlines_df.replace('"', '', regex=True)
Cleaning for routes_df
We start by performing a general inspection of the routes_df dataframe.

[138]
display(routes_df.describe(include='all'))
display(routes_df.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 67663 entries, 0 to 67662
Data columns (total 9 columns):
 #   Column                  Non-Null Count  Dtype
---  ------                  --------------  -----
 0   Airline                 67663 non-null  object
 1   Airline ID              67663 non-null  object
 2   Source Airport          67663 non-null  object
 3   Source Airport ID       67663 non-null  object
 4   Destination Airport     67663 non-null  object
 5   Destination Airport ID  67663 non-null  object
 6   Codeshare               14597 non-null  object
 7   Stops                   67663 non-null  int64
 8   Equipment               67645 non-null  object
dtypes: int64(1), object(8)
memory usage: 4.6+ MB


None
display(routes_df.head())

Of the first items of interest, we find that the codeshare column is mainly a column that is filled with 'NaN' values. Further inspection upon the usefulness of the column indicates low relevance for the purpose of this analysis. The codeshare column will appear as "Y" if the particular flight is not operated by the airline but by another carrier. Therefore, we will first drop this column.

[139]
routes_df.drop(columns=['Codeshare'], inplace=True)
Next, we note that there are some rows in the equipment column that have null objects. Because the equipment column (which shows what types of aircrafts are mainly used for the routes) is an important one, we will omit all the rows that have null equipment values.

[140]
routes_df = routes_df.dropna(subset=['Equipment'])
Continuing the work on the 'equipment' column, we find that in some cases, the column has multiple equipment all listed in the same cell. For instance, take rows 64049 to 64055 as shown below.

[141]
routes_df.iloc[64049:64056]

As shown, some of the cells in the 'Equipment' column have more than one equipment/aircraft type listed within the cell. We would like to have a separate row for each of the equipment in order for appropriate analysis. Therefore, we need to separate a row which has the cell "73C 733 73W 73H" into four different rows so that every type of equipment has its own row. The rows would be:

Row 1 would have the 73C in the 'Equipment' column
Row 2 would have the 733 in the 'Equipment' column
Row 3 would have the 73W in the 'Equipment' column
Row 4 would have the 73H in the 'Equipment' column
Therefore, the last step in cleaning the routes_df would be to 'explode' these rows with multiple strings in the 'Equipment' column into different rows for each equipment.

[142]
routes_df['Equipment'] = routes_df['Equipment'].str.split()
routes_df = routes_df.explode('Equipment')
Cleaning for countries_df
We start by performing a general inspection of the countries_df dataframe.

[119]
display(countries_df.describe(include='all'))
display(countries_df.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 261 entries, 0 to 260
Data columns (total 4 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   name        261 non-null    object
 1   iso_code    261 non-null    object
 2   dafif_code  261 non-null    object
 3   Unnamed: 3  2 non-null      object
dtypes: object(4)
memory usage: 8.3+ KB


None
Whilst inspecting the countries_df, we found a few items of interest. First, we find that there are 261 rows in the countries dataframe, but only 259 are unique (as seen in the unique column). Let's inspect further.

[120]
duplicate_countries = countries_df[countries_df.duplicated(subset='name', keep=False)]
print(duplicate_countries)
          name iso_code dafif_code Unnamed: 3
33       India       IN         BS        NaN
101  Palestine       PS         GZ        NaN
112      India       IN         IN        NaN
252  Palestine       PS         WE        NaN

The reason for the duplicates is because the country 'India' and 'Palestine; has two different dafif_codes. Further research shows that the "DAFIF code" is not a standard or widely recognized code for countries. It's possible that "DAFIF" refers to a specific system or dataset that uses its own set of codes for countries or locations. DAFIF (Digital Aeronautical Flight Information File) codes are mainly used in the aviation and aeronautical navigation field and the information is not readily available. Seeing that the dafif_code is not as popular, and that the ISO code is more standard, this will guide us to focus on the ISO_codes from now. For the purpose of cleaning and avoiding duplicates, we will get rid of the first of the duplicates for each of the duplicated countries.

The reason for the duplicates is because the country 'India' has two different dafif_codes. The correct dafif_code for India is "IN". Therefore, we will drop the first of the two rows in india_rows (index = 33).

[121]
countries_df = countries_df.drop_duplicates(subset=['name'], keep='last')

We also note that the discrepancy in ISO_codes where, there are 241 unique ISO codes and 259 (now) unique countries. Referring back to the guide from the website that provides the dataset, we find the following "Some entries have DAFIF codes, but not ISO codes. These are primarily uninhabited islands without airports, and can be ignored for most purposes." Given that these locations do not have airports, they become useless for the purpose of our research. Therefore, we will omit all the rows where iso_code == '\N'.

[115]
countries_df = countries_df[countries_df['iso_code'] != '\\N']

Now that we have cleaned up the countries_df, we go back to obsolete nature of the dafif_code column and the "Unnamed: 3" column. The final step in making this dataframe analysis-ready is to drop the irrelevant columns. We drop the last two columns of the dataframe.

Some entries have DAFIF codes, but not ISO codes. These are primarily uninhabited islands without airports, and can be ignored for most purposes.

[122]
countries_df = countries_df.iloc[:, :-2]

# display(planes_df.describe(include='all'))
# display(planes_df.info())

# display(airports_df.describe(include='all'))
# display(airports_df.info())

# display(airlines_df.describe(include='all'))
# display(airlines_df.info())