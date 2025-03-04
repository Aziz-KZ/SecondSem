#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>

#define SOCKET_PATH "example_socket"

int main() {
    int client_fd;
    struct sockaddr_un server_addr;
    char name[256];

    // Создаем сокет
    client_fd = socket(AF_UNIX, SOCK_STREAM, 0);
    if (client_fd == -1) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    // Настройка адреса сервера
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sun_family = AF_UNIX;
    strncpy(server_addr.sun_path, SOCKET_PATH, sizeof(server_addr.sun_path) - 1);

    // Подключаемся к серверу
    if (connect(client_fd, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
        perror("connect failed");
        exit(EXIT_FAILURE);
    }

    printf("Введите имя для передачи на сервер: ");
    fgets(name, sizeof(name), stdin);

    // Отправка имени на сервер
    if (write(client_fd, name, strlen(name)) == -1) {
        perror("write failed");
        exit(EXIT_FAILURE);
    }

    close(client_fd);

    return 0;
}