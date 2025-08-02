# I just realized that this is better version than `ctype`
from cffi import FFI

# Obtain an FFI handle
our_ffi_handle = FFI()

# Load the library
# rename the path here to match output of the C file
# Linux, extension is .so
# Windows, extension is .dll
path_to_our_shared_library = "./libadd.so"
the_library = our_ffi_handle.dlopen(path_to_our_shared_library)

# Teach our FFI handle what to expect from the library
our_ffi_handle.cdef("""
   // This has to be valid C code, unfortunately.
   // So don't put garbage here
   int addition(int a, int b);     
""")

# Hopefully, no bad happened above.
# Put the new definition to use; it's really inside `our_ffi_handle` btw
addition = the_library.addition # It's now a Python function

# What's up ?
assert(69 == addition(35, 34))
print("Yup, it works!")
