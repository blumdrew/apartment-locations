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

| Neighborhood         | Apartment Major Road Percent | House Major Road Percent | Total Apartments | Total Houses | Difference |
|----------------------|------------------------------|--------------------------|------------------|--------------|------------|
| lloyd district       | 87.5%                        | 0.0%                     | 8                | 19           | 87.5%      |
| arnold creek         | 100.0%                       | 12.9%                    | 1                | 1084         | 87.1%      |
| far southwest        | 100.0%                       | 21.7%                    | 1                | 471          | 78.3%      |
| collins view         | 85.7%                        | 19.6%                    | 7                | 755          | 66.1%      |
| old town             | 65.5%                        | 0.0%                     | 29               | 0            | 65.5%      |
| beaumont-wilshire    | 76.9%                        | 13.3%                    | 13               | 2203         | 63.7%      |
| south burlingame     | 66.7%                        | 4.7%                     | 3                | 578          | 62.0%      |
| piedmont             | 68.1%                        | 14.1%                    | 94               | 2153         | 54.0%      |
| crestwood            | 60.0%                        | 11.1%                    | 15               | 859          | 48.9%      |
| linnton              | 66.7%                        | 19.5%                    | 15               | 210          | 47.1%      |
| woodstock            | 57.0%                        | 13.5%                    | 107              | 3383         | 43.5%      |
| overlook             | 50.0%                        | 8.1%                     | 102              | 1933         | 41.9%      |
| alameda              | 55.6%                        | 14.2%                    | 9                | 1985         | 41.4%      |
| ardenwald            | 66.7%                        | 26.6%                    | 3                | 203          | 40.1%      |
| roseway              | 42.6%                        | 3.7%                     | 61               | 2582         | 38.9%      |
| mount tabor          | 48.8%                        | 12.7%                    | 207              | 3181         | 36.1%      |
| hosford-abernethy    | 36.8%                        | 1.8%                     | 234              | 11508        | 35.0%      |
| kenton               | 47.6%                        | 13.0%                    | 63               | 2548         | 34.6%      |
| markham              | 45.5%                        | 11.1%                    | 11               | 910          | 34.4%      |
| hollywood            | 60.9%                        | 26.7%                    | 23               | 236          | 34.2%      |
| east columbia        | 42.9%                        | 9.2%                     | 7                | 489          | 33.7%      |
| mount scott-arleta   | 46.6%                        | 14.0%                    | 146              | 2421         | 32.6%      |
| concordia            | 43.5%                        | 14.1%                    | 115              | 3317         | 29.4%      |
| eastmoreland         | 33.3%                        | 5.9%                     | 3                | 1586         | 27.5%      |
| arbor lodge          | 42.9%                        | 16.1%                    | 70               | 2377         | 26.8%      |
| cully                | 35.9%                        | 10.7%                    | 181              | 3149         | 25.2%      |
| maplewood            | 37.5%                        | 13.1%                    | 8                | 849          | 24.4%      |
| north tabor          | 42.1%                        | 18.9%                    | 202              | 1129         | 23.2%      |
| king                 | 37.8%                        | 15.6%                    | 135              | 1612         | 22.2%      |
| south tabor          | 27.6%                        | 5.7%                     | 156              | 1889         | 21.8%      |
| saint johns          | 33.1%                        | 11.6%                    | 281              | 3315         | 21.5%      |
| richmond             | 28.6%                        | 7.5%                     | 339              | 3663         | 21.1%      |
| sellwood-moreland    | 33.4%                        | 12.6%                    | 389              | 2952         | 20.8%      |
| ashcreek             | 30.0%                        | 9.8%                     | 60               | 1422         | 20.2%      |
| sunnyside            | 30.8%                        | 10.7%                    | 402              | 1457         | 20.1%      |
| glenfair             | 36.7%                        | 17.7%                    | 98               | 368          | 19.1%      |
| northwest district   | 40.1%                        | 21.6%                    | 489              | 1167         | 18.5%      |
| parkrose heights     | 32.1%                        | 13.7%                    | 53               | 1759         | 18.4%      |
| southwest hills      | 39.2%                        | 21.6%                    | 51               | 2193         | 17.6%      |
| northwest heights    | 26.7%                        | 9.3%                     | 30               | 1502         | 17.3%      |
| rose city park       | 28.1%                        | 10.9%                    | 121              | 3225         | 17.2%      |
| vernon               | 35.6%                        | 19.4%                    | 73               | 790          | 16.2%      |
| centennial           | 27.5%                        | 11.5%                    | 374              | 5499         | 16.0%      |
| hazelwood            | 27.9%                        | 13.4%                    | 470              | 4557         | 14.5%      |
| cathedral park       | 26.0%                        | 11.5%                    | 104              | 905          | 14.5%      |
| humboldt             | 37.5%                        | 23.2%                    | 168              | 1059         | 14.3%      |
| eliot                | 24.7%                        | 10.6%                    | 85               | 443          | 14.1%      |
| sabin                | 30.6%                        | 16.6%                    | 49               | 1527         | 14.0%      |
| madison south        | 26.4%                        | 13.1%                    | 129              | 1773         | 13.3%      |
| south portland       | 34.1%                        | 20.8%                    | 88               | 24           | 13.3%      |
| wilkes               | 20.1%                        | 7.1%                     | 199              | 2382         | 13.0%      |
| lents                | 25.5%                        | 12.9%                    | 369              | 4971         | 12.6%      |
| multnomah            | 42.9%                        | 30.4%                    | 49               | 601          | 12.4%      |
| montavilla           | 21.0%                        | 8.7%                     | 390              | 4624         | 12.3%      |
| hillsdale            | 27.3%                        | 15.3%                    | 22               | 124          | 12.0%      |
| woodlawn             | 24.1%                        | 12.7%                    | 54               | 1672         | 11.3%      |
| sullivan's gulch     | 28.0%                        | 16.8%                    | 125              | 179          | 11.2%      |
| hayhurst             | 26.1%                        | 15.7%                    | 23               | 966          | 10.4%      |
| hillside             | 17.2%                        | 7.5%                     | 29               | 710          | 9.8%       |
| boise                | 28.2%                        | 18.7%                    | 142              | 743          | 9.5%       |
| mill park            | 21.5%                        | 12.3%                    | 130              | 1674         | 9.2%       |
| sumner               | 21.4%                        | 12.2%                    | 14               | 776          | 9.2%       |
| goose hollow         | 37.7%                        | 28.6%                    | 151              | 185          | 9.1%       |
| university park      | 22.6%                        | 13.8%                    | 53               | 1656         | 8.9%       |
| pleasant valley      | 21.4%                        | 13.0%                    | 98               | 2752         | 8.5%       |
| buckman              | 26.6%                        | 19.1%                    | 636              | 782          | 7.5%       |
| reed                 | 24.1%                        | 17.2%                    | 141              | 775          | 7.0%       |
| creston-kenilworth   | 15.9%                        | 9.2%                     | 378              | 1697         | 6.7%       |
| foster-powell        | 16.0%                        | 9.6%                     | 119              | 2360         | 6.4%       |
| kerns                | 18.5%                        | 12.1%                    | 168              | 355          | 6.3%       |
| argay terrace        | 21.0%                        | 14.9%                    | 162              | 1290         | 6.1%       |
| powellhurst-gilbert  | 19.2%                        | 13.7%                    | 475              | 5696         | 5.4%       |
| brentwood-darlington | 19.6%                        | 14.3%                    | 102              | 4203         | 5.3%       |
| portsmouth           | 20.6%                        | 15.6%                    | 136              | 2068         | 5.0%       |
| parkrose             | 29.3%                        | 25.0%                    | 133              | 1203         | 4.3%       |
| grant park           | 15.4%                        | 13.7%                    | 13               | 1446         | 1.7%       |
| brooklyn             | 10.3%                        | 9.2%                     | 224              | 793          | 1.1%       |
| russell              | 12.5%                        | 11.9%                    | 8                | 1189         | 0.6%       |
| hayden island        | 0.0%                         | 0.0%                     | 10               | 54           | 0.0%       |
| northwest industrial | 0.0%                         | 0.0%                     | 0                | 0            | 0.0%       |
| irvington            | 20.6%                        | 21.4%                    | 252              | 2112         | -0.7%      |
| west portland park   | 9.5%                         | 17.0%                    | 21               | 894          | -7.5%      |
| marshall park        | 0.0%                         | 8.7%                     | 5                | 586          | -8.7%      |
| homestead            | 9.8%                         | 20.0%                    | 61               | 60           | -10.2%     |
| bridlemile           | 2.6%                         | 12.8%                    | 39               | 1337         | -10.2%     |
| downtown             | 88.2%                        | 100.0%                   | 76               | 3            | -11.8%     |
| bridgeton            | 16.7%                        | 34.5%                    | 6                | 55           | -17.9%     |
| sylvan-highlands     | 0.0%                         | 18.0%                    | 12               | 422          | -18.0%     |
| laurelhurst          | 0.0%                         | 19.6%                    | 8                | 1375         | -19.6%     |
| pearl district       | 80.0%                        | 100.0%                   | 40               | 2            | -20.0%     |
| forest park          | 0.0%                         | 21.0%                    | 0                | 462          | -21.0%     |
| healy heights        | 0.0%                         | 21.7%                    | 0                | 46           | -21.7%     |
| woodland park        | 0.0%                         | 23.8%                    | 0                | 101          | -23.8%     |
| arlington heights    | 0.0%                         | 36.4%                    | 0                | 294          | -36.4%     |
| sunderland           | 0.0%                         | 51.6%                    | 0                | 31           | -51.6%     |

