## Overpass API

### List all countries name

Return in csv format to define a specific tags
Return in json format for full tags (***verbose***)

```
[out:csv(
  "ISO3166-1", "name:en";true; ","
)];
(
relation["type"="boundary"]["boundary"="administrative"]["admin_level"="2"];
relation["type"="land_area"]["admin_level"="2"];
);
out;
```

### Get country by name:

```
[out:json];
node[place=country]["name:en"="Finland"];
out;
```

### Get cities by country:
```
[out:json];
area
	["name:en"="insert_country_name"];
node
	[place=city];

out;
```
