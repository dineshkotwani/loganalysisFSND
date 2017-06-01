# Log Analysis FSND

Log Analysis is a project which answers the assignment questions for the log analysis project as part of FSND program.

# Steps to run the project

  - The project uses Views to run queries for calculating answers ,hence please run the views.sql file to create the Views in news db  by running below command:
    ```sh
    cd /vagrant/loganalysis
    psql -d news -f  views.sql
    ```
  - After the running the above command , you will see the views created as output of above command will be 3 times printed as CREATE VIEW.
  - Once the views have been created , go ahead and run the python script called as loganalysis.py to get the output . The python script writes the output to console and also writes it to file called as "output.txt".
  - Please open "output.txt" to verify the query answers.






  

