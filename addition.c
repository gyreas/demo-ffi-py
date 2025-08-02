// This standalone thing is known as a function prototype
// It lets you say a function exists (declare it) before the entire function itself
// It alse a data type, but don't worry about that for now
//
// The FFI handle from Python will need this (and maybe more others) to make sense of the
// library it loads
int addition(int a, int b);

int addition(int a, int b) {
	return a + b;
}

// Compile with `cc -shared -o lib<choose a name>.dll addition.c`
