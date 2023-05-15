#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	return is_palindrome_helper(head, *head);
}

/**
 * is_palindrome_helper - helper function for palindrome check
 * @left: pointer to pointer to the left node
 * @right: pointer to the right node
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome_helper(listint_t **left, listint_t *right)
{
	int is_palindrome;

	if (right == NULL)
		return (1);

	is_palindrome = is_palindrome_helper(left, right->next);

	if (!is_palindrome)
		return (0);

	is_palindrome = ((*left)->n == right->n);

	*left = (*left)->next;

	return (is_palindrome);
}
