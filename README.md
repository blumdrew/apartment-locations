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

Complete data is below:

Neighborhood	Apartment Major Road Percent	House Major Road Percent	Difference
lents	25.5%	12.9%	13%
roseway	42.6%	3.7%	39%
cully	35.9%	10.7%	25%
irvington	20.6%	21.4%	-1%
sabin	30.6%	16.6%	14%
king	37.8%	15.6%	22%
eliot	24.7%	10.6%	14%
grant park	15.4%	13.7%	2%
alameda	55.6%	14.2%	41%
concordia	43.5%	14.1%	29%
beaumont-wilshire	76.9%	13.3%	64%
rose city park	28.1%	10.9%	17%
hollywood	60.9%	26.7%	34%
sullivan's gulch	28.0%	16.8%	11%
laurelhurst	0.0%	19.6%	-20%
kerns	18.5%	12.1%	6%
lloyd district	87.5%	0.0%	88%
old town	65.5%	0.0%	66%
boise	28.2%	18.7%	9%
overlook	50.0%	8.1%	42%
pearl district	80.0%	100.0%	-20%
humboldt	37.5%	23.2%	14%
piedmont	68.1%	14.1%	54%
woodlawn	24.1%	12.7%	11%
vernon	35.6%	19.4%	16%
sunderland	0.0%	51.6%	-52%
sumner	21.4%	12.2%	9%
arbor lodge	42.9%	16.1%	27%
kenton	47.6%	13.0%	35%
east columbia	42.9%	9.2%	34%
north tabor	42.1%	18.9%	23%
madison south	26.4%	13.1%	13%
parkrose	29.3%	25.0%	4%
parkrose heights	32.1%	13.7%	18%
woodland park	0.0%	23.8%	-24%
hazelwood	27.9%	13.4%	14%
montavilla	21.0%	8.7%	12%
hayden island	0.0%	0.0%	0%
bridgeton	16.7%	34.5%	-18%
sunnyside	30.8%	10.7%	20%
buckman	26.6%	19.1%	8%
mount tabor	48.8%	12.7%	36%
argay terrace	21.0%	14.9%	6%
russell	12.5%	11.9%	1%
wilkes	20.1%	7.1%	13%
glenfair	36.7%	17.7%	19%
centennial	27.5%	11.5%	16%
south tabor	27.6%	5.7%	22%
downtown	88.2%	100.0%	-12%
hosford-abernethy	36.8%	1.8%	35%
richmond	28.6%	7.5%	21%
mill park	21.5%	12.3%	9%
south portland	34.1%	20.8%	13%
brooklyn	10.3%	9.2%	1%
creston-kenilworth	15.9%	9.2%	7%
foster-powell	16.0%	9.6%	6%
powellhurst-gilbert	19.2%	13.7%	5%
pleasant valley	21.4%	13.0%	8%
mount scott-arleta	46.6%	14.0%	33%
reed	24.1%	17.2%	7%
woodstock	57.0%	13.5%	43%
sellwood-moreland	33.4%	12.6%	21%
eastmoreland	33.3%	5.9%	27%
ardenwald	66.7%	26.6%	40%
brentwood-darlington	19.6%	14.3%	5%
university park	22.6%	13.8%	9%
northwest district	40.1%	21.6%	18%
portsmouth	20.6%	15.6%	5%
saint johns	33.1%	11.6%	21%
linnton	66.7%	19.5%	47%
cathedral park	26.0%	11.5%	14%
forest park	0.0%	21.0%	-21%
hillside	17.2%	7.5%	10%
arlington heights	0.0%	36.4%	-36%
goose hollow	37.7%	28.6%	9%
sylvan-highlands	0.0%	18.0%	-18%
northwest heights	26.7%	9.3%	17%
southwest hills	39.2%	21.6%	18%
homestead	9.8%	20.0%	-10%
healy heights	0.0%	21.7%	-22%
hillsdale	27.3%	15.3%	12%
bridlemile	2.6%	12.8%	-10%
hayhurst	26.1%	15.7%	10%
multnomah	42.9%	30.4%	12%
maplewood	37.5%	13.1%	24%
south burlingame	66.7%	4.7%	62%
ashcreek	30.0%	9.8%	20%
crestwood	60.0%	11.1%	49%
west portland park	9.5%	17.0%	-7%
markham	45.5%	11.1%	34%
far southwest	100.0%	21.7%	78%
collins view	85.7%	19.6%	66%
marshall park	0.0%	8.7%	-9%
arnold creek	100.0%	12.9%	87%
northwest industrial	0.0%	0.0%	0%