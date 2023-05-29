#include <Python.h>

/**
 * python_list_print - Prints basic info about Python lists.
 *
 * @ptr_pyobject: A PyObject list object.
 */
void python_list_print(PyObject *ptr_pyobject)
{
	Py_ssize_t span, mem_alloc, index;
	const char *type;
	PyListObject *list = (PyListObject *)ptr_pyobject;
	PyVarObject *var = (PyVarObject *)ptr_pyobject;

	span = var->ob_size;
	mem_alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(ptr_pyobject->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", span);
	printf("[*] Allocated = %ld\n", mem_alloc);

	index = 0;
	while (index < span)
	{
		type = list->ob_item[index]->ob_type->tp_name;
		printf("Element %ld: %s\n", index, type);
		if (strcmp(type, "bytes") == 0)
			python_bytes_print(list->ob_item[index]);
		else if (strcmp(type, "float") == 0)
			python_float_print(list->ob_item[index]);

		index++;
	}
}

/**
 * python_bytes_print - Prints basic info about Python byte objects.
 * @ptr_pyobject: A PyObject byte object.
 */
void python_bytes_print(PyObject *ptr_pyobject)
{
	Py_ssize_t span, index;
	PyBytesObject *bytes = (PyBytesObject *)ptr_pyobject;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(ptr_pyobject->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  span: %ld\n", ((PyVarObject *)ptr_pyobject)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)ptr_pyobject)->ob_size >= 10)
		span = 10;
	else
		span = ((PyVarObject *)ptr_pyobject)->ob_size + 1;

	printf("  first %ld bytes: ", span);

	index = 0;
	while (index < span)
	{
		printf("%02hhx", bytes->ob_sval[index]);
		if (index == (span - 1))
			printf("\n");
		else
			printf(" ");

		index++;
	}
}

/**
 * python_float_print - Prints basic info about Python float objects.
 * @ptr_pyobject: A PyObject float object.
 */
void python_float_print(PyObject *ptr_pyobject)
{
	char *mem_buff = NULL;

	PyFloatObject *object_float = (PyFloatObject *)ptr_pyobject;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(ptr_pyobject->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	mem_buff = PyOS_double_to_string(object_float->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", mem_buff);
	PyMem_Free(mem_buff);
}
