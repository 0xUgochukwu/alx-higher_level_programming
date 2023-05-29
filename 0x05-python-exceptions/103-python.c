#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to the PyObject list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to the PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);
	printf("  first %ld bytes: ", size > 10 ? 10 : size);

	for (i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf("%02x ", bytes[i] & 0xff);
	}

	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: Pointer to the PyObject float object
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);
	printf("  value: %f\n", value);
}

