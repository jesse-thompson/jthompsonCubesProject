<h1>Jesse Thompson's CUBES Project</h1>

<h3>Instructions:</h3>

- secrets.template is to be used as a template for 
holding the API key in a file "secrets.py"
- Wufoo form: https://jessethompson.wufoo.com/forms/z1pdyem009hdgsr/

<h3>Description:</h3>

This program has 2 options when run.<br>
Option 1 retrieves the data entries of a Wufoo form and saves it into a
SQL database.<br>
Option 2 displays the data in a GUI.<br>
When the GUI is selected, it will display a list of names with their respective organizations for selection. 
When a selection is made form the list, the corresponding information will be displayed.<br>
There is also the option of entering data to select and entry. Once the data is entered into the fields, 
the "Click to claim proposal" button is clicked, it will save the data into the tables.

The database consists of a table for WuFoo entries and a table for claiming entries.
The field names are adapted to be easily understood.

The tests on GitHub Actions don't work, and no new tests have been added.<br>
Auto-filling of data on email entry doesn't happen.