#include "Python.h"
/**
 * print_python_list_info - Print list python
 * @p: Python object
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	int i, count;
	PyListObject *l = (PyListObject *) p;

	count = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", count);
	printf("[*] Allocated = %ld\n", l->allocated);

	for (i = 0 ; i < count ; i++)
	{
		printf("Element %d: %s\n", i, (PyList_GET_ITEM(l, i))->ob_type->tp_name);
	}
}
