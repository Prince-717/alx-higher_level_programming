#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks for the occurence of a cycle in a singly-linked list.
 * @list: singly-linked list.
 *
 * Return: 0 if there is no cycle and -1 if there is.
 */
int check_cycle(listint_t *list)
{
	listint_t *veryslow;
	listint_t *veryfast;

	if (list == NULL || list->next == NULL)
		return (0);

	veryslow = list->next;
	veryfast = list->next->next;

	while (veryslow && veryfast && veryfast->next)
	{
		if (veryslow == veryfast)
			return (1);

		veryslow = veryslow->next;
		veryfast = veryfast->next->next;
	}

	return (0);
}
