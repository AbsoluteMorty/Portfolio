# Analyzing Stocks With VBA

## Overview of Project
This analysis serves to shine a light on refactoring code to increase speed and efficiency.
I have already made a VBA script to analyze all of the stock data provided based on the year requested, but it is in efficient.
To make this script scaleable I will be streamlining my script to reduce the workload on the computer.

   ## Results
   The biggest slow down for my code was I would loop through all the rows for each ticker which made about 92% of the work needlessly redundant.
   This caused my original script to run slow.
   
   <img src ="https://github.com/AbsoluteMorty/Stock_Analysis/blob/main/Resources/2017%20old.png" width="300"> <img src ="https://github.com/AbsoluteMorty/Stock_Analysis/blob/main/Resources/2018%20old.png" width="300">    
   
   
   I overcame this issue by creating seperate arrays for tickerVolumes, tickerStartingPrice and tickerEndingPrice. I then used a tickerIndex variable which I used monitor for  
   ticker changes and assign data to the right ticker.
   
   <img src ="https://github.com/AbsoluteMorty/Stock_Analysis/blob/main/Resources/Code%20after.png" width="1200"> 
   
   As a result the computer only had to loop over the rows once to gather the correct information Drastically improving time. 
   
   <img src ="https://github.com/AbsoluteMorty/Stock_Analysis/blob/main/Resources/VBA_Challenge_2017.png" width="300"> <img src ="https://github.com/AbsoluteMorty/Stock_Analysis/blob/main/Resources/VBA_Challenge_2018.png" width="300"> 
   
   
 
## Summary

### Refactoring Code | Pros and Cons
In general it is good to look back at your code and think of ways you can make it more efficient. This allows you to future proof your code and widen its compatibility.
One thing to note is it is just as easy to overcomplicate your code making it so abstract it takes forever to debug while making it unclear what is happening in the code. As with anything there is always a balance.

### Relevence to VBA
As it pertains to our example, our code needed alot of work. As I stated in the beginning, our code spent about 92% of the time not making progress becuase it was combing through stocks and not doing anything with them as it passed them. While this does make things more efficient it does make the code easier to break and harder to debug which in most cases it is worth it.
