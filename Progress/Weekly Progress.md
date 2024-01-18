


``` tracker
searchType: dvField
searchTarget: tasksDone
folder: /Weekly notes 
startDate: <% moment(tp.file.title,'YYYY-[W]ww').day(0).format("YYYY-MM-DD - ddd") %>
endDate: <% moment(tp.file.title,'YYYY-[W]ww').day(6).format("YYYY-MM-DD - ddd") %>
datasetName: Progress
line:
    title: "You can do it!"
    lineColor: lightblue
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
