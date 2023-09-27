#include "lists.h"
/**
 * reverse_list - function to reverse a list
 * @head: pointer to the list
 *
 * Return: pointer to the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current = *head, *next, *previous = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
	return (*head);
}
/**
 * is_palindrome - function to check if list is palindrome
 * @head: the pointer to the string
 *
 * Return: 1 if string is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	second_half = reverse_list(&slow);
	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
			return (0);
		*head = (*head)->next;
		second_half = second_half->next;
	}

	reverse_list(&slow);
	return (1);
}
