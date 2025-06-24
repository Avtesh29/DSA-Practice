#include <stdlib.h>
#include <stdio.h>
#include "list.h"


int main(int argc, int** argv) {

    list_t* list = create_list();

    

    delete_list(&list);

    return 0;
}