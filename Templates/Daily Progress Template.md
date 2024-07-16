---
aliases: 
tags: 
Created: <% tp.file.creation_date() %>
Modified: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
---
<< [[<%tp.date.now("YYYY-MM-DD - ddd", -1)%>]] | [[<%tp.date.now("gggg-[W]ww", 1)%>]] | [[<%tp.date.now("YYYY-MM-DD - ddd", 1)%>]] >>


<%tp.web.daily_quote()%>


```tracker
searchType: dvField
searchTarget: tasksDone
folder: /Daily notes 
datasetName: 🏖️
month:
	startWeekOn: 'Sun'
	color: steelblue
	showSelectedValue: true 
```


Target:: 
- React
- DSA
- cpp
- Flutter
- Rust
- Solana
- learnweb3.io
- Blender
- After Effects

tasksDone:: 
- 


```tracker
searchType: dvField
searchTarget: tasksDone, Target
folder: /Daily notes 
startDate:
endDate:
datasetName: Tasks Done, Total Tasks
line:
    title: "Keep Going!"
    lineColor: lightblue, yellow
    fillGap: true
    showLegend: true
    legendOrientation: vertical
    xAxisLabel: ''
    yAxisLabel: Productivity
```

