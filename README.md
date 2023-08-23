# Pay form automation

This code will fill out the timesheet with data from .csv files. It is very important for these to be saved as .csv files or else this will not work.
- Make sure files are saved in the correct format, with that being date, time in, time out, and total worked as each of the collumns, respectively. 
- Do not add any labels or anything, just data. You can use my sheet as an example. Make sure to fill in blank spaces with zeros
- You will have to edit a couple of things in the init class to match your personal
information. You can either copy these exactly from the form or from the .html file included. It is important for these to be exact or it won't work. 
- Totals will be automatically calculated, make sure these are correct before submitting
 - You will
(probably) need to install selenium, which can be done with 
`pip install selenium `. ONLY WORKS FOR SELENIUM >= 4.10 
- When you run the program you will be redirected to the university's sso page, you will have ~10 seconds to fill this out, and after
that all you need to do is watch, check that everything is correct, and press submit. The window will automatically close WITHOUT SUBMITTING after 100 seconds

