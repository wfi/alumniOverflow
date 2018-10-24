# alumniOverflow

# TODO:
  * Design Database [Christian, Kyle]
  * Fill out TODO

# SETUP
  * Install SQLite
  * To access database, in "database" directory, type the following:
    ```
    sqlite3 2468
    ```
    This will create a database file "2468" in the database directory

# DATABASE
  * Create/enter the database called "2468" by typing the following command
    ```
    sqlite3 2468
    ```
  * To test, for now, do the following:
    * From the "database" directory, enter "sqlite3 2468" database
    * Execute "\i createschema.sql" to create tables
      * Should display "CREATE TABLE" 8 times.
    * Try inserting and deleting various things in the database
    * When finished, remove all data and drop tables by executing "\i dropschema.sql"

  __NEXT STEPS:__
  * Create a test dataset
  * Make an automated test
  * Add tables which others see necessary
  * Identify keys and dependencies
  * Change how survey is stored--seems very cumbersome (maybe just make survey its own table, with key as email of survey taker?)

# HTML TEMPLATES
Currently a few skeleton templates for the html files which we will need to make
  * survey_q#.html
    * the #th page which a visitor will view while taking a survey (can also most likely be put in a single file, but needs JavaScript
  * editor.html
    * the page for an editor to edit and publish new questions
  * answer.html
    * the page for responders to answer questions
  * responses.html
    * the page for viewing responses
