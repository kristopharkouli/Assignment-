# Assignment 16: Multithreaded C Program using POSIX Threads and Semaphores

## Objective

Implement the Producer-Consumer problem using POSIX threads (`pthread`)
and semaphores to demonstrate thread synchronization and safe
shared-memory access.

## Features

-   Uses POSIX Threads (`pthread`)
-   Uses Semaphores for synchronization
-   Implements Producer-Consumer architecture
-   Prevents race conditions using mutex locks
-   Demonstrates inter-thread communication

## C Program

``` c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;

sem_t empty;
sem_t full;
pthread_mutex_t mutex;

void* producer(void* arg) {
    int item;

    for (int i = 1; i <= 10; i++) {
        item = i;

        sem_wait(&empty);
        pthread_mutex_lock(&mutex);

        buffer[in] = item;
        printf("Producer produced item: %d at position %d\n", item, in);

        in = (in + 1) % BUFFER_SIZE;

        pthread_mutex_unlock(&mutex);
        sem_post(&full);

        sleep(1);
    }

    pthread_exit(NULL);
}

void* consumer(void* arg) {
    int item;

    for (int i = 1; i <= 10; i++) {
        sem_wait(&full);
        pthread_mutex_lock(&mutex);

        item = buffer[out];
        printf("Consumer consumed item: %d from position %d\n", item, out);

        out = (out + 1) % BUFFER_SIZE;

        pthread_mutex_unlock(&mutex);
        sem_post(&empty);

        sleep(2);
    }

    pthread_exit(NULL);
}

int main() {
    pthread_t producerThread;
    pthread_t consumerThread;

    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);
    pthread_mutex_init(&mutex, NULL);

    pthread_create(&producerThread, NULL, producer, NULL);
    pthread_create(&consumerThread, NULL, consumer, NULL);

    pthread_join(producerThread, NULL);
    pthread_join(consumerThread, NULL);

    sem_destroy(&empty);
    sem_destroy(&full);
    pthread_mutex_destroy(&mutex);

    printf("\nAll threads completed successfully.\n");

    return 0;
}
```

## Synchronization Explanation

1.  `empty` semaphore tracks available buffer slots.
2.  `full` semaphore tracks occupied buffer slots.
3.  Mutex ensures only one thread accesses shared memory at a time.
4.  Producer waits when the buffer is full.
5.  Consumer waits when the buffer is empty.
6.  `sem_wait()` blocks threads until resources become available.
7.  `sem_post()` signals waiting threads.

## Conclusion

This program demonstrates thread synchronization using POSIX threads,
semaphores, and mutex locks, ensuring safe access to shared resources
and preventing race conditions.
