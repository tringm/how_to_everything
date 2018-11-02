# How to set up logging level

```
logging.VERBOSE = 5
logging.addLevelName(logging.VERBOSE, "VERBOSE")
logging.Logger.verbose = lambda inst, msg, *args, **kwargs: inst.log(logging.VERBOSE, msg, *args, **kwargs)
logging.LoggerAdapter.verbose = lambda inst, msg, *args, **kwargs: inst.log(logging.VERBOSE, msg, *args, **kwargs)
logging.verbose = lambda msg, *args, **kwargs: logging.log logging.VERBOSE, msg, *args, **kwargs)
```