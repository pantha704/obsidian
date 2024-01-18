---
tags: 
aliases: 
Created: 2024-01-17 23:00
Modified: Thursday 18th January 2024 13:30:52
---

{{date}}


Day 1 :                [[<% moment(tp.file.title,'YYYY-[W]ww').day(0) %>]]
Day 2 :                
Day 3 :                
Day 4 :                
Day 5 :                
Day 6 :                
Day 7 :                


```tracker
searchType: dvField
searchTarget: tasksDone, Target
folder: /Weekly notes 
startDate: <% moment(tp.file.title,"YYYY-[W]ww").day(0).format("YYYY-MM-DD - ddd") %>
endDate: <% moment(tp.file.title,"YYYY-[W]ww").day(6).format("YYYY-MM-DD - ddd") %>
datasetName: Tasks Done, Total Tasks
line:
    title: "Keep Going!"
    lineColor: blue, yellow
    fillGap: true
    showLegend: true
    legendOrientation: vertical
    xAxisLabel: Dates
    yAxisLabel: Productivity
```


```tracker
searchType: dvField
searchTarget: tasksDone, Target
folder: /Daily notes 
startDate:
endDate:
datasetName: Tasks Done, Total Tasks
line:
    title: "Keep Going!"
    lineColor: blue, yellow
    fillGap: true
    showLegend: true
    legendOrientation: vertical
    xAxisLabel: ''
    yAxisLabel: Productivity
```