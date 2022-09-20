#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly listint_t list
 * @head: pointer to pointer to head
 * @number: the number to be inserted
 * Return: Conditional, fail=NULL, otherwise a pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *node_parser = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;

	if (!node_parser || node_parser->n >= number)
	{
		new_node->next = node_parser;
		*head = new_node;
		return (new_node);
	}
	while (node_parser->next->n < number)
		node_parser = node_parser->next;

	new_node->next = node_parser->next;
	node_parser->next = new_node;

	return (new_node);
}
