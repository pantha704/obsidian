> Partials in Typescript,
> example,
>   type todo = {
> 	  title: string;
> 	  description: string;
> 	  done: boolean;
> 	  id: string;
>   }
>   type UpdateTodoInput = Partial<Todo>   // means a subset of **todo type**. 
