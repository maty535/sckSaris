import xml.etree.ElementTree as ET
import math

def gpx_to_kml_tour(gpx_filename, kml_filename, tour_name="Automaticky prelet"):
    # Registrovanie Google Earth menných priestorov (namespaces)
    ET.register_namespace('', "http://www.opengis.net/kml/2.2")
    ET.register_namespace('gx', "http://www.google.com/kml/ext/2.2")
    
    # Načítanie GPX súboru
    try:
        tree = ET.parse(gpx_filename)
        root = tree.getroot()
    except Exception as e:
        print(f"Chyba pri načítaní GPX súboru: {e}")
        return

    # Definícia namespaces pre vyhľadávanie v GPX
    # Často sa líšia podľa verzie GPX, toto pokrýva najbežnejšie verzie
    namespaces = {
        'gpx': root.tag.split('}')[0].strip('{') if '}' in root.tag else ''
    }
    ns_prefix = f"{{{namespaces['gpx']}}}" if namespaces['gpx'] else ''

    # Extrakcia trackpointov (bodov trasy)
    points = []
    for trkpt in root.findall(f'.//{ns_prefix}trkpt'):
        lat = trkpt.get('lat')
        lon = trkpt.get('lon')
        
        # Pokus o vytiahnutie nadmorskej výšky (ele), ak chýba, dáme 0
        ele_elem = trkpt.find(f'{ns_prefix}ele')
        ele = ele_elem.text if ele_elem is not None else "0"
        
        if lat and lon:
            points.append((lon, lat, ele))

    if not points:
        print("V GPX súbore sa nenašli žiadne body (trkpt).")
        return

    print(f"Načítaných {len(points)} bodov. Generujem KML Tour...")

    # Nastavenia kamery (môžete upraviť podľa potreby)
    altitude = 200      # Výška kamery nad zemou v metroch
    tilt = 65           # Sklon kamery (60-70° dáva pekný 3D efekt)
    duration = 0.5      # Čas v sekundách medzi jednotlivými bodmi (určuje rýchlosť)

    # Budovanie KML štruktúry
    kml = ET.Element('kml', {
        'xmlns': "http://www.opengis.net/kml/2.2",
        'xmlns:gx': "http://www.google.com/kml/ext/2.2"
    })
    
    document = ET.SubElement(kml, 'Document')
    doc_name = ET.SubElement(document, 'name')
    doc_name.text = tour_name

    # 1. Časť: Vytvorenie samotnej Tour (Preletu)
    gx_tour = ET.SubElement(document, '{http://www.google.com/kml/ext/2.2}Tour')
    tour_name_elem = ET.SubElement(gx_tour, 'name')
    tour_name_elem.text = "Spustit prelet po trase"
    
    gx_playlist = ET.SubElement(gx_tour, '{http://www.google.com/kml/ext/2.2}Playlist')

    # Výpočet azimutu (heading) medzi bodmi, aby sa kamera natáčala v smere jazdy
    for i in range(len(points)):
        lon, lat, ele = points[i]
        
        if i < len(points) - 1:
            next_lon, next_lat, _ = points[i+1]
            # Jednoduchý výpočet azimutu medzi dvoma bodmi
            try:
                d_lon = math.radians(float(next_lon) - float(lon))
                lat1 = math.radians(float(lat))
                lat2 = math.radians(float(next_lat))
                y = math.sin(d_lon) * math.cos(lat2)
                x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(d_lon)
                heading = (math.degrees(math.atan2(y, x)) + 360) % 360
            except:
                heading = 0
        else:
            # Posledný bod prevezme azimut z predchádzajúceho
            heading = heading if 'heading' in locals() else 0

        # Pridanie bodu do playlistu preletu
        gx_flyto = ET.SubElement(gx_playlist, '{http://www.google.com/kml/ext/2.2}FlyTo')
        gx_duration = ET.SubElement(gx_flyto, '{http://www.google.com/kml/ext/2.2}duration')
        gx_duration.text = str(duration)
        
        # Prvý bod inicializujeme plynule (smooth), ostatné tiež
        gx_flyto_mode = ET.SubElement(gx_flyto, '{http://www.google.com/kml/ext/2.2}flyToMode')
        gx_flyto_mode.text = "smooth"

        camera = ET.SubElement(gx_flyto, 'Camera')
        ET.SubElement(camera, 'longitude').text = lon
        ET.SubElement(camera, 'latitude').text = lat
        ET.SubElement(camera, 'altitude').text = str(float(ele) + altitude)
        ET.SubElement(camera, 'heading').text = str(heading)
        ET.SubElement(camera, 'tilt').text = str(tilt)
        ET.SubElement(camera, 'roll').text = "0"
        ET.SubElement(camera, 'altitudeMode').text = "absolute"

    # 2. Časť: Vykreslenie samotnej čiary (aby bola trasa na mape aj viditeľná)
    placemark = ET.SubElement(document, 'Placemark')
    pm_name = ET.SubElement(placemark, 'name')
    pm_name.text = "Vizualna trasa"
    
    # Štýl čiary (červená farba, hrúbka 4)
    style = ET.SubElement(placemark, 'Style')
    line_style = ET.SubElement(style, 'LineStyle')
    ET.SubElement(line_style, 'color').text = "ff0000ff" 
    ET.SubElement(line_style, 'width').text = "4"

    line_string = ET.SubElement(placemark, 'LineString')
    ET.SubElement(line_string, 'tessellate').text = "1"
    ET.SubElement(line_string, 'altitudeMode').text = "clampToGround"
    
    coordinates = ET.SubElement(line_string, 'coordinates')
    coord_text = "\n".join([f"{p[0]},{p[1]},{p[2]}" for p in points])
    coordinates.text = coord_text

    # Uloženie do súboru
    kml_tree = ET.ElementTree(kml)
    kml_tree.write(kml_filename, encoding='utf-8', xml_declaration=True)
    print(f"Súbor úspešne uložený ako: {kml_filename}")

# --- Spustenie skriptu ---
if __name__ == "__main__":
    # Sem zadajte názov vášho gpx súboru
    vstupny_gpx = "2026-05-10-Zraz-Trasa1.gpx" 
    vystupny_kml = "2026-05-10-Zraz-Trasa1-tour.kml"
    
    gpx_to_kml_tour(vstupny_gpx, vystupny_kml)