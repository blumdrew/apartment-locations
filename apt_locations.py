"""Houses vs. Apartments on Major Roads"""

import geopandas as gpd
import pandas as pd
import os
import overpass
import osm2geojson
import time
import json
from typing import Sequence, Tuple

def fetch_neighborhood_data(
    city: str,
    state: str
) -> True:
    """Fetch neighborhoods from city on OSM"""
    out_path = os.path.join(
        os.path.dirname(__file__),
        "neighborhood names",
        f"Neighborhoods {city} {state}.geojson"
    )
    if os.path.isfile(out_path):
        return out_path
    os.makedirs(os.path.dirname(out_path),exist_ok=True)
    query = (
        'area[name~"^{0}$",i]->.state;\n'
        'area[name~"^{1}$",i]->.city;\n'
        'rel[admin_level=10](area.state)(area.city);\n'
        '(._;>;)'
    ).format(state.capitalize(), city.capitalize())
    print(query)
    op = overpass.API(timeout=300)
    xml_data = op.get(query, responseformat="xml")
    nhoods = osm2geojson.xml2geojson(xml_data)
    with open(out_path, 'w') as f:
        f.write(json.dumps(nhoods))
    return out_path

def fetch_housing_location_data(
    nhood: str,
    city: str,
    state: str,
    replace: bool = False,
    save: bool = True,
    run_query: bool = True,
    return_data: bool = True
) -> Sequence[gpd.GeoDataFrame]:
    """User overpass api to dynamically fetch and save data"""
    #nhood = nhood.capitalize()
    #city = city.capitalize()
    bp = os.path.dirname(__file__)
    out_path = os.path.join(bp, state.lower(), city.lower(), nhood.lower())
    if os.path.isdir(out_path) and not replace:
        print(f"Data for {nhood} nhood in city {city} already exists.")
        apt_all_pth = os.path.join(out_path,"apartments_all.geojson")
        apt_maj_pth = os.path.join(out_path,"apartments_major.geojson")
        house_all_pth = os.path.join(out_path,"houses_all.geojson")
        house_maj_pth = os.path.join(out_path,"houses_major.geojson")
        if all(
            os.path.isfile(os.path.join(out_path, pth)) for pth in 
            [apt_all_pth, apt_maj_pth, house_all_pth, house_maj_pth]
            ):
            if return_data:
                return (
                    gpd.read_file(apt_all_pth),
                    gpd.read_file(apt_maj_pth),
                    gpd.read_file(house_all_pth),
                    gpd.read_file(house_maj_pth)
                )
            else:
                return True
        else:
            print(f"Not all files found, generating new ones.")
    if not run_query:
        return None
    query_path = os.path.join(
        bp,
        "overpass queries"
    )
    queries_to_run = sorted(
        os.path.join(query_path, f) for f in os.listdir(query_path)
        if ".DS_Store" not in f
    )
    op = overpass.API(timeout=300)

    data = []
    print(f"Running queries for {nhood}, {city}, {state}")
    for q_idx, q in enumerate(queries_to_run):
        _retries = 3
        with open(q, 'r') as f:
            query = f.read()
            query = query.format(
                nhood,city,state
            )
        # TODO figure out how to pass a literal query in
        query = query.replace("out;","")
        query = query.replace("(._;>;);","(._;>;)")
        print(f"Running query {os.path.basename(q)}")
        _standard_result = True
        while _retries:
            try:
                gj = op.get(query, verbosity="geom")
                _standard_result = True
                break
            except overpass.errors.UnknownOverpassError:
                print(f"Failed to fetch geojson, trying xml. Sleeping 3 seconds.")
                time.sleep(3)
                gj = op.get(query, responseformat="xml", verbosity="geom")
                gj = osm2geojson.xml2geojson(gj)
                _standard_result = False
                if save:
                    pth = os.path.join(
                        out_path,
                        f"{os.path.basename(q).split('.')[0]}.geojson"
                    )
                    with open(pth, 'w') as f:
                        f.write(json.dumps(gj))
                break
            except Exception as e:
                print(f"Failed on try {4-_retries}")
                _retries -= 1
                if _retries:
                    print(f"Waiting 3 seconds and trying again")
                    time.sleep(3)
                else:
                    print(f"Exceeded max retries, raising error.")
                    raise
                continue
        gdf = gpd.GeoDataFrame(gj["features"])
        if not gdf.empty and _standard_result:
            gdf = gdf[gdf["geometry"].type == "LineString"]
        elif not _standard_result:
            pass
        else:
            gdf = gpd.GeoDataFrame(
                data=[(None, None, None, None)],
                columns=['type', 'id', 'properties', 'geometry']
            )
        if save and _standard_result:
            os.makedirs(out_path,exist_ok=True)
            print(f'Saving to: {out_path}')
            gdf.to_file(
                os.path.join(out_path,f"{os.path.basename(q).split('.')[0]}.geojson"),
                driver="GeoJSON"
            )
        data.append(gdf)
        print(f"Succesfully ran query {q}, returned {len(gdf.index)} results.")
        if q_idx != len(queries_to_run) - 1:
            print(f"Sleeping 3 seconds to avoid multiple request errors")
            time.sleep(3)
    if return_data:
        return data
    else:
        return True

