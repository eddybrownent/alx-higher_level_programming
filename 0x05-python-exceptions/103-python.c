#include <python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);


/**
 * print_python_list - prints basic info about python lists
 * @p: Pyobject list object
 */
void print_python_list(PyObject *p)
{
	/* variables to store the size and allocation of list */
	Py_ssize_t size, allocation, i;
	const char *type_name;

	/* Casting the PyObject to PyListObject and PyVarObject pointers */
	PyListObject *list_obj = (PyListObject *)p;
	PyvarObject *var_obj = (PyVarObject *)p;

	/* getting the size and allocation values */
	size = var_obj->ob_size;
	allocation = list_obj->Allocated;

	fflush(stdout);

	printf("[*] Python list info\n");

	/* check if the object is a list */
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocation);

	/* Iterating over each element of the list */
	for (i = 0; i < size; i++)
	{
		/* to get the name of the current element */
		type_name = list_obj->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type_name);

		/* printing additional info based on type of element*/
		if (strcmp(type_name, "bytes") == 0)
			print_python_bytes(list_obj->ob_item[i]);
		else if (strcmp(type_name, "float") == 0)
			print_python_float(list_obj->ob_item[i];
	}
}

/**
 * print_python_bytes - prints basic info about python byte objects
 * @p: A PyObject byte object
 *
 */
void print_python_bytes(PyObject *p)
{
	/* Variables to store the size and iterate over the bytes */
	Py_ssize_t size, i;
	PyBytesObject *bytes_obj = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");

	/* checking if the object is a bytes object */
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/* printing the size and trying the sting */
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes_obj->ob_sval);

	/* getting the number of bytes to display */
	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		/*printng the hexadecimal representation of each byte */
		printf("%02hhx", bytes_obj->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - prints basic info about python float objects
 *
 * @p: A PyObject float object
 *
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	/* Casting the PyObject to PyFloatObject pointer */
	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");

	/* Checking if the object is a float */
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	/* Converting the float value to a string representation */
	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", buffer);

	PyMem_Free(buffer);

}


