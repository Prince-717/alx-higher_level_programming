#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints information about bytes
 *
 * @bytes_obj: Python Bytes Object
 * Return: no return
 */
void print_python_bytes(PyObject *bytes_obj)
{
	char *string;
	long int osize, j, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(bytes_obj))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	osize = ((PyVarObject *)(bytes_obj))->ob_size;
	string = ((PyBytesObject *)bytes_obj)->ob_sval;

	printf("  size: %ld\n", osize);
	printf("  trying string: %s\n", string);

	if (osize >= 10)
		limit = 10;
	else
		limit = osize + 1;

	printf("  first %ld bytes:", limit);

	for (j = 0; j < limit; j++)
		if (string[j] >= 0)
			printf(" %02x", string[j]);
		else
			printf(" %02x", 256 + string[j]);

	printf("\n");
}

/**
 * print_python_list - Print information on list
 *
 * @list_obj: Python List Object
 * Return: no return
 */
void print_python_list(PyObject *list_obj)
{
	long int osize, j;
	PyObject *element;
	PyListObject *list;

	osize = ((PyVarObject *)(list_obj))->ob_size;
	list = (PyListObject *)list_obj;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", osize);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (j = 0; j < osize; j++)
	{
		element = ((PyListObject *)list_obj)->ob_item[j];
		printf("Element %ld: %s\n", j, ((element)->ob_type)->tp_name);
		if (PyBytes_Check(element))
			print_python_bytes(element);
	}
}
