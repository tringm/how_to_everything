### Python package manger pipenv
1.  Sources:
    -   <https://docs.python-guide.org/dev/virtualenvs/>
2.  Install pipenv
    ```
    $ pip install --user pipenv
    ```

    This does a user installation to prevent breaking any system-wide packages. If pipenv isn’t available in your shell after installation, you’ll need to add the user base’s binary directory to your PATH.
    * Finding user base binary directory
        ```
        python -m site --user-base
        ```
        E.g: ```/home/tri/.local```.
    * Add ```/bin``` to the end, and add it to PATH.
        ```
        vim ~/.bashrc
        ```
    add to .bashrc
        ```bash
        export PATH="$PATH/home/tri/.local/bin"
        source ~/.bashrc
        ```

1.  Installing packages
    -   Similar to pip:
        ```
        pipenv install packages
        ```
2.  [Adding pipenv to Pycharm Project](https://www.jetbrains.com/help/pycharm/pipenv.html)
    -   If pipenv not automatically found, point it to the executable file. E.g:`/home/tri/.local/bin/pipenv`

1. Install packages from test.pypi and dependencies:

  ```
  pip install -i https://test.pypi.org/simple/ aitoai --no-deps
  pip install aitoai
  ```
