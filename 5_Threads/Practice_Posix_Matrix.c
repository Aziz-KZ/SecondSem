#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define N 3 // Размер матриц N x N

int A[N][N] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

int B[N][N] = {
    {9, 8, 7},
    {6, 5, 4},
    {3, 2, 1}
};

int C[N][N]; // Результат умножения матриц

typedef struct {
    int row; // индекс строки
} ThreadData;

void *multiply_row(void *arg) {
    ThreadData *data = (ThreadData *)arg;
    int row = data->row;

    for (int j = 0; j < N; j++) {
        C[row][j] = 0;
        for (int k = 0; k < N; k++) {
            C[row][j] += A[row][k] * B[k][j];
        }
    }
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[N];
    ThreadData threadData[N];

    // Создаем потоки, каждый считает одну строку
    for (int i = 0; i < N; i++) {
        threadData[i].row = i;
        pthread_create(&threads[i], NULL, multiply_row, &threadData[i]);
    }

    // Ждем завершения всех потоков
    for (int i = 0; i < N; i++) {
        pthread_join(threads[i], NULL);
    }

    // Вывод результата
    printf("Result matrix:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }

    return 0;
}
