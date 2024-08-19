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


With the regex patterns established, the file was processed line by line. The function iterated through each line, matching it against the predefined patterns. Depending on the matches found, relevant information was extracted and stored in variables, which were later used to form a structured table. <br>

![image](https://github.com/user-attachments/assets/987f0799-e419-4b15-9c88-75ba1640d7da)

Finally, once the data was parsed and organized, sqlalchemy was used to create an engine that connected Python to a MySQL database. The DataFrame was then written to a new table in the database using the to_sql method, making it readily accessible for further analysis and reporting.
