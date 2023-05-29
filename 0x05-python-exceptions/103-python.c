#include <stdio.h>
#include <Python.h>

/**
 * display_python_bytes - Prints bytes information
 *
 * @pointer: Python Object
 * Return: no return
 */
void display_python_bytes(PyObject *pointer)
{
	char *ptr_string;
	long int dimension, index, threshold;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(pointer))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	dimension = ((PyVarObject *)(pointer))->ob_size;
	ptr_string = ((PyBytesObject *)pointer)->ob_sval;

	printf("  dimension: %ld\n", dimension);
	printf("  trying ptr_string: %s\n", ptr_string);

	if (dimension >= 10)
		threshold = 10;
	else
		threshold = dimension + 1;

	printf("  first %ld bytes:", threshold);

	index = 0;
	while (index < threshold)
	{
		if (ptr_string[index] >= 0)
			printf(" %02x", ptr_string[index]);
		else
			printf(" %02x", 256 + ptr_string[index]);
		index++
	}

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * display_python_float - Prints float information
 *
 * @pointer: Python Object
 * Return: no return
 */
void display_python_float(PyObject *pointer)
{
	double value;
	char *ptr_nf;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(pointer))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	value = ((PyFloatObject *)(pointer))->ob_fval;
	ptr_nf = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", ptr_nf);
	setbuf(stdout, NULL);
}

/**
 * display_python_list - Prints ptr_list information
 *
 * @pointer: Python Object
 * Return: no return
 */
void display_python_list(PyObject *pointer)
{
	long int dimension, index;
	PyListObject *ptr_list;
	PyObject *ptr_obj;

	setbuf(stdout, NULL);
	printf("[*] Python ptr_list info\n");

	if (!PyList_Check(pointer))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	dimension = ((PyVarObject *)(pointer))->ob_size;
	ptr_list = (PyListObject *)pointer;

	printf("[*] Size of the Python List = %ld\n", dimension);
	printf("[*] Allocated = %ld\n", ptr_list->allocated);

	index = 0;
	while (index < dimension)
	{
		ptr_obj = ptr_list->ob_item[index];
		printf("Element %ld: %s\n", index, ((ptr_obj)->ob_type)->tp_name);

		if (PyBytes_Check(ptr_obj))
			display_python_bytes(ptr_obj);
		if (PyFloat_Check(ptr_obj))
			display_python_float(ptr_obj);
		
		index++;
	}
	setbuf(stdout, NULL);
}
