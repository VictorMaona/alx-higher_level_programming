#include "lists.h"

/**
 * check_cycle - cycle detection functionality
 * @list: Check the connected list structure
 * Return: 0 list doesnt have cycle, 1 if does.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
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
