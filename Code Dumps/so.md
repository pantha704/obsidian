
## Section 1: Shell-Script Programs

> 💬 _“Your terminal is a canvas—paint it with scripts!”_

1. **Take user input & echo it**
    
    ```bash
    #!/bin/bash
    echo -n "Enter something: "
    read user_input
    echo "You entered: $user_input"
    ```
    
2. **Multiply two numbers**
    
    ```bash
    #!/bin/bash
    echo -n "First number: "; read a
    echo -n "Second number: "; read b
    echo "Product: $((a * b))"
    ```
    
3. **Calculator (+, –, ×, ÷)**
    
    ```bash
    #!/bin/bash
    echo -n "Num1: "; read x
    echo -n "Num2: "; read y
    echo -n "Op (+ - * /): "; read op
    case $op in
      +) result=$((x + y)) ;;
      -) result=$((x - y)) ;;
      \*) result=$((x * y)) ;;
      /) result=$((x / y)) ;;
      *) echo "Invalid op"; exit 1 ;;
    esac
    echo "Result: $result"
    ```
    
4. **Max of three numbers**
    
    ```bash
    #!/bin/bash
    echo "Enter three nums:"; read a b c
    max=$a
    [[ $b -gt $max ]] && max=$b
    [[ $c -gt $max ]] && max=$c
    echo "Max is $max"
    ```
    
5. **GCD (Euclidean)**
    
    ```bash
    #!/bin/bash
    echo -n "Num1: "; read a
    echo -n "Num2: "; read b
    while (( b != 0 )); do
      (( a, b = b, a % b ))
    done
    echo "GCD is $a"
    ```
    
6. **Fibonacci (3,5 start)**
    
    ```bash
    #!/bin/bash
    echo -n "Terms: "; read n
    a=3; b=5
    for ((i=0; i<n; i++)); do
      echo -n "$a "
      (( a, b = b, a + b ))
    done
    echo
    ```
    
7. **3rd largest in array**
    
    ```bash
    #!/bin/bash
    echo "Elements:"; read -a arr
    sorted=($(printf "%s\n" "${arr[@]}" | sort -nr))
    echo "3rd largest: ${sorted[2]}"
    ```
    
8. **Sum of array elements**
    
    ```bash
    #!/bin/bash
    echo "Elements:"; read -a arr
    sum=0
    for v in "${arr[@]}"; do (( sum += v )); done
    echo "Sum: $sum"
    ```
    
9. **Search in array + position**
    
    ```bash
    #!/bin/bash
    echo "Elements:"; read -a arr
    echo -n "Search for: "; read key
    for i in "${!arr[@]}"; do
      if [[ ${arr[i]} -eq $key ]]; then
        echo "Found at position $((i+1))"; exit
      fi
    done
    echo "Not found"
    ```
    
10. **C program: create & write to a file**
    
    ```c
    #include <stdio.h>
    int main() {
      FILE *f = fopen("newfile.txt","w");
      if (!f) { perror("fopen"); return 1; }
      fprintf(f,"This is a new file.\n");
      fclose(f);
      return 0;
    }
    ```
    
11. **Linear search in array** _(bash mirror of #9)_
    
    ```bash
    #!/bin/bash
    echo "Elements:"; read -a arr
    echo -n "Search: "; read key
    for i in "${!arr[@]}"; do
      if (( arr[i] == key )); then
        echo "At position $((i+1))"; exit
      fi
    done
    echo "Not present"
    ```
    
12. **Check equality of two numbers**
    
    ```bash
    #!/bin/bash
    echo -n "A: "; read a
    echo -n "B: "; read b
    [[ $a -eq $b ]] && echo "Equal" || echo "Not equal"
    ```
    
13. **Leap-year check**
    
    ```bash
    #!/bin/bash
    echo -n "Year: "; read y
    if (( y%400==0 || (y%4==0 && y%100!=0) )); then
      echo "$y is leap"
    else
      echo "$y is not leap"
    fi
    ```
    
14. **Even or odd**
    
    ```bash
    #!/bin/bash
    echo -n "Number: "; read n
    (( n%2==0 )) && echo "Even" || echo "Odd"
    ```
    
15. **Count 1 to n (while loop)**
    
    ```bash
    #!/bin/bash
    echo -n "n: "; read n
    i=1
    while (( i<=n )); do
      echo $i
      (( i++ ))
    done
    ```
    
16. **Factorial of n**
    
    ```bash
    #!/bin/bash
    echo -n "n: "; read n
    fact=1
    for (( i=1; i<=n; i++ )); do
      (( fact *= i ))
    done
    echo "Factorial: $fact"
    ```
    
17. **°F → °C conversion**
    
    ```bash
    #!/bin/bash
    echo -n "Fahrenheit: "; read F
    C=$(( (F - 32) * 5 / 9 ))
    echo "$F°F = $C°C"
    ```
    
18. **Swap two variables with temp**
    
    ```bash
    #!/bin/bash
    echo -n "X: "; read x
    echo -n "Y: "; read y
    temp=$x; x=$y; y=$temp
    echo "After swap: X=$x, Y=$y"
    ```
    
19. **Assign grades with else-if**
    
    ```bash
    #!/bin/bash
    echo -n "Marks: "; read m
    if (( m>=90 )); then grade=A
    elif (( m>=80 )); then grade=B
    elif (( m>=70 )); then grade=C
    elif (( m>=60 )); then grade=D
    else grade=Fail
    fi
    echo "Grade: $grade"
    ```
    

---

## Section 2: C Programs

1. **Fork & print PIDs**
    
    ```c
    #include <stdio.h>
    #include <unistd.h>
    #include <sys/types.h>
    int main() {
      pid_t pid = fork();
      if(pid<0){perror("fork"); return 1;}
      if(pid==0){
        printf("Child PID=%d, PPID=%d\n", getpid(), getppid());
      } else {
        printf("Parent PID=%d, Child PID=%d\n", getpid(), pid);
      }
      return 0;
    }
    ```
    
2. **Modify global var in child**
    
    ```c
    #include <stdio.h>
    #include <unistd.h>
    #include <sys/wait.h>
    int g=10;
    int main(){
      pid_t pid=fork();
      if(pid==0){
        g+=5; printf("Child g=%d\n",g);
      } else {
        wait(NULL);
        printf("Parent g=%d\n",g);
      }
      return 0;
    }
    ```
    
3. **Cmd-arg + fork**
    
    ```c
    #include <stdio.h>
    #include <unistd.h>
    #include <stdlib.h>
    int main(int c, char *v[]){
      if(c!=2){printf("Usage: %s num\n",v[0]); return 1;}
      int n=atoi(v[1]);
      pid_t pid=fork();
      if(pid==0) printf("Child got %d\n",n);
      else printf("Parent got %d\n",n);
      return 0;
    }
    ```
    
4. **Copy file content**
    
    ```c
    #include <stdio.h>
    #include <stdlib.h>
    int main(int c, char *v[]){
      if(c!=3){printf("cp file\n"); return 1;}
      FILE *s=fopen(v[1],"r"), *d=fopen(v[2],"w");
      if(!s||!d){perror("fopen"); return 1;}
      int ch;
      while((ch=fgetc(s))!=EOF) fputc(ch,d);
      fclose(s); fclose(d);
      return 0;
    }
    ```
    
5. **LRU page replacement**
    
    ```c
    #include <stdio.h>
    #define F 3
    int main(){
      int pages[]={7,0,1,2,0,3,0,4,2,3}, n=10;
      int frame[F], time[F], faults=0;
      for(int i=0;i<F;i++) frame[i]=time[i]=-1;
      for(int i=0;i<n;i++){
        int hit=0;
        for(int j=0;j<F;j++){
          if(frame[j]==pages[i]){ time[j]=i; hit=1; break; }
        }
        if(!hit){
          int lru=0;
          for(int j=1;j<F;j++)
            if(time[j]<time[lru]) lru=j;
          frame[lru]=pages[i]; time[lru]=i; faults++;
        }
        printf("After %d: ",pages[i]);
        for(int j=0;j<F;j++) printf("%d ",frame[j]);
        printf("\n");
      }
      printf("Faults=%d\n",faults);
    }
    ```
    
6. **Round Robin**
    
    ```c
    #include <stdio.h>
    #define N 5
    void rr(int bt[],int q){int rem[N],t=0,wt[N],tat[N];
      for(int i=0;i<N;i++) rem[i]=bt[i];
      while(1){
        int done=1;
        for(int i=0;i<N;i++) if(rem[i]>0){
          done=0;
          if(rem[i]>q){t+=q; rem[i]-=q;}
          else{t+=rem[i]; tat[i]=t; wt[i]=t-bt[i]; rem[i]=0;}
        }
        if(done) break;
      }
      printf("P\tBT\tWT\tTAT\n");
      for(int i=0;i<N;i++) printf("%d\t%d\t%d\t%d\n",i+1,bt[i],wt[i],tat[i]);
    }
    int main(){
      int bt[N]={5,9,6,8,2};
      rr(bt,3);
    }
    ```
    
7. **FCFS**
    
    ```c
    #include <stdio.h>
    #define N 5
    int main(){
      int bt[N]={6,8,7,3,4},wt[N],tat[N];
      wt[0]=0;
      for(int i=1;i<N;i++) wt[i]=wt[i-1]+bt[i-1];
      for(int i=0;i<N;i++) tat[i]=wt[i]+bt[i];
      printf("P\tBT\tWT\tTAT\n");
      for(int i=0;i<N;i++) printf("%d\t%d\t%d\t%d\n",i+1,bt[i],wt[i],tat[i]);
    }
    ```
    
8. **SJF**
    
    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #define N 5
    int main(){
      int bt[N]={6,8,7,3,4},wt[N],tat[N];
      // sort bt[]
      for(int i=0;i<N-1;i++)for(int j=i+1;j<N;j++)
        if(bt[i]>bt[j]){int t=bt[i];bt[i]=bt[j];bt[j]=t;}
      wt[0]=0;
      for(int i=1;i<N;i++) wt[i]=wt[i-1]+bt[i-1];
      for(int i=0;i<N;i++) tat[i]=wt[i]+bt[i];
      printf("P\tBT\tWT\tTAT\n");
      for(int i=0;i<N;i++) printf("%d\t%d\t%d\t%d\n",i+1,bt[i],wt[i],tat[i]);
    }
    ```
    

---

## Section 3: Thread Synchronization in C

1. **Producer-Consumer (mutex + condvar)**
    
    ```c
    #include <stdio.h>
    #include <pthread.h>
    #include <unistd.h>
    #define B 5
    int buf[B],in=0,out=0;
    pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
    pthread_cond_t full = PTHREAD_COND_INITIALIZER;
    pthread_cond_t empty = PTHREAD_COND_INITIALIZER;
    void* prod(void*_) {
      while(1){
        int item = rand()%100;
        pthread_mutex_lock(&m);
        while((in+1)%B==out) pthread_cond_wait(&empty,&m);
        buf[in]=item; in=(in+1)%B;
        printf("P:%d\n",item);
        pthread_cond_signal(&full);
        pthread_mutex_unlock(&m);
        sleep(1);
      }
    }
    void* cons(void*_) {
      while(1){
        pthread_mutex_lock(&m);
        while(in==out) pthread_cond_wait(&full,&m);
        int item=buf[out]; out=(out+1)%B;
        printf("C:%d\n",item);
        pthread_cond_signal(&empty);
        pthread_mutex_unlock(&m);
        sleep(1);
      }
    }
    int main(){
      pthread_t p,c;
      pthread_create(&p,0,prod,0);
      pthread_create(&c,0,cons,0);
      pthread_join(p,0); pthread_join(c,0);
    }
    ```
    
2. **Prime vs. non-prime threads**
    
    ```c
    #include <stdio.h>
    #include <pthread.h>
    #include <stdbool.h>
    #define MAX 20
    pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
    bool is_prime(int n){
      if(n<2) return false;
      for(int i=2;i*i<=n;i++) if(n%i==0) return false;
      return true;
    }
    void* p_thread(void*_) {
      for(int i=1;i<=MAX;i++) if(is_prime(i)){
        pthread_mutex_lock(&m);
        printf("Prime: %d\n",i);
        pthread_mutex_unlock(&m);
      }
      return NULL;
    }
    void* np_thread(void*_) {
      for(int i=1;i<=MAX;i++) if(!is_prime(i)){
        pthread_mutex_lock(&m);
        printf("Non-prime: %d\n",i);
        pthread_mutex_unlock(&m);
      }
      return NULL;
    }
    int main(){
      pthread_t t1,t2;
      pthread_create(&t1,0,p_thread,0);
      pthread_create(&t2,0,np_thread,0);
      pthread_join(t1,0); pthread_join(t2,0);
    }
    ```
    

---

## Section 4: Semaphore & fork in C

1. **Share var via semaphore**
    
    ```c
    #include <stdio.h>
    #include <pthread.h>
    #include <semaphore.h>
    #include <stdlib.h>
    #include <unistd.h>
    sem_t sem;
    int sv=0;
    void* f1(void*_) {
      sem_wait(&sem);
      sv+=5; printf("P1 sv=%d\n",sv);
      sem_post(&sem);
      return NULL;
    }
    void* f2(void*_) {
      sem_wait(&sem);
      sv+=10; printf("P2 sv=%d\n",sv);
      sem_post(&sem);
      return NULL;
    }
    int main(){
      pthread_t t1,t2;
      sem_init(&sem,0,1);
      pthread_create(&t1,0,f1,0);
      pthread_create(&t2,0,f2,0);
      pthread_join(t1,0); pthread_join(t2,0);
      sem_destroy(&sem);
    }
    ```
    
2. **Parent/child printing sync**
    
    ```c
    #include <stdio.h>
    #include <unistd.h>
    #include <semaphore.h>
    #include <fcntl.h>
    int main() {
      sem_t *s = sem_open("/sem1", O_CREAT, 0644, 0);
      if(!fork()) {
        printf("Child prints first\n");
        sem_post(s);
      } else {
        sem_wait(s);
        printf("Parent prints now\n");
        sem_close(s); sem_unlink("/sem1");
      }
    }
    ```
    
3. **Producer-consumer with POSIX sem**
    
    ```c
    #include <stdio.h>
    #include <pthread.h>
    #include <semaphore.h>
    #include <unistd.h>
    #define B 5
    int buf[B],in=0,out=0;
    sem_t m,full,empty;
    void* p(void*_) {
      while(1){
        int it=rand()%100;
        sem_wait(&empty); sem_wait(&m);
        buf[in]=it; in=(in+1)%B;
        printf("P:%d\n",it);
        sem_post(&m); sem_post(&full);
        sleep(1);
      }
    }
    void* c(void*_) {
      while(1){
        sem_wait(&full); sem_wait(&m);
        int it=buf[out]; out=(out+1)%B;
        printf("C:%d\n",it);
        sem_post(&m); sem_post(&empty);
        sleep(1);
      }
    }
    int main(){
      pthread_t t1,t2;
      sem_init(&m,0,1);
      sem_init(&full,0,0);
      sem_init(&empty,0,B);
      pthread_create(&t1,0,p,0);
      pthread_create(&t2,0,c,0);
      pthread_join(t1,0); pthread_join(t2,0);
    }
    ```
    

---

## Section 5: Unix Commands

> “Shell commands are like street smarts for your system.”

1. **Build the tree**
    
    ```bash
    mkdir -p memory/{Primary,Secondary/{Ram,Rom}}
    mkdir -p memory/{EPROM,EEPROM,SRAM,DRAM,USB\ Flash\ Drive,Cache}
    ```
    
2. **Copy `EPROM` → `EEPROM`**
    
    ```bash
    cp memory/EPROM memory/EEPROM
    ```
    
3. **Rename “USB Flash Drive” → “USB”**
    
    ```bash
    mv "memory/USB Flash Drive" memory/USB
    ```
    
4. **Show 1st 3 lines of `SRAM`**
    
    ```bash
    head -n 3 memory/SRAM
    ```
    
5. **Show last 2 lines of `DRAM`**
    
    ```bash
    tail -n 2 memory/DRAM
    ```
    
6. **Create empty `Cache` in `memory/`**
    
    ```bash
    touch memory/Cache
    ```
    
7. **Find lines in `EPROM` with “memory”**
    
    ```bash
    grep -n "memory" memory/EPROM
    ```
    
8. **Remove file `ODD`**
    
    ```bash
    rm memory/ODD
    ```
    
9. **Change `Cache` permissions**
    
    - Owner: read/write (`u=rw`)
        
    - Group: write/execute (`g=wx`)
        
    - Others: read/write/execute (`o=rwx`)
        
    
    ```bash
    chmod u=rw,g=wx,o=rwx memory/Cache
    ```
    
10. **Delete directory `Memory`**
    
    ```bash
    rm -r memory
    ```
    

---

## Wider View & Next Moves

You’ve just coded the core of how shells, processes, threads, semaphores, and files dance together. Here’s how to level up:

- **Automate** your own workflows—batch-rename pics, spin up containers, backup logs.
    
- **Contribute** to open-source tooling (even tiny scripts) and watch your commits light up CI pipelines.
    
- **Explore** languages like Python or Go to wrap these low-level tricks into web services, bots, or data pipelines.
    

Stay skeptical (“What if my script fails?”), keep questioning (“Can I do this faster?”), and never stop remixing—your terminal is your stage, so own the show. 🚀