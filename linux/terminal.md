## Find everything recursively in children folder and cp (or rm)
```
find ./MyFolder -name "*.pdf" -type f -exec cp {} ./ \;
```
```
find _folderToLookInto_ -name "_fileType_" -type f -exec _command_ {} _folderToPutAllFiles_ \;
```

## Viewing/Searching

### Search for all occurence and include the line number (-n return line number, -r recursively traverse the folder)

```
grep -nr <search-term> README.md
```

### Print a specific line
```sed -n 5p README.md``` => Print line 5
```sed -n 2,3p README.md```=> print line 2 to 3
