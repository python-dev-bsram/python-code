# Python CLI Commands

## 1. Running Python Scripts
- `python script.py`: Run a Python script.
- `python -m module`: Run a Python module as a script.
- `python -c "command"`: Execute Python commands directly from the command line.
- `python -i script.py`: Run the script and then enter interactive mode (useful for debugging).

## 2. Enable Interactive Mode and REPL(Read , Evaluate , Print and Loop)
- `python`: Start the interactive interpreter (REPL).
- `python -q`: Start the interpreter without printing the Python version and copyright information.

## 3. Get Version and Help Information
- `python --version` or `python -V`: Print the Python version.
- `python --help`: Display help information about Python options and commands.

## 4. Optimize and Bytecode
- `python -O script.py`: Run Python in optimized mode (removes assertions and optimizations).
- `python -OO script.py`: Run Python in extra optimized mode (also removes docstrings).
- `python -B script.py`: Prevent writing `.pyc` files on import.

## 5. Debugging Options
- `python -d script.py`: Debug output from the parser.
- `python -X showrefcount`: Show reference count at program exit (CPython only).
- `python -X tracemalloc`: Start the program with a trace of memory allocations (useful for debugging memory usage).
- `python -X faulthandler`: Enable the fault handler to print a traceback when a fatal error occurs.

## 6. Warnings Control
- `python -W options`:
  - `-W default`: Display all warnings (default behavior).
  - `-W ignore`: Ignore all warnings.
  - `-W error`: Turn warnings into errors.
  - `-W once`: Show each warning only once.
  - `-W module`: Show warnings only once per module.

## 7. Environment Variables
- `python -E script.py`: Ignore environment variables like `PYTHONPATH`.
- `python -s script.py`: Don’t add the user’s site-packages directory to `sys.path`.

## 8. Buffering and Encoding
- `python -u script.py`: Force the `stdout` and `stderr` streams to be unbuffered.
- `python -b script.py`: Issue warnings about `str/bytes` comparisons.
- `python -X utf8`: Use UTF-8 mode regardless of the locale setting.

## 9. Module Access and Package Management
- `python -m venv myenv`: Create a virtual environment.
- `python -m pip install package_name`: Install packages using pip.
- `python -m unittest`: Run the Python `unittest` module for testing.

## 10. Profiling and Timing
- `python -m timeit "code"`: Measure execution time of small code snippets.
- `python -m cProfile script.py`: Run a script and profile its performance.

## 11. Isolation and Site Modules
- `python -I script.py`: Run Python in isolated mode, ignoring environment variables and user-installed packages.
- `python -S script.py`: Don’t import the `site` module on startup.

## 12. Command Line Inspection
- `python -m pydoc topic`: Display the documentation for a module, function, class, or keyword.
- `python -m dis script.py`: Disassemble Python bytecode into a readable format.

## 13. Create Virtual Environments
- `python -m venv nameofvenv`: create virtual environments for Isolation of python application
- `source venv/bin/activate` : Activate the create virtual environment and then install the library(linux/mac os)
- `python freeze > requirements.txt`: Store python dependencies in one file.
- `pip install -m requirements.txt` : Install the file dependencies in some another instances.
