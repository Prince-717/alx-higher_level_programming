#include "lists.h"

/**
 * reverse_linked_list - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_linked_list(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}

	*head = previous;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_node = *head;
	listint_t *fast_node = *head;
	listint_t *temporary_node = *head;
	listint_t *duplicate_node = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return 1;

	while (1)
	{
		fast_node = fast_node->next->next;
		if (fast_node == NULL)
		{
			duplicate_node = slow_node->next;
			break;
		}
		if (fast_node->next == NULL)
		{
			duplicate_node = slow_node->next->next;
			break;
		}
		slow_node = slow_node->next;
	}

	reverse_linked_list(&duplicate_node);

	while (duplicate_node && temporary_node)
	{
		if (temporary_node->n == duplicate_node->n)
		{
			duplicate_node = duplicate_node->next;
			temporary_node = temporary_node->next;
		}
		else
		{
			return 0;
		}
	}

	if (duplicate_node == NULL)
		return 1;

	return 0;
}
