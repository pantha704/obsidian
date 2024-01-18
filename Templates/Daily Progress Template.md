---
aliases: 
tags: 
mood: 
target: 
Created: <% tp.file.creation_date() %>
Modified: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
---

<< [[<%tp.date.now("YYYY-MM-DD - ddd", -1)%>]] | [[<%tp.date.now("gggg-[W]ww", 1)%>]] | [[<%tp.date.now("YYYY-MM-DD - ddd", 1)%>]] >>

<%tp.web.daily_quote()%>


Target : 

Day end : 


```tracker
searchType: frontmatter 
searchTarget: mood,target
folder: /Daily notes 
startDate:
endDate:
line:
    title: "Keep Going!"
    xAxisLabel: Dates
    yAxisLabel: Productivity 
```