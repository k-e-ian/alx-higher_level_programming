#include "lists.h"

/**
 * is_palindrome - function that checks for palindrome
 * @head: list pointer to the first of the linked listss node
 * Return: Condition, 0 and 1 success and failure
 */
int is_palindrome(listint_t **head)
{
	const listint_t *current;
	int len = 0, x = 0, y = 0, tmp[9999];

	if (!*head)
		return (1);
	current = *head;
	while (!current)
	{
		current = current->next;
		len++;
	}
	current = *head;

	while (!current)
	{
		tmp[x] = current->n;
		x++;
		current = current->next;
	}
	x = x - 1;
	len = len - 1;
	while (x >= (len / 2))
	{
		if (tmp[x] != tmp[y])
			return (0);
		x--;
		y++;
	}
	return (1);
}
