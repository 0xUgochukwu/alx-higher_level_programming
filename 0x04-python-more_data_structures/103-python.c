#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to the Python bytes object
 *
 * Return: None
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes: ", (size > 10) ? 10 : size);

	for (i = 0; i < ((size > 10) ? 10 : size); i++)
		printf("%02hhx ", str[i]);

	printf("\n");
}

/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to the Python list object
 *
 * Return: None
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;

	printf("[*] Python list info\n");
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

