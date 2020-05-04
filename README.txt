#########################################################
THE OPTION 1 IS OPTIONAL. THIS IS INCLUDED TO CHECK THE WORKING OF PYTHON SCRIPTS IF WAMP SERVER IS UNAVAILABLE. IF YOU WANT TO RUN THE COMPLETE WEBSITE, YOU CAN GO DIRECTLY TO OPTION 2.
#########################################################

#########################################################
OPTION 1: To run only the python scripts,
#########################################################
1. Copy and paste the subfolder SalesForecast_Python (SalesForecastProject/SalesForecast_Python) to Desktop.

2. Open and execute the scripts Sales_forecast.py and Sales_forecast_predict.py using Spyder.

3. Check the SalesForecast_Python/images/visualize and SalesForecast_Python/images/predict folders to see the resulting .png images.

4. Check the results of predictions in SalesForecast_Python/results.txt file.

#########################################################
OPTION 2: To run the complete website, follow the steps below:
#########################################################

1. Download and install Wamp server 3.2

2. Copy and paste the SalesForecastProject folder in www folder in wamp. The path should look like C:\\wamp64\\www\\SalesForecastProject

3. Add python system path in line 107 of predictions.php and line 107 of visualize.php files.

4. Start the WAMP server.

5. Open the browser, type 127.0.0.1. The WAMP server homepage is displayed, indicating the server started successfully.

6. In the address bar, type 127.0.0.1/SalesForecastProject. This opens up the website. Click on different tabs to view functionality.