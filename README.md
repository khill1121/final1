# Florida Citrus Industry from 2002 to 2021
## Getting the Data
All of the data used in this project was based on the data in reports from the USDA's National Agricultural Statistics Service
Florida Field Office. Specifically, the citrus summary was used which can be found [here] (https://www.nass.usda.gov/Statistics_by_State/Florida/Publications/Citrus/Citrus_Summary/index.php).
## Organizing the Data
In order to make the charts that would go on each county's page, I made seperate CSV files for each county and uploaded them to a database. Because the data from the USDA was sorted by years and not by county, I had to enter all the data by hand for these CSV files. I entered three sets of data for 20 years for all 25 counties, meaning I manually entered 1500 cells.
![Database Example Image]<img width="808" alt="Screen Shot 2022-04-27 at 12 06 39 PM" src="https://user-images.githubusercontent.com/71909951/165562997-7243aac3-d035-450e-a157-157f636a6671.png">
The other data points were made into a seperate CSV sheet that was used to interact with the app and calculate the percentage change in the values from 2002 to 2021. That data sheet is included in this repo and is country.csv
## Making the Charts
I made the charts using plotly. I uploaded the CSVs I made to my database and then linked the database to plotly using Falcon SQL Client. From there making the charts was fairly simple and I was able to follow the instructions on plotly before downloading the charts as png files. I would have preferred SVG files for interactivity, but that was a pro subscription option only on plotly.
## Putting it together
Finally, I was able to start putting the app together with the information I included in country.csv and just kept slightly altering stylistic choices until I got with something that I think looks clean and professional on both desktop and mobile.
