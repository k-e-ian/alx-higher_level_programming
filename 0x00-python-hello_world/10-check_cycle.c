#include "lists.h"

/**
 * check_cycle - check if a singly linked listint_t contains a cycle
 * @list: listint_t singly linked list
 * Return: Conditional 0 if there's no circle, 1 if there's a circle
 */
int check_cycle(listint_t *list)
{
	listint_t *infront = list, *behind = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (infront)
	{
		behind = behind->next;
		infront = infront->next->next;
		if (infront == behind)
			return (1);
	}
	return (0);
}
