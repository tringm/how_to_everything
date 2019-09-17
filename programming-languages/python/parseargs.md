

### Dictionary args (key value pair)
> NOTE: this only handle string value

[Source](https://gist.github.com/fralau/061a4f6c13251367ef1d9a9a99fb3e8d)
#### Standard declaration with argparse:
```python
import argparse
parser = argparse.ArgumentParser(description="...")
...
parser.add_argument("--set",
                        metavar="KEY=VALUE",
                        nargs='+',
                        help="Set a number of key-value pairs "
                             "(do not put spaces before or after the = sign). "
                             "If a value contains spaces, you should define "
                             "it with double quotes: "
                             'foo="this is a sentence". Note that '
                             "values are always treated as strings.")
args = parser.parse_args()
```

The argument is optional and multivalued, with a minimum of one occurrence (`nargs='+'`).

The result is a **list** of strings e.g. `["foo=hello", "bar=hello world", "baz=5"]` in `args.set`, which we now need to parse (note how the shell has processed and removed the quotes!).

#### Parsing the result

```Python
def parse_var(s):
    """
    Parse a key, value pair, separated by '='
    That's the reverse of ShellArgs.

    On the command line (argparse) a declaration will typically look like:
        foo=hello
    or
        foo="hello world"
    """
    items = s.split('=')
    key = items[0].strip() # we remove blanks around keys, as is logical
    if len(items) > 1:
        # rejoin the rest:
        value = '='.join(items[1:])
    return (key, value)


def parse_vars(items):
    """
    Parse a series of key-value pairs and return a dictionary
    """
    d = {}

    if items:
        for item in items:
            key, value = parse_var(item)
            d[key] = value
    return d

# parse the key-value pairs
values = parse_vars(args.set)
```

Now the variable `values`contains a dictionary with the key-value pairs defined on the command line:

    values = {'foo':'hello', 'bar':'hello world', 'baz':'5'}

### Nested layer of arg parse

[Source](https://chase-seibert.github.io/blog/2014/03/21/python-multilevel-argparse.html)

```Python
#!/usr/bin/env python

import argparse
import sys


class FakeGit(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Pretends to be git',
            usage='''git <command> [<args>]

The most commonly used git commands are:
   commit     Record changes to the repository
   fetch      Download objects and refs from another repository
''')
        parser.add_argument('command', help='Subcommand to run')
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def commit(self):
        parser = argparse.ArgumentParser(
            description='Record changes to the repository')
        # prefixing the argument with -- means it's optional
        parser.add_argument('--amend', action='store_true')
        # now that we're inside a subcommand, ignore the first
        # TWO argvs, ie the command (git) and the subcommand (commit)
        args = parser.parse_args(sys.argv[2:])
        print 'Running git commit, amend=%s' % args.amend

    def fetch(self):
        parser = argparse.ArgumentParser(
            description='Download objects and refs from another repository')
        # NOT prefixing the argument with -- means it's not optional
        parser.add_argument('repository')
        args = parser.parse_args(sys.argv[2:])
        print 'Running git fetch, repository=%s' % args.repository


if __name__ == '__main__':
    FakeGit()
```
