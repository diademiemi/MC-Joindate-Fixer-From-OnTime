# Script to restore broken firstPlayed fields in player.dat using OnTime MariaDB table

This script is very niché but I am making it public regardless. Our player.dat files had an error and some players' firstPlayed date was wrong.  
This script uses the OnTime database which we still had keeping track of it too and takes the data from there into the player.dat files.  

### HOW TO USE

Run `pip install -r requirements.txt` before continuing.  
modify the .env file in this directory, change the the playerdata location and the MariaDB connection info, then run the script!  

### HOW IT WORKS

This script connects to MariaDB and reads the table from OnTime, it then reads every uuid and firstlogin from there.  
Then for every UUID it gets, it opens that associated .dat file and writes the firstlogin into the firstPlayed field.  