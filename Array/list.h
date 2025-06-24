// Implementation of Python's built in List object, essentially a dynamic array
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>


// List struct representing Python's List object with length and array properties,
// array contains void* elements so that it can point to any type
struct list{
    void** array;
    int length;
};
typedef struct list list_t;

// Create empty list
list_t* create_list() {
    
    list_t* list = (list_t*)malloc(sizeof(list_t));
    list->array = (void**)malloc(sizeof(void*));
    list->length = 0;

    return list;
}

// Add element to the end of list
bool list_append(list_t* list, void* elem) {

    return true;
}

// Delete list
void delete_list(list_t** list) {

    if ((*list)->array != NULL) {
        free((*list)->array);
        (*list)->array = NULL;
    }

    free(*list);
}