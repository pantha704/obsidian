```



// tsc --init initialise tsconfig.json

function getFirstElement<T>(arr: T[]) {
  return arr[0];
}

let ans1 = getFirstElement<number>([1, 2, 3]);

let ans2 = getFirstElement<string>(["OnE", "two", "three"]);  

// console.log(ans2.toLocaleLowerCase());

function swap<T, U>(a: U, b: T): [T, U] {
  return [b, a];
}

const a = swap(true, "2");
console.log(a);            // Output: ["2", true]
```



> Partials in Typescript,
> example,
>   type todo = {                  // declaring a new type **todo**
> 	  title: string;
> 	  description: string;
> 	  done: boolean;
> 	  id: string;
>   }
>   type UpdateTodoInput = Partial<Todo>   // means a subset of **todo** type. 
