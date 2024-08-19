![image](https://github.com/user-attachments/assets/b38e64d8-9738-4c4d-ac54-aeeee4ba426e) <br>


# Project Summary

In the context of virtual learning, student engagement is a crucial component of the educational experience, particularly as universities increasingly depend on platforms like Zoom to conduct classes. To assess and encourage participation, many courses incorporate a class participation grade into the overall course assessment. However, determining each student's level of engagement through virtual interactions can be challenging.

This project aims to address this challenge by analyzing auto-generated transcripts from Zoom classes to calculate the total airtime each student accumulates by speaking up during class. By measuring airtime in milliseconds, this project seeks to provide a quantitative measure of student participation, offering valuable insights that can help educators enhance engagement strategies and improve the virtual learning experience.

# Data Extraction with Python

The Zoom auto-generated transcript is in VTT format. Each entry in the transcript is structured across three lines, with an empty line separating subsequent entries. The general pattern is as follows: <br>
[SNo]<br>
[TimeFrom] --> [TimeTo]<br>
[RegName]: [Utterance]<br>

Example: <br>

![image](https://github.com/user-attachments/assets/6a52d47e-b654-4dbb-bb83-1553cfda41b5)


### Importing Essential Libraries
To begin, essential Python libraries were imported, with re (Regular Expressions) playing a key role in text processing. This library enabled pattern matching and the extraction of specific data formats, which was crucial for parsing the VTT transcript files. Next, a set of variables was defined to capture different key elements within the VTT file. <br>
  ![image](https://github.com/user-attachments/assets/84615a48-96e5-4e1e-a7fd-f771cb8826e4)



With the regex patterns in place, the file was processed line by line. The function iterated through each line, matching it against the predefined patterns. Relevant information was extracted based on these matches and stored in variables, which were then used to construct a structured table. An elif loop was incorporated to handle scenarios where empty cells might be recorded due to the absence of a speaker or the presence of multiple speakers simultaneously.<br>

![image](https://github.com/user-attachments/assets/987f0799-e419-4b15-9c88-75ba1640d7da)

Finally, once the data was parsed and organized, sqlalchemy was used to create an engine that connected Python to a MySQL database. The DataFrame was then written to a new table in the database using the to_sql method, making it readily accessible for further analysis.


### Data Manipulation with SQL

To streamline the analysis of student engagement data, the original vtt table was duplicated into a new table named vttclean. The timefrom and timeto columns were then refined by altering their data types to TIME(3), ensuring precise measurement in milliseconds. With the data types adjusted, the duration between timefrom and timeto was calculated for each record, converting the result from microseconds to milliseconds. This calculated duration was then recorded in a new column within the vttclean table. These steps ensured that the data was accurately prepared for further analysis, providing a solid foundation for evaluating student participation.


### Data Visualisation with R



R was selected for this analysis due to its robust capabilities in data manipulation and visualization. The RMySQL, dplyr, forcats, and ggplot2 libraries were employed to seamlessly connect to the MySQL database, process the data, and produce a compelling visual representation.

The analysis began by connecting to the anl503 database and loading the vttclean table into a data frame. The total airtime for each student was then computed by summing the milliseconds column, followed by filtering out entries where RegName was either 'INSTRUCTOR' or missing.

To improve clarity, the results were arranged in descending order based on total duration using the fct_reorder function from the forcats package. Finally, the data was visualized using ggplot2, creating a bar chart that effectively displays the accumulated airtime for each student. This visualization makes it easy for readers to identify and compare student engagement levels.
![image](https://github.com/user-attachments/assets/e7622f14-ee74-4b26-bf60-f3e33b928f4e)




