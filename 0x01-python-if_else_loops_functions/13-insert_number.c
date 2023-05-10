#include "lists.h"

/**
 * insert_node - Position a number into a sorted singly-linked list.
 * @head: Pointer the head of the linked list.
 * @number: Number to insert.
 * Return: 0 if the function fails or points to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *fresh;

	fresh = malloc(sizeof(listint_t));
	
	if (fresh == NULL)
		return (NULL);
	fresh->n = number;

	if (node == NULL || node->n >= number)
	{
		fresh->next = node;
		*head = fresh;
		return (fresh);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	fresh->next = node->next;
	node->next = fresh;

	return (fresh);
}
