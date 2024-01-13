---
tags:
  - Code
---
***Week 8.1,***

> pm2 start (ready to deploy webpage)   // to start the server
> pm2 kill               // to stop the server

 pm2 helps to keep the server running even if the user has entered any wrong datatype which isn't expected by the backend and could have crashed the servers.

> Use  ***validator.js or zod***  for input validation and avoid entering the wrong inputs/datatypes by,
```
npm install zod

import { z } from "zod";

let titleInputProps = z.object({
	title: z.string().min(1),
	description: z.string().min(1),
})

router.post('/todos', authenticateJwt, (req, res) => {
	const parsedInput = titleInputProps.safeParse(req.body);
	if (!parsedInput.success) {
		return res.status(411).json({
			msg: parsedInput.error
		})
	}
	let title = parsedInput.data.title;
	let description = parsedInput.data.description;
})

```