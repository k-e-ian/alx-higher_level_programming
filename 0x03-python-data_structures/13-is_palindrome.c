#include "lists.h"

/**
 * is_palindrome - function that checks for palindrome
 * @head: list pointer to the first of the linked listss node
 * Return: Condition, 0 and 1 success and failure
 */
int is_palindrome(listint_t **head)
{
	const listint_t *current;
	int len, x, y, tmp[9999];

	if (*head == NULL)
		return (1);
	current = *head;
	len = 0;
	while (current != NULL)
	{
		current = current->next;
		len++;
	}
	if (len == 1)
		return (1);
	current = *head;
	x = 0;
	while (current != NULL)
	{
		tmp[x] = current->n;
		x++;
		current = current->next;
	}
	y = 0;
	x--;
	len--;
	while (x >= (len / 2))
	{
		if (tmp[x] != tmp[y])
			return (0);
		x--;
		y++;
	}
	return (1);
}
