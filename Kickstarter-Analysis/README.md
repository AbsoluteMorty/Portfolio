# Kickstarting with Excel

## Overview of Project

### Purpose
  This analysis serves to visualize how other Theater campaigns faired based on their launch date and their fundraising goals to help Louise better understand why her play came close to her fundraising goal in a short amount of time.

## Analysis and Challenges

### Analysis of Outcomes Based on Launch Date
  
  Before I could start my analysis I needed to create a new column in the data extracting the years from the launch dates using the Years() formula. From there I created a pivot table filtering the category and the years. For the rows I put the launch date showing only the months and for the columns and values I set them to Outcomes.
  
  <img src="https://github.com/AbsoluteMorty/Kickstarter-Analysis/blob/main/Resources/Pivot%20table.png" width="600">
  

### Analysis of Outcomes Based on Goals

First I created a new worksheet and named 12 different rows with 12 different ranges increasing in increments of 5,000 up until 50,000. Then I titled 8 columns as shown below.

<img src ="https://github.com/AbsoluteMorty/Kickstarter-Analysis/blob/main/Resources/Goals%20Chart.png" width="600">

I filled out the data in Number Successful, Failed, and Canceled by using the CountIfs() formula 
> =COUNTIFS(Kickstarter!$D:$D, "<1000", Kickstarter!$F:$F, "successful", Kickstarter!R:R, "Plays")
> 
> =COUNTIFS(Kickstarter!$D:$D, ">=1000",Kickstarter!$D:$D, "<4999", Kickstarter!$F:$F, "successful", Kickstarter!R:R, "Plays")

### Challenges and Difficulties Encountered

The biggest challenge I faced while performing this analysis was using the Countifs() formula. I was unfamiliar with the formula and the syntax which forced me to look into examples of it being used. I first attempted to look at the documentation provided by Microsoft and the video provided but my application of the formula was still broken.
My next step was to look at the provided video in the module which had a more specific example that was similar to the use I needed. After I watched the video I better understood the formula and was able to successfully apply my new found knowledge.

## Results

- What are two conclusions you can draw about the Outcomes based on Launch Date?
   
   Based on the line chart created from the pivot table I can conclude that May is the best month to launch a campaign. Another conclusion you could make is December is not a good    month to launch a campaign due to the low amount of successful campaigns.

    <img src = "https://github.com/AbsoluteMorty/Kickstarter-Analysis/blob/main/Resources/Outcomes%20based%20on%20launch%20date.png" width="600">

- What can you conclude about the Outcomes based on Goals?
    
    You can Conlude that the most successful campaigns had a budget less than 4,999 or between 35,000 and 44,999.
    
    <img src = "https://github.com/AbsoluteMorty/Kickstarter-Analysis/blob/main/Resources/Outcomes_vs_Goals.png" width="600">

- What are some limitations of this dataset?

  Within the Theater category the data heavily favors the subcategory Plays. For some of the other subcategories There would not be enough datapoints to make a proper analysis.

- What are some other possible tables and/or graphs that we could create?
 
  Additional graphs we could use to analyize the data further would be an Outcomes based on Country. We would show the most successful country to launch in while filtering based     on parent category and subcategory.
