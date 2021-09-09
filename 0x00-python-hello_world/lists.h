#ifndef HOLBER_LISTS
#define HOLBER_LISTS

#include <stdlib.h>

/**
 * struct listint_s - function in C that checks if a
 * singly linked list has a cycle in it.
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* HOLBER_LISTS */
