---
tags: 
aliases: 
Created: <% tp.file.creation_date() %>
Modified: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
---

Day 1 :                [Monday](<Daily notes/<% moment(tp.file.title,'YYYY-[W]ww').day(1).format("YYYY-MM-DD - ddd") %>>)
Day 2 :                [Tuesday](<Daily notes/<% moment(tp.file.title,'YYYY-[W]ww').day(2).format("YYYY-MM-DD - ddd") %>>)
Day 3 :                [Wednesday](<Daily notes/<% moment(tp.file.title,'YYYY-[W]ww').day(3).format("YYYY-MM-DD - ddd") %>>)
Day 4 :                [Thursday](<Daily notes/<% moment(tp.file.title,'YYYY-[W]ww').day(4).format("YYYY-MM-DD - ddd") %>>)
Day 5 :                [Friday](<Daily notes/<% moment(tp.file.title,'YYYY-[W]ww').day(5).format("YYYY-MM-DD - ddd") %>>)
Day 6 :                [Saturday](<Daily notes/<% moment(tp.file.title,'YYYY-[W]ww').day(6).format("YYYY-MM-DD - ddd") %>>)
Day 7 :                [Sunday](<Daily notes/<% moment(tp.file.title,'YYYY-[W]ww').day(7).format("YYYY-MM-DD - ddd") %>>)

tasksDone:: 

```tracker
searchType: dvField
searchTarget: tasksDone
folder: /Daily notes 
startDate: <% moment(tp.file.title,'YYYY-[W]ww').day(0).format("YYYY-MM-DD - ddd") %>
endDate: <% moment(tp.file.title,'YYYY-[W]ww').day(6).format("YYYY-MM-DD - ddd") %>
datasetName: Progress
line:
    title: "You can do it!"
    lineColor: lightgreen
    fillGap: true
    showLegend: true
    legendOrientation: vertical
    xAxisLabel: ''
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