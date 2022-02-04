#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
//#include <unistd.h>

// Atomic data
int atmc_intgr1 = 0;
int atmc_intgr2 = 0;
unsigned atmc_unsgnd1 = 0;
unsigned atmc_unsgnd2 = 0;
long atmc_lng1 = 0;
long atmc_lng2 = 0;
long unsigned atmc_lng_unsgnd1 = 0;
long unsigned atmc_lng_unsgnd2 = 0;

// Atomic functions
void atmc_input();
void atmc_modification();
void atmc_output();

// Threads id
pthread_t P1;
pthread_t P2;
pthread_t P3;
pthread_t P4;
pthread_t P5;
pthread_t P6;

// Mutex id
pthread_mutex_t MCR1 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t MCR2 = PTHREAD_MUTEX_INITIALIZER;

// Signal variables id
pthread_cond_t sig1 = PTHREAD_COND_INITIALIZER;     // Stack is not full
pthread_cond_t sig2 = PTHREAD_COND_INITIALIZER;     // Stack is not empty
pthread_cond_t sig21 = PTHREAD_COND_INITIALIZER;

// Sig21 flags
bool flag_p6_p2 = false;
bool flag_p6_p5 = false;
bool flag_p3_p2 = false;

// Semaphors id
sem_t SCR21;
sem_t SCR22;

// Stack frame struct
typedef struct
{
    int frame_value;
    struct stack_frame *previous_frame;
} stack_frame;

// Stack pointer declaration
stack_frame *stack_top = NULL;

// Stack terminator defining data
const unsigned int terminate_frame = 10;             // Stack top terminator
unsigned int crnt_frame = 0;
unsigned int up_limit = 0;
unsigned int down_limit = 0;

// Service functions signatures
void push_frame();
void pop_frame();

// Stack checking functions
bool isFull();
bool isEmpty();

// Thread functions signatures
void *p1_func(void *thread_arg); // First producer
void *p2_func(void* thread_arg); // Second producer
void *p3_func(void* thread_arg);
void *p4_func(void *thread_arg); // First consumer
void *p5_func(void* thread_arg); // Second consumer
void *p6_func(void* thread_arg);

bool deadlock_flag = false;
void deadlock_killer();


int main()
{
    while (crnt_frame < terminate_frame / 2)
        push_frame();
    printf("\n\n Stack for %d/%d elements has been created\n\n", crnt_frame, terminate_frame);

    sem_init(&SCR21, 0, 0);
    sem_init(&SCR22, 0, 0);

    srand(time(NULL));
    atmc_input();
    printf("\n Atomic data was initialized");
    atmc_output(); 

    pthread_create(&P1, NULL, &p1_func, NULL);
    pthread_create(&P2, NULL, &p2_func, NULL);
    pthread_create(&P3, NULL, &p3_func, NULL);
    pthread_create(&P4, NULL, &p4_func, NULL);
    pthread_create(&P5, NULL, &p5_func, NULL);
    pthread_create(&P6, NULL, &p6_func, NULL);
 
    pthread_join(P1, NULL);
    printf("\n\n Pthread 1 was stopped");
    pthread_join(P2, NULL);
    printf("\n Pthread 2 was stopped");
    pthread_join(P3, NULL);
    printf("\n Pthread 3 was stopped");
    pthread_join(P4, NULL);
    printf("\n Pthread 4 was stopped");
    pthread_join(P5, NULL);
    printf("\n Pthread 5 was stopped");
    pthread_join(P6, NULL);
    printf("\n Pthread 6 was stopped");

    printf("\n\n All theads have been stopped!");

    sem_destroy(&SCR21);
    printf("\n\n Semaphore SCR21 was destroyed");
    sem_destroy(&SCR22);
    printf("\n Semaphore SCR22 was destroyed");

    if(stack_top != NULL)
    {
        printf("\n\n Threads finished their work with not empty stack!");
        while(stack_top != NULL)
            pop_frame();
        printf("\n Stack memory was cleaned before a program ending");
    }

    printf("\n\n UL = %d", up_limit);
    printf("\n DL = %d", down_limit);

    return 0;
}

bool isFull()
{
    return (crnt_frame == terminate_frame);
}

bool isEmpty()
{
    return (crnt_frame == 0);
}

bool end_cond()
{
    return ((up_limit >= 2) && (down_limit >= 2));
}

void *p1_func(void *thread_arg)
{
    pthread_setcancelstate(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);
    printf("\n\n\n Thread P1 has been started!");
    fflush(stdout);
    printf("\n -----------------------------------------------");
    fflush(stdout);
    while (true)
    {
        printf("\n\n P1 Cond checking");
        fflush(stdout);
        if (end_cond())  break;

        pthread_mutex_lock(&MCR1);
        while (isFull() && !deadlock_flag)
        {
            printf("\n P1 locked MCR1 mutex");
            fflush(stdout);
            printf("\n P1 is waiting for \"not full\" signal");
            fflush(stdout);
            printf("\n P1 unlocked MCR1 mutex for dispatch switching");   
            fflush(stdout);
            pthread_cond_wait(&sig1, &MCR1);
            printf("\n P1 received some signal");
            fflush(stdout);
        }
        printf("\n P1 locked MCR1 mutex");
        fflush(stdout);
        printf("\n \"isFull\" condition was not met");
        fflush(stdout);
        push_frame();
        pthread_mutex_unlock(&MCR1);
        printf("\n P1 unlocked MCR1 mutex");
        fflush(stdout);
        pthread_cond_broadcast(&sig2); //Stack is not empty
        printf("\n P1 send sig2 broadcast signal");
        fflush(stdout);
    }
    printf("\n End of P1 thread\n");
    fflush(stdout);
    deadlock_killer();
    return NULL;
}

void* p2_func(void *thread_arg)
{
    pthread_setcancelstate(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);
    printf("\n\n\n Thread P2 has been started!");
    fflush(stdout);
    printf("\n -----------------------------------------------");
    fflush(stdout);
    while (true)
    {
        printf("\n\n P2 Cond checking");
        fflush(stdout);
        if (end_cond())  break;

        pthread_mutex_lock(&MCR1);
        while (isFull() && !deadlock_flag)
        {
            printf("\n P2 (buffer) locked MCR1 mutex");
            fflush(stdout);
            printf("\n P2 (buffer) is waiting for \"not full\" signal");
            fflush(stdout);
            printf("\n P2 (buffer) unlocked MCR1 mutex for dispatch switching");  
            fflush(stdout);
            pthread_cond_wait(&sig1, &MCR1);
            printf("\n P2 (buffer) received some signal");
            fflush(stdout);
        }
        printf("\n P2 (buffer) locked MCR1 mutex");
        fflush(stdout);
        printf("\n \"isFull\" condition was not met");
        fflush(stdout);
        push_frame();
        pthread_mutex_unlock(&MCR1);
        printf("\n P2 (buffer) unlocked MCR1 mutex");
        fflush(stdout);
        pthread_cond_broadcast(&sig2); //Stack is not empty
        printf("\n P2 (buffer) send sig2 broadcast signal");
        fflush(stdout);
        // **********************************************************
        pthread_mutex_lock(&MCR2);
        while(!(flag_p3_p2 || flag_p6_p2) && !deadlock_flag)      
        {
            printf("\n P2 (atmc) locked MCR2 mutex");
            fflush(stdout);
            printf("\n P2 (atmc) is waiting for synchronizing sig21 signal from P3 or P6");
            fflush(stdout);
            printf("\n P2 (atmc) unlocked MCR2 mutex for dispatch switching");
            fflush(stdout);
            pthread_cond_wait(&sig21, &MCR2);
            printf("\n P2 (atmc) received some signal");
            fflush(stdout);
        }
        printf("\n P2 (atmc) locked MCR2 mutex");
        fflush(stdout);
        printf("\n P2 (atmc) received confirmed sig21");
        fflush(stdout);
        flag_p3_p2 = false;
        flag_p6_p5 = false;
        printf("\n flag_p3_p2 = false");
        fflush(stdout);
        printf("\n flag_p6_p5 = false");
        fflush(stdout);
        atmc_output();
        printf("\n P2 (atmc) before modification");
        fflush(stdout);
        atmc_modification();
        printf("\n P2 (atmc) after modification");
        fflush(stdout);
        pthread_mutex_unlock(&MCR2);
        printf("\n P2 (atmc) unlocked MCR2 mutex");
        fflush(stdout);
    }
    printf("\n End of P2 thread\n");
    fflush(stdout);
    deadlock_killer();
    return NULL;
}

void* p3_func(void *thread_arg)
{
    pthread_setcancelstate(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);
    printf("\n\n\n Thread P3 has been started!");
    fflush(stdout);
    printf("\n -----------------------------------------------");
    fflush(stdout);
    while (true)
    {
        printf("\n\n P3 Cond checking");
        fflush(stdout);
        if (end_cond()) break; //

        printf("\n P3 before modification");
        fflush(stdout);
        atmc_modification();
        printf("\n P3 after modification");
        fflush(stdout);

        sem_post(&SCR21);
        printf("\n SCR21 in P3 was opened");
        fflush(stdout);
        printf("\n P3 is waiting for SCR22 opening");
        fflush(stdout);
        sem_wait(&SCR22);
        printf("\n SCR22 in P3 was opened by thread P6");
        fflush(stdout);

        pthread_mutex_lock(&MCR2);
        printf("\n P3 locked MCR2 mutex");
        fflush(stdout);
        flag_p3_p2 = true;
        printf("\n flag_p3_p2 in P3 = true");
        fflush(stdout);
        pthread_mutex_unlock(&MCR2);
        printf("\n P3 unlocked MCR2 mutex");
        fflush(stdout);
        pthread_cond_signal(&sig21);
        printf("\n P3 send sig21 signal");
        fflush(stdout);
        atmc_output();
    }
    printf("\n End of P3 thread\n");
    fflush(stdout);
    deadlock_killer();
    return NULL;
}

void *p4_func(void *thread_arg)
{
    pthread_setcancelstate(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);
    printf("\n\n\n Thread P4 has been started!");
    fflush(stdout);
    printf("\n -----------------------------------------------");
    fflush(stdout);
    while (true)
    {
        printf("\n\n P4 Cond checking");
        fflush(stdout);
        if (end_cond()) break;

        pthread_mutex_lock(&MCR1);
        while (isEmpty() && !deadlock_flag)
        {
            printf("\n P4 locked MCR1 mutex");
            fflush(stdout);
            printf("\n P4 is waiting for \"not full\" signal");
            fflush(stdout);
            printf("\n P4 unlocked MCR1 mutex for dispatch switching");  
            fflush(stdout);
            pthread_cond_wait(&sig2, &MCR1);
            printf("\n P4 received some signal");
            fflush(stdout);
        }
        printf("\n P4 locked MCR1 mutex");
        fflush(stdout);
        printf("\n \"isEmpty\" condition was not met");
        fflush(stdout);
        pop_frame();
        pthread_mutex_unlock(&MCR1);
        printf("\n P4 unlocked MCR1 mutex");
        fflush(stdout);
        pthread_cond_broadcast(&sig1); //Stack is not full
        printf("\n P4 send sig1 broadcast signal");
        fflush(stdout);
    }
    printf("\n End of P4 thread\n");
    fflush(stdout);
    deadlock_killer();
    return NULL;
}

void *p5_func(void *thread_arg)
{
    pthread_setcancelstate(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);
    printf("\n\n\n Thread P5 has been started!");
    fflush(stdout);
    printf("\n -----------------------------------------------");
    fflush(stdout);
    while (true)
    {
        printf("\n\n P5 Cond checking");
        fflush(stdout);
        if (end_cond()) break; //

        pthread_mutex_lock(&MCR1);
        while (isEmpty() && !deadlock_flag)
        {
            printf("\n P5 (buffer) locked MCR1 mutex");
            fflush(stdout);
            printf("\n P5 (buffer) is waiting for \"not empty\" signal");
            fflush(stdout);
            printf("\n P5 (buffer) unlocked MCR1 mutex for dispatch switching");
            fflush(stdout);
            pthread_cond_wait(&sig2, &MCR1);
            printf("\n P5 (buffer) received some signal");
            fflush(stdout);
        }
        printf("\n P5 (buffer) locked MCR1 mutex");
        fflush(stdout);
        printf("\n \"isEmpty\" condition was not met");
        fflush(stdout);
        pop_frame();
        pthread_mutex_unlock(&MCR1);
        printf("\n P5 (buffer) unlocked MCR1 mutex");
        fflush(stdout);
        pthread_cond_broadcast(&sig1); //Stack is not full
        printf("\n P5 send sig1 broadcast signal");
        fflush(stdout);
        // *********************************************************
        pthread_mutex_lock(&MCR2);
        while(!flag_p6_p5 && !deadlock_flag)
        {
            printf("\n P5 (atmc) locked MCR2 mutex");
            fflush(stdout);
            printf("\n P5 (atmc) is waiting for sig21 signal from P6");
            fflush(stdout);
            printf("\n P5 (atmc) unlocked MCR2 mutex for dispatch switching");
            fflush(stdout);
            pthread_cond_wait(&sig21, &MCR2);
            printf("\n P5 (atmc) received some signal");
            fflush(stdout);
        }
        printf("\n P5 (atmc) locked MCR2 mutex");
        fflush(stdout);
        printf("\n P5 (atmc) received confirmed sig21");
        fflush(stdout);
        flag_p6_p5 = false;
        printf("\n flag_p6_p5 in P5 = false");
        fflush(stdout);
        atmc_output();
        pthread_mutex_unlock(&MCR2);
        printf("\n P5 (atmc) unlocked MCR2 mutex");
        fflush(stdout);
    }
    printf("\n End of P5 thread\n");
    fflush(stdout);
    deadlock_killer();
    return NULL;
}

void *p6_func(void *thread_arg)
{
    pthread_setcancelstate(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);
    printf("\n\n\n Thread P6 has been started!");
    fflush(stdout);
    printf("\n -----------------------------------------------");
    fflush(stdout);
    while (true)
    {
        printf("\n\n P6 Cond checking");
        fflush(stdout);
        if (end_cond()) break;

        printf("\n P6 before modification");
        fflush(stdout);
        atmc_modification();
        printf("\n P6 after modification");
        fflush(stdout);

        sem_post(&SCR22);
        printf("\n SCR22 was opened in P6");
        fflush(stdout);
        printf("\n P6 is waiting for SCR21 opening");
        fflush(stdout);
        sem_wait(&SCR21);
        printf("\n SCR21 in P6 was opened by thread P3");
        fflush(stdout);

        pthread_mutex_lock(&MCR2);
        printf("\n P6 mutex MCR2 lock");
        fflush(stdout);
        flag_p6_p2 = true;
        flag_p6_p5 = true;
        printf("\n flag_p6_p2 in P6 = true");
        fflush(stdout);
        printf("\n flag_p6_p5 in P6 = true");
        fflush(stdout);
        pthread_mutex_unlock(&MCR2);
        printf("\n P6 unlocked MCR2 mutex");
        fflush(stdout);
        pthread_cond_broadcast(&sig21);
        printf("\n P6 send sig21 broadcast signal");
        fflush(stdout);
        atmc_output();
    }
    printf("\n End of P6 thread\n");
    fflush(stdout);
    deadlock_killer();
    return NULL;
}

void push_frame()
{
    if(!deadlock_flag)
    {
        if(crnt_frame < terminate_frame)
        {
            stack_frame *buf = stack_top;
            stack_top = (stack_frame *)malloc(sizeof(stack_frame));
            if (stack_top != NULL)
            {
                stack_top->frame_value = ++crnt_frame;
                stack_top->previous_frame = buf;
                printf("\n Stack frame [%d] was created with value = %d", crnt_frame, stack_top->frame_value);
                fflush(stdout);
            }
            else
                stack_top = buf;
        }

        if (crnt_frame == terminate_frame)
        {
            printf("\n\n \tStack buffer is full!");
            fflush(stdout);
            up_limit++;
            printf("\n \tUL = %d\tDL = %d\n", up_limit, down_limit);
            fflush(stdout);
        }
    }
}

void pop_frame()
{
        if (stack_top != NULL)
        {
            stack_frame *buf = stack_top;
            stack_top = stack_top->previous_frame;
            free(buf);
            printf("\n Stack frame [%d] was deleted from stack", crnt_frame);
            fflush(stdout);
            crnt_frame--;
        }

        if (stack_top == NULL)
        {
            printf("\n\n \tStack buffer is empty!");
            fflush(stdout);
            down_limit++;
            printf("\n \tUL = %d\tDL = %d\n", up_limit, down_limit);
            fflush(stdout);
        }
}

void atmc_input()
{
    atmc_intgr1 = rand() % 100;
    atmc_intgr2 = (-1) * (rand() % 100);
    atmc_unsgnd1 = rand() % 100;
    atmc_unsgnd2 = rand() % 100;
    atmc_lng1 = rand() % 300;
    atmc_lng2 = (-1) * (rand() % 300);
    atmc_lng_unsgnd1 = rand() % 300;
    atmc_lng_unsgnd2 = rand() % 300;
}

void atmc_modification()
{
    __sync_fetch_and_add(&atmc_intgr1, (-1) * (rand() % 100));                                      // 1
    __sync_add_and_fetch(&atmc_unsgnd1, rand() % 100);                                              // 7
    __sync_fetch_and_xor(&atmc_unsgnd2, rand() % 100);                                              // 5
    __sync_fetch_and_nand(&atmc_intgr2, (-1) * (rand() % 100));                                     // 6
    __sync_or_and_fetch(&atmc_lng1, (-1) * (rand() % 300));                                         // 9
    __sync_and_and_fetch(&atmc_lng2, (rand() % 300));                                               // 10
    __sync_bool_compare_and_swap(&atmc_lng_unsgnd1, (rand() % 300), (rand() % 300));                // 13
    __sync_val_compare_and_swap(&atmc_lng_unsgnd2, (rand() % 300), (rand() % 300));                 // 14
}

void atmc_output()
{
    printf("\n\n Atomic data:");
    fflush(stdout);
    printf("\n First integer = %d", __sync_fetch_and_add(&atmc_intgr1, 0));
    fflush(stdout);
    printf("\n Second integer = %d", __sync_fetch_and_add(&atmc_intgr2, 0));
    fflush(stdout);
    printf("\n First unsigned integer = %d", __sync_fetch_and_add(&atmc_unsgnd1, 0));
    fflush(stdout);
    printf("\n Second unsigned integer = %d", __sync_fetch_and_add(&atmc_unsgnd2, 0));
    fflush(stdout);
    printf("\n First long integer = %ld", __sync_fetch_and_add(&atmc_lng1, 0));
    fflush(stdout);
    printf("\n Second long integer = %ld", __sync_fetch_and_add(&atmc_lng2, 0));
    fflush(stdout);
    printf("\n First long unsigned integer = %lu", __sync_fetch_and_add(&atmc_lng_unsgnd1, 0));
    fflush(stdout);
    printf("\n Second long unsigned integer = %lu", __sync_fetch_and_add(&atmc_lng_unsgnd2, 0));
    fflush(stdout);
}

void deadlock_killer()
{
    deadlock_flag = true;
    sem_post(&SCR21);
    sem_post(&SCR22);
    pthread_cond_broadcast(&sig1);      
    pthread_cond_broadcast(&sig2);
    pthread_cond_broadcast(&sig21);
}