#include "lists.h"

/**
* Check_cycle - checks if a inked list contain a cycle
* @list: linked list 
*
* Return: 1 if the list has a cycle 0 if it fail
*/

int check_cycle(listint_t *list)
{
	list_t *slw = list, *fst = list;
	
	if (!list)
	return (0);
	
	while(slw && fst && fst->next)
	{
		slw = slw->next;
		fst = fst->next->next;
		if (slw == fst)
		return (1);
	}

	return (0);
}
