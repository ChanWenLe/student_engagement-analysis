# Deploy library
library(RMySQL)
library(dplyr)
library(forcats)
library(ggplot2)

# Link to SQL
con = dbConnect(MySQL(), dbname="anl503", user="root", password="111111")
df = suppressWarnings(dbReadTable(conn=con, name="vttclean"))
dbDisconnect(conn=con)



# Calculate the sum of milliseconds for each RegName
result <- df %>%
  group_by(RegName) %>%
  summarise(TotalDuration = sum(milliseconds))

# View the result
print(result)

# Drop rows where RegName is 'INSTRUCTOR' & RegName is NA
result <- result[!(result$RegName == 'INSTRUCTOR' | is.na(result$RegName)), ]


#Arrange the sequence of the bar as descending order of Total Duration
result$RegName <- fct_reorder(result$RegName, result$TotalDuration, .desc = TRUE)

# Plot out the bar chart
ggplot(result, aes(x = RegName, y=TotalDuration)) +
  geom_bar(stat = 'identity',fill = "blue", color = "black")+
  geom_text(aes(label = TotalDuration),vjust = -0.3, color = "black", size = 2.1) +
  scale_y_continuous(labels = scales::comma) + 
  labs(x = "Name of Students", y = "Total Duration(milliseconds)", title = "Accumulated Airtime for Students who Spoke Up ")+
  theme(axis.text.x = element_text(angle = 45, hjust = 1),plot.title = element_text(hjust = 0.5))


