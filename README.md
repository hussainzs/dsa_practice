Make sure you run the files with the `-m` tag; otherwise, the root directory path isn't added to `sys.path`, and a "module not found" error is thrown in imports.

Example: `python -m templates.binarySearch`