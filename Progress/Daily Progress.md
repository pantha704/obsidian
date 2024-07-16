


```tracker
searchType: dvField
searchTarget: tasksDone
folder: /Daily notes 
datasetName: Progress
month:
	startWeekOn: 'Sun'
	color: steelblue
	showSelectedValue: true 
```


```tracker
searchType: dvField
searchTarget: tasksDone
folder: /Daily notes 
datasetName: Tasks Done
summary:
	template: "Minimum: {{min()}}\n\nMaximum: {{max()}}\n\nAverage: {{average()}} per day\n\nTotal: {{sum()}} tasks completed up till date"
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
    lineColor: lightblue, yellow
    fillGap: true
    showLegend: true
    legendOrientation: vertical
    xAxisLabel: ''
    yAxisLabel: Productivity
```



