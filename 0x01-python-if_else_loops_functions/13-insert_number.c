#include "lists.h"

/**
 * insert_node - insert int into a sorted linked list
 * @head: head pointer to the list
 * @number: into to be stored in the new_node
 *
 * Return: pointer to new_node or Null if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp_po, *new_node;
/*Set temp_po as the head of the linked list*/
	temp_po = *head;

/*Allocate memory for the new_node*/
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

/*Set the value of the new_node to the given number*/
	new_node->n = number;

/*Check if list is empty or new_node be insert at beginning*/
	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

/*Traverse the linked list to find the right postion for the new_node*/
	while (temp_po->next != NULL)
	{
		if ((temp_po->next)->n >= number)
		{
			new_node->next = temp_po->next;
			temp_po->next = new_node;
			return (new_node);
		}
		temp_po = temp_po->next;
	}

/*Insert the new_node at the end of the linked list */
	new_node->next = NULL;
	temp_po->next = new_node;
	return (new_node);
}
