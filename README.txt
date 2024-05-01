To run file make sure to download the Capstone.py, logo.png, and the 4 .csv files titled; User1, User2, User3, User4
Open command prompt and CD to where the python file, png, and csv files are located.
You will need the latest python version installed and to run these commands prior to running the main file.

pip install pandas
pip install tk
pip install matplotlib

After this you can run the main code with

python Capstone.py

Current Login is hardcoded as 
USER: jhs0137
PASS: Pokemon12

To add more data please input the data in the formats listed below.
Date - ##/## ; ##/# ; #/## ; #/#
Time - ##:## ; ##:# ; #:## ; #:# - Needs to be in 24hr time format, for example instead of 6:23pm input 18:23
Activity - Sleep ; Awake

Currently our program only checks for empty cells and if the activity is "Sleep" or "Awake".
In future versions all 3 data entries will be changed to drop downs to make sure data cannot be input incorrectly.

Also please note that the graph shows the previous 7 days of data in relation to the current time on your computer. 
Current csv files may not display a graph due to data not being within the last 7 days. 
Please contact jacobhschwab12@gmail.com if you need an updated csv for testing purposes.
