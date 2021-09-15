#include "lists.h"

/**
 * is_palindrome - Validate if list is palindrome
 * @head: List
 *
 * Return: 1 if is palindrome or 0 if not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *h;
	int i = 0, n = 0;
	int *numbers;

	if (head == NULL)
		return (1);

	h = *head;

	while (!h)
	{
		*numbers = h->n;
	        h = h->next;
		n++;
		numbers++;
	}

	if (n == 0)
		return (1);


	while (i < n / 2)
	{
		if (numbers[i] != numbers[n - i - 1])
			return (0);
	}

	return (1);
}
