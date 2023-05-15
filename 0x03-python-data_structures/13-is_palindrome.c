#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	/* Check if the list is empty */
	if (*head == NULL)
	{
		return (1);
	}

	/* Create a pointer to the middle node of the list */
	listint_t *middle = *head;

	while (middle->next != NULL && middle->next->next != NULL)
	{
		middle = middle->next->next;
	}
	/* Reverse the second half of the list */
	listint_t *prev = NULL;
	listint_t *curr = middle->next;
	listint_t *next;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	/* Compare the first half of the list to the reversed second half */
	listint_t *first = *head;

	while (first != NULL && prev != NULL)
	{
		if (first->n != prev->n)
		{
			return (0);
		}
		first = first->next;
		prev = prev->next;
	}
	/* The list is a palindrome */
	return (1);
}

