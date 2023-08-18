# apartment-locations
Apartments Near Major Roads

Investigation on how apartment dwellers are forced into undesirable living situations along major roads in Portland, Oregon

Primary tool is the Overpass API tool that hits OpenStreetMap.

In general, every part of Portland is guilty of this, despite the online chatter. Portland gets a lot of credit in urbanist circles for inclusionary zoning, and to be fair it is broadly better than typical US cities. But the end result for the lions share of apartment dwellers is still living on busy roads.

In Portland, an apartment is more than twice as likely to be on a major road (as defined by a functional classification of tertiary, secondary, primary, trunk, or motorway in OpenStreetMap) than a detached house is - with 30% of apartments being directly on those roads, compared to 12% of detached houses. And anyone who is familiar with neighborhood politics knows that this is relatively unlikely to change. Most homeowners tend to view this as perfectly natural, despite the known health and safety risks associated with living on busy roads.

![Zoning Map of Central SE Portland](https://cityhikes.files.wordpress.com/2023/08/screen-shot-2023-08-18-at-7.57.33-am.png)
This zoning map of the central part of Southeast Portland illustrates this. The darker horizontal bands correspond to (from top to bottom) Belmont, Hawthorne, and Division - all roads that see far higher traffic volumes than their parrallel neighborhood streets. Them, along with Cesar Chavez (the darker vertical band) move almost all of the motor vehicle traffic through the area. The darker orange, pink, and light blue corresponds to "apartments allowed" zoning, while the light yellow indicated detached houses.

![Difference In Rate Of Apartments on major roads and detached houses on major roads by neighborhood](https://cityhikes.files.wordpress.com/2023/08/apt-house-difference-major-road-percent.png)
This map, created from the code in this repo, shows that almost all Portland neighborhoods have a higher proportion of apartments on major roads than houses. All of the exceptions come from neighborhoods that have either no detached houses, no apartments, or both. For example, Laurelhurst is the light blue neighborhood almost directly in the center. It has a total of 8 apartments, versus 1,343 detached houses. And the Pearl and Downtown (the center left light blue areas) have a total of 5 detached houses between them versus 120 or so apartments. Northwest Industrial and Forest Park also have no apartments.


For reference, see below for a map of Portland neighborhoods
![Portland](http://www.mappery.com/maps/Portland-Neighborhood-Map.jpg)
