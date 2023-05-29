#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t dimension, mem_alloc, index;
	const char *kind;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	dimension = var->object_size;
	mem_alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", dimension);
	printf("[*] Allocated = %ld\n", mem_alloc);

	for (index = 0; index < dimension; index++)
	{
		kind = list->ob_item[index]->ob_type->tp_name;
		printf("Element %ld: %s\n", index, kind);
		if (strcmp(kind, "bytes") == 0)
			print_python_bytes(list->ob_item[index]);
		else if (strcmp(kind, "float") == 0)
			print_python_float(list->ob_item[index]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t dimension, index;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  dimension: %ld\n", ((PyVarObject *)p)->object_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->object_size >= 10)
		dimension = 10;
	else
		dimension = ((PyVarObject *)p)->object_size + 1;

	printf("  first %ld bytes: ", dimension);
	for (index = 0; index < dimension; index++)
	{
		printf("%02hhx", bytes->ob_sval[index]);
		if (index == (dimension - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *mem_buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	mem_buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", mem_buffer);
	PyMem_Free(mem_buffer);
}
