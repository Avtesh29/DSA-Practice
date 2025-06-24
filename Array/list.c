#include <stdlib.h>
#include <stdio.h>
#include "list.h"


int main(int argc, int** argv) {

    list_t* list = create_list();

    printf("Sizeof(int): %ld\n", sizeof(int));          // 4 bytes
    printf("Sizeof(list_t): %ld\n", sizeof(list_t));    // 16 bytes, 4 bytes added to int for padding  

    delete_list(&list);

    return 0;
}