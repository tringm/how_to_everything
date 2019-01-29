## Overpass API

***Generic format***:
```
[out:json];
area
    [name="insert_city_name"];
way(area)
    [name]
    [highway]
    [postal_code];
out;
```

* ```[out:json]```: output format
* ```[name]```: tag. If no value is defined => required tag




### Node by id

```
[out:json];
node
	(id:1314184532);
out;
```

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
    ["is_in:country"="insert_country_name"]
	[place=city];

out;
```

### Get streets by city:

```
[out:json];
area
    [name="insert_city_name"];
way(area)
    [name]
    [highway];
out;
```

Highway is for way type:
* residential: Road in a residential area
* service: Generally for access to a building, service station, beach, campsite, industrial estate, business park, etc.
* track:  Roads for agricultural and forestry use etc.
* unclassified: Public access road, non-residential.
* footway: For designated footpaths, i.e. mainly/exclusively for pedestrians.
* path: A generic multi-use path open to non-motorized vehicles.
* tertiary: A road linking small settlements, or the local centres of a large town or city.
* secondary: A highway linking large towns.
* crossing: Pedestrian crossing
* primary: A highway linking large towns.
* bus_stop: A bus stop is a place where public buses stop.
* turning_circle: A widened area of road that allows vehicles to turn more easily.
* traffic_signals: A traffic signal for regulating circulation.
* living_street: Road with very low speed limits and other pedestrian friendly traffic rules
* cycleway: For designated cycleways.
* street_lamp: A single pole with one or more lights to illuminate the street.
* trunk: Important roads that are not motorways.
* steps:For flights of steps on footways and paths.
* motorway: High capacity highways designed to safely carry fast motor traffic.
* motorway_link: The link roads (sliproads / ramps) leading to and from a motorway.
* pedestrian: Roads mainly / exclusively for pedestrians
* stop: Used to mark stop signs
* trunk_link: Driveways or descents of an expressway
