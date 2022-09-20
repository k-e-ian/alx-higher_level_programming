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
	if (!*head)
	{
		new_node = add_nodeint_end(head, number);
		return (new_node);
	}
	if  (node_parser->n > number)
	{
		new_node->next = node_parser;
		new_node->n = number;
		*head = new_node;
		return (new_node);
	}
	while (node_parser->next)
	{
		if (number < node_parser->next->n)
		{
			new_node->next = node_parser->next;
			node_parser->next = new_node;
			new_node->n = number;
			return (new_node);
		}
		node_parser = node_parser->next;
	}
	new_node = add_nodeint_end(head, number);
	return (new_node);
}
