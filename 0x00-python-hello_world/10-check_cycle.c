#include "lists.h"

/**
 * check_cycle - check if a singly linked listint_t contains a cycle
 * @list: listint_t singly linked list
 * Return: Conditional 0 if there's no circle, 1 if there's a circle
 */
int check_cycle(listint_t *list)
{
/**	listint_t *infront, *behind;

	if (list == NULL || list->next == NULL)
		return (0);

	behind = list->next;
	infront = list->next->next;

	while (infront && behind && behind->next)
	{
		if (infront == behind)
			return (1);
		behind = behind->next;
		infront = infront->next->next;
	}
	return (0);**/
	listint_t *head, *infront;

	if (list == NULL || list->next == NULL)
		return (0);

	head = list->next;
	infront = list->next->next;
	
	while (head && infront)
	{
		if (head == infront)
			return (1);
		head = head->next;
		infront = infront->next->next;
	}
	return (0);
}
