# Project Summary

In the context of virtual learning, student engagement is a crucial component of the educational experience, particularly as universities increasingly depend on platforms like Zoom to conduct classes. To assess and encourage participation, many courses incorporate a class participation grade into the overall course assessment. However, determining each student's level of engagement through virtual interactions can be challenging.

This project aims to address this challenge by analyzing auto-generated transcripts from Zoom classes to calculate the total airtime each student accumulates by speaking up during class. By measuring airtime in milliseconds, this project seeks to provide a quantitative measure of student participation, offering valuable insights that can help educators enhance engagement strategies and improve the virtual learning experience.

# Data Extraction

The Zoom auto-generated transcript is in vtt, the transcript was stored in the following sequence, with each entry spreaded across three lines with an empty line separating subsequent entries. The general pattern is…
[SNo]
[TimeFrom] --> [TimeTo]
[RegName]: [Utterance]

Example:
![image](https://github.com/user-attachments/assets/6a52d47e-b654-4dbb-bb83-1553cfda41b5)
