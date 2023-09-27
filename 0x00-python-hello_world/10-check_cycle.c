#include "lists.h"

/**
 * check_cycle - checks if linked list contains a cycle
 * @list: the list to check
 *
 * Return: 0 if the list does not have a cycle else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