def relative_major_percents(
    nhood: str = "buckman",
    city: str = "portland",
    state: str = "oregon"
) -> Tuple[float, float]:
    """quick and dirty lads"""
    bp = os.path.dirname(__file__)
    all_apts = gpd.read_file(
        os.path.join(bp,state,city,nhood,'apartments_all.geojson')
    )
    all_houses = gpd.read_file(
        os.path.join(bp,state,city,nhood,'houses_all.geojson')
    )
    maj_apts = gpd.read_file(
        os.path.join(bp,state,city,nhood,'apartments_major.geojson')
    )
    maj_houses = gpd.read_file(
        os.path.join(bp,state,city,nhood,'houses_major.geojson')
    )
    # pct of apartments on major roads
    try:
        all_apts = all_apts[
            all_apts["id"].str.startswith("way")
            | all_apts["id"].str.startswith("relation")
        ]
    except Exception:
        pass
    all_apts["on_major"] = all_apts["id"].isin(maj_apts["id"])
    try:
        all_apts["floors"] = pd.to_numeric(
            all_apts["building:levels"],
            errors="coerce"
        ).fillna(1,inplace=False)
    except KeyError:
        all_apts["floors"] = pd.to_numeric(
            all_apts["properties"].apply(
                lambda x: x.get("building:levels", 1)
            ), errors="coerce"
        ).fillna(1,inplace=False)
    apt_percent = len(all_apts[all_apts["on_major"]].index) / len(all_apts.index)
    apt_floor_percent = (
        all_apts[all_apts["on_major"]]["floors"].sum()
        / all_apts["floors"].sum()
    )
    try:
        all_houses = all_houses[
            all_houses["id"].str.startswith("way")
            | all_houses["id"].str.startswith("relation")
        ]
    except Exception:
        pass
    all_houses["on_major"] = all_houses["id"].isin(maj_houses["id"])
    house_percent = len(all_houses[all_houses["on_major"]].index) / len(all_houses.index)
    return (
        apt_percent, 
        apt_floor_percent,
        house_percent,
        len(all_apts.index),
        all_apts["floors"].sum(),
        len(all_houses.index)
    )

def main(
    state: str = "Oregon",
    city: str = "Portland",
    fetch_all: bool = False,
    replace_data: bool = False
):
    """compare nhoods in the city/state passed"""
    nhood_data_path = fetch_neighborhood_data(city, state)
    nhood_data = gpd.read_file(nhood_data_path)
    nhood_data = nhood_data[nhood_data["type"] != "node"]
    nhood_data["name"] = nhood_data['tags'].apply(lambda x: x.get('name'))
    nhood_data["name_lower"] = nhood_data["name"].str.lower()
    nhoods = [n for n in nhood_data["name"].tolist() if n is not None]
    for nhood in nhoods:
        _d = fetch_housing_location_data(
            nhood,
            city,
            state,
            save=True,
            replace=replace_data,
            run_query=fetch_all,
            return_data=False
        )
        if _d is not None:
            print(f"Fetched data from {nhood} for {city},{state}")
        else:
            print(f"No data found for {nhood} for {city},{state} and fetch_all=False")
            
    data = []
    for nhood in os.listdir(os.path.join(os.path.dirname(__file__), state, city)):
        if ".DS_Store" in nhood:
            continue
        try:
            apt, apt_floor, house, total_apt, total_apt_floors, total_house = relative_major_percents(
                nhood, city, state
            )
        except Exception as e:
            print(f"No data found for {nhood}")
            print(e)
            continue
        p_statement = (
            f"Neighborhood {nhood} has {round(100*apt,2)}% of apartments "
            f"and {round(100*apt_floor,2)}% of apartment floors "
            f"but {round(100*house,2)}% of houses within 30m of major roads."
        )
        print(p_statement)
        data.append(
            {
                "State":state,
                "City":city,
                "Neighborhood":nhood,
                "name_lower":nhood.lower(),
                "Apartment Major Road Percent":apt,
                "Total Apartments":total_apt,
                "Apt Floor Major Road Percent":apt_floor,
                "Total Apt Floors":total_apt_floors,
                "House Major Road Percent":house,
                "Total Houses":total_house
            }
        )
    df = pd.DataFrame(data)
    df = nhood_data.merge(
        df,
        how="inner",
        on="name_lower"
    )
    df = df[
        ["State","City","Neighborhood","Apartment Major Road Percent","Total Apartments",
        "Total Apt Floors","Apt Floor Major Road Percent",
        "House Major Road Percent","Total Houses","geometry"
        ]
    ]
    df[[c for c in df.columns if c != "geometry"]].to_csv(
        os.path.join(os.path.dirname(__file__),"test_csv.csv")
    )
    df.to_file(
        os.path.join(os.path.dirname(__file__),"test_gj.geojson"),
        driver="GeoJSON"
    )

#main(city="madison")
#fetch_housing_location_data("Tenney-Lapham","Madison","Wisconsin")
#p = fetch_neighborhood_data("Portland","Oregon")
#gdf = gpd.read_file(p)
#gdf = gdf[gdf["type"] != "node"]
#print(gdf)
main(fetch_all=False)