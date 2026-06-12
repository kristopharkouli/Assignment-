#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define THREADS 5
#define INCREMENTS 100000

long long counter = 0;

/* Mutex declaration */
pthread_mutex_t mutex;

/* Function without synchronization */
void* increment_without_mutex(void* arg) {
    for (int i = 0; i < INCREMENTS; i++) {
        counter++;
    }
    pthread_exit(NULL);
}

/* Function with mutex synchronization */
void* increment_with_mutex(void* arg) {
    for (int i = 0; i < INCREMENTS; i++) {
        pthread_mutex_lock(&mutex);
        counter++;
        pthread_mutex_unlock(&mutex);
    }
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[THREADS];

    printf("===== WITHOUT MUTEX =====\\n");
    counter = 0;

    for (int i = 0; i < THREADS; i++) {
        pthread_create(&threads[i], NULL, increment_without_mutex, NULL);
    }

    for (int i = 0; i < THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Expected Counter Value: %d\\n", THREADS * INCREMENTS);
    printf("Actual Counter Value: %lld\\n\\n", counter);

    printf("===== WITH MUTEX =====\\n");
    counter = 0;

    pthread_mutex_init(&mutex, NULL);

    for (int i = 0; i < THREADS; i++) {
        pthread_create(&threads[i], NULL, increment_with_mutex, NULL);
    }

    for (int i = 0; i < THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Expected Counter Value: %d\\n", THREADS * INCREMENTS);
    printf("Actual Counter Value: %lld\\n", counter);

    pthread_mutex_destroy(&mutex);

    return 0;
}
