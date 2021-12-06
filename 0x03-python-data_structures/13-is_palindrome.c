#include "lists.h"

/**
 * is_palindrome - Validate if list is palindrome
 * @head: List
 *
 * Return: 1 if is palindrome or 0 if not palindrome
 */
int is_palindrome(listint_t **head)
{		  
	listint_t *vodka = *head;	
	listint_t *vino = *head;	
	listint_t *ron = NULL;		
	int count = 0;	
	int ver = 0;	

	if (*head == NULL)
		return (1);
	while (vino->next != NULL)	
	{	
		vino = vino->next;		
		count += 1;		
	}
	 if (count % 2 != 0)
	 {
		 count -= 1;	
	 }
	while (ver < count/2)
	{
		if (vodka->n != vino->n)	
		{
			return (0);	
		}
		vodka = vodka->next;
		ron = vodka;
		while (ron->next != vino)
		{
			ron = ron->next;	
		}
		vino = ron;	
		ver++;		
	}	
	return (1);
}
