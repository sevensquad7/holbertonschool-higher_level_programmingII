#include "lists.h"
/**
 * comments the code for Holberton School students.
 */
int check_cycle(listint_t *list)
{
	listint_t *before = list;
	listint_t *after = list;

	while (after && after->next)
	{
		before = before->next;
		after = after->next->next;
		if (before == after)
		{
			return (1);
		}
	}
	return (0);
}
