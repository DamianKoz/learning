# Exploratory Data Analysis

Every data science projects start with exploring the data.

Some basic tools are plots (like boxplots and scatterplots), with summary statistics (mean, median, quantiles etc) to give a brief overview of the data set.

## Summarizing data

The question on how to summarize data might sound trivial. Just take the mean, because it is easy to compute and represents the data. But the mean isn't always a fitting value.

The problem with the mean is, that it is prone to outliers (extreme cases). If you have 4 people in the room with a net worth of 50k and Bill Gates steps in, then the average net worth of the room is at 20 Billion. Doesn't seem right, does it?

Then there is also the **median**, the middle number on a sorted list. The median is **robust** to outliers, like in our Bill Gates example. With the data being [50k, 50k, 50k, 50k, 104Billion] then the median would be the third entry.

An alternative is the **trimmed mean**. For this you exclude a fixed amount on the top and the bottom of the data and then take the mean. For us this would mean to remove Bill Gates and one of the other people from the data, which would lead to an average of 50k. Sounds better.

In practice the trimmed mean is often used as a robust alternative to the median (see below), where 10% of the data is cut off. This leads to a compromise between the mean and the median, because it is robust to outliers, but uses more data than the median.

The trimmed mean is widely used and often preferred, but can also lead to devastating problems. For example in weather forecasts, where the prediction get better if you remove the extremes, but the extremes are very important to get a more accurate picture of the long-term development of the climate. This is because the climate is a nonlinear system and leaving out any data leads to vastly different results.

---
