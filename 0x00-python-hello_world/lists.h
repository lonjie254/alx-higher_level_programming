#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
<<<<<<< HEAD
=======

>>>>>>> 7aa1491f830d8fc720b18c6fe006726b37ace74b
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
<<<<<<< HEAD
 *
 */
typedef struct listint_s
{
  int n;
  struct listint_s *next;
}listint_t;
=======
 * 
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;
>>>>>>> 7aa1491f830d8fc720b18c6fe006726b37ace74b

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
