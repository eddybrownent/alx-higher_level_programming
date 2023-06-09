#include "Python.h"

/**
 * print_python_string - Prints information about Python strings
 *  @p: A PyObject string object
 */

void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");

	/* Check if the object's type is a string */
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	/* Get the length of the string */
	length = ((PyASCIIObject *)(p))->length;

	/* Check the string type and print information accordingly */
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");
	else
		printf(" type: compact unicode object\n");

	/* Print the length and value of the string */
	printf(" length: %ld\n", length);
	printf(" value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
