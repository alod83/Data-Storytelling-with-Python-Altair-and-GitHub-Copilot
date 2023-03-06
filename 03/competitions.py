# import the required libraries
# load 'data/competitions.csv' as a pandas dataframe
# select only the columns Training Type, Record Time (Seconds), Our Best Time
# calculate the percentage difference between columns Our Best Time and Record Time (Seconds)  and store it into a new column called Percentage Difference
# use the Altair library to plot the following chart:
# draw a single chart which contains a bar chart showing Percentage Difference on the Y axis and Training Type on the X axis, with the values sorted in descending order (-y)
# set the domain of the Y scale to [0,100], set the width of the chart to 300 pixels 

import pandas as pd
import altair as alt

df = pd.read_csv('data/competitions.csv')
df = df[['Training Type', 'Record Time (Seconds)', 'Our Best Time']]
df['Percentage Improvement'] = 100 - (df['Our Best Time'] - df['Record Time (Seconds)']) / df['Record Time (Seconds)'] * 100
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Training Type', sort='-y'),
    y=alt.Y('Percentage Improvement', scale=alt.Scale(domain=[0,100])),
    # add color to the bars: #003049 if the Percentage Improvement is greater than 50, lightgray otherwise
    color=alt.condition(
        alt.datum['Percentage Improvement'] > 50,
        alt.value('#003049'),
        alt.value('lightgray')
    )
    
).properties(
    width=300
)

# add a horizontal red line to the chart at y=50
line = alt.Chart(pd.DataFrame({'y': [50]})).mark_rule(color='red').encode(y='y')

# add the line to the chart
chart = chart + line


chart.save('competitions.html')
