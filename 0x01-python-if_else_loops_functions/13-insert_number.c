#include "lists.h"

/**
 * insert_node - insert a node into a sorted singly linked list.
 * @head: head node
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *list = *(head);

	if (head == NULL || new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (list)
	{
		if (list->next == NULL || list->next->n > number)
		{
			new->next = list->next;
			list->next = new;
			return (new);
		}
		list = list->next;
	}

	return (NULL);
}

