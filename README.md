# Football-Analysis-and-player-comparison
This Python script analyses and visualises a football player statistic dataset using the pandas, matplotlib, and plotly packages. The code is organised as follows:
# Dependencies
pandas
matplotlib
plotly

# Purpose
The purpose of this project is to provide insights into the performance of football players based on their statistics. By analyzing the data and visualizing it in various plots, users can gain a better understanding of player performance trends and make informed comparisons.

# Steps
Install Dependencies:

Firstly I have Install the required libraries by running pip install pandas matplotlib plotly in terminal.
Dataset:

Then I have uploaded dataset which i got from kaggel and then using 'pandas' library 

Then I have Perform data transformations on the DataFrame and Remove any missing values from the DataFrame

Created various plots using plotly.express:
Line plots for "Number of Goals Scored Throughout the Years" and "Average Shots Taken per Player"
Calculate and plot "Average Goals Scored per Match" and "Number of Missed Goals per Player"
Line plots for "Average Goals Scored per Match" and "Number of Goals Scored per Minute"
Bar plots for "Number of Goals Scored per Player," "Number of Goals Scored per Minute," "Number of Missed Goals Shot by Players," "Avg Goals Scored per Match," and "Avg Shots Taken per Match"
Scatter plots for "Minutes Played vs Goals," "Matches Played vs Goals," and "Shots vs Goals"

# Create a graphical user interface (GUI) using tkinter for player comparison:

Display a window with a player selection listbox and a compare button.
Define a function to compare selected players and display the comparison results as labels in the GUI.
Display a bar graph comparing the goals scored by the selected players using matplotlib.
