## [jq cookbook](https://remysharp.com/drafts/jq-recipes)

### Push on to an existing array (where source is [1, 2, 3]):

```
. + [ 4 ]
```
result: [ 1, 2, 3, 4 ]

### Convert object to array, moving the key into the array item under the property slug:

```
to_entries | map_values(.value + { slug: .key })
```

### Convert an array to a keyed object (the inverse of the above example):

```
map({ (.slug): . }) | add
```

### Swap the key/value pair to read as value/key object:

```
to_entries | map( {(.value) : .key } ) | add
```

### Read a plain list of strings from a file into an array, specifically splitting into an array and removing the last empty \n:

```
echo "1\n2\n3" | jq --slurp --raw-input 'split("\n")[:-1]'
```

### Convert a plain list of timestamps to an array of objects with date and time separated (using jq's --slurp and --raw-input options combined):

```
cat timestamps.txt | jq --slurp --raw-input 'split("\n")[:-1] | map({
    date: (. | strptime("%a, %d %b %Y %H:%M:%S") | todate[0:10]),
    time: (. | strptime("%a, %d %b %Y %H:%M:%S") | todate[11:19])
})'
```

### From a plain list of timestamps, count the occurrences of unique days (the first part is from the example above):

```
split("\n")[:-1] | map({
  date: (. | strptime("%a, %d %b %Y %H:%M:%S") | todate[0:10]),
  time: (. | strptime("%a, %d %b %Y %H:%M:%S") | todate[11:19])
}) | reduce .[] as $item (
  {}; # initial value
  .[$item.date] += 1 # reducer
)
```

### Take an object with two similar objects, but separated between team and formerly, and merge into a single object, adding a flag for all those from the formerly group:

```
[.team, (.formerly | map(. + {formerly: true }))] | flatten
```

### Download and extract all the files from a gist:

```
eval "$(
  curl https://api.github.com/gists/968b8937a153127cfae4a173b6000c1e |
  jq -r '
    .files |
    to_entries |
    .[].value |
    @sh "echo \(.content) > \(.filename)"
  '
)"
```

### Update all outdated npm dependencies:

```
npm i $(echo $(npm outdated --json | jq -r 'to_entries | .[] | "\(.key)@\(.value.latest)"'))
```

### Install the dependencies from one node project to another:

```
npm i $(cat ../other-project/package.json| jq '.dependencies | keys[]' -r)
```

### Add a new property to every object:

```
map(. + { "draft": true })
```
Or
```
[.[] | . + { "draft" : true }]
```

### Add new property to every object in a nested object, i.e. source looks like:

```json
{
 "offline-panel": {
    "title": "Offline Panel",
    "tags": [
      "web"
    ]
  },
  "rewrite-it": {
    "title": "Let's just rewrite it",
    "tags": [
      "business"
    ]
  }
}
```

Command:
```
with_entries(.value += { "draft": true})
```

### Remove a property from a nested object (example as above):

```
with_entries(.value |= del(.title))
```

### List all the dependencies in a package.json for use in other commands, like npm uninstall:

```
echo $(cat package.json | jq '.dependencies | keys | .[] | "\(.)"' -r)
```

### Get mongodb data into jq compatible format:

```
mongo / --norc --username  --password  \
  --eval 'printjson(db.getCollection("users").find().toArray())' | \
  jq '.[]'
```

### From Twitter's API, take all DM received and sent and transform into readable format sorted by date order:

```
[ .[] | {
  text,
  date: .created_at,
  from: { screen_name: .sender.screen_name },
  to: { screen_name: .recipient.screen_name}
} ] |
sort_by(.date)
```

### Using Serverless and Next.js and working out which dependencies I need to force include (because they live in the .next directory):

```
depcheck --json |
  jq '
    .using |
    [
      to_entries[] |
      select(.value[] | contains("/.next/")) |
      .key
    ] |
    unique |
    sort[] | "- \(.)"
  ' -r
```
Note: also uses depcheck to resolve the npm dependencies.

### From a nested tree of objects, find the object whose id matches X:

```
curl -sL https://git.io/vxPyi | \
  jq '.. | objects | select(.id == "0:16")'
```

### Strip all occurrences of a property (email in this example):

```
walk(if type == "object" then . | del(.email) else . end)
Note that the walk function is missing from jq@1.5 and needs to be added (seen in demo).
```

### Bulk insert into elastic search using a vanilla JSON array, i.e. [1,2,3,4] - zipping the array with the required elastic search metadata:

```
cat data.json | \
  jq 'reduce .[] as $n ([]; . + [{ "index" : { "_index": "my-index", "_type" : "my-type" } }, $n]) | .[]' -c | \
  curl -H "Content-Type: application/x-ndjson" -XPOST http://localhost:9200/_bulk --data-binary "@-"
```

### Filter an array, similar to a JavaScript array filter:

```
def filter(cond): map(select(cond));

filter(. > 2)
```
### Converting a text output of columns and converting to a JSON object. In this case, running Zeit's now ls | jq --raw-input --slurp to find out how many running instance I have:

```
split("\n")[1:-3] | # split into an array of strings, removing the 1st and last few blank lines
map([ split(" ")[] | select(. != "") ]) | # convert large spaces into individual colmns
map({ # map into a usable object
  app: .[0],
  url: .[1],
  number: (if (.[2] == "-") then .[2] else .[2] | tonumber end),
  type: .[3],
  state: .[4],
  age: .[5]
}) |
# now I can query the result - in this case: how many running and are npm
map(select(.number > 0 and .type == "NPM")) | length
```

### Find duplicates in an array based on a key:

```
[
  reduce .[].id as $item (
    {}; # initial value
    .[$item] += 1
  ) | to_entries[] | select(.value > 1)
] | from_entries
```

### Quickly convert a list of strings into an array (for JavaScript dev, etc):

```
pbpaste | jq -Rs 'split("\n")' | pbcopy
```
