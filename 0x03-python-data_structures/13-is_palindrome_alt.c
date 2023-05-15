#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *next = NULL;
	listint_t *second_half = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		second_half = slow->next;
	}
	else
	{
		second_half = slow;
	}

	prev->next = NULL;
	reverse_list(&second_half);

	is_palindrome = compare_lists(*head, second_half);

	reverse_list(&second_half);

	if (fast != NULL)
	{
		prev->next = slow;
		slow->next = second_half;
	}
	else
	{
		prev->next = second_half;
	}

	return (is_palindrome);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @list1: pointer to the head of the first list
 * @list2: pointer to the head of the second list
 * Return: 0 if lists are not equal, 1 if lists are equal
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	listint_t *temp1 = list1;
	listint_t *temp2 = list2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}

