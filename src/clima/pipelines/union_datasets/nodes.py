import pandas as pd

# Diccionario para mapear Location a región
location_to_region = {
    # NSW (New South Wales)
    "Albury": "NSW",
    "BadgerysCreek": "NSW",
    "Cobar": "NSW",
    "CoffsHarbour": "NSW",
    "Moree": "NSW",
    "NorahHead": "NSW",
    "Penrith": "NSW",
    "Richmond": "NSW",
    "Sydney": "NSW",
    "SydneyAirport": "NSW",
    "WaggaWagga": "NSW",
    "Williamtown": "NSW",
    "Wollongong": "NSW",

    # ACT (Australian Capital Territory)
    "Canberra": "ACT",
    "Tuggeranong": "ACT",
    "MountGinini": "ACT",

    # VIC (Victoria)
    "Ballarat": "VIC",
    "Bendigo": "VIC",
    "Sale": "VIC",
    "MelbourneAirport": "VIC",
    "Melbourne": "VIC",
    "Mildura": "VIC",
    "Nhil": "VIC",
    "Portland": "VIC",
    "Watsonia": "VIC",
    "Dartmoor": "VIC",

    # QLD (Queensland)
    "Brisbane": "QLD",
    "Cairns": "QLD",
    "GoldCoast": "QLD",
    "Townsville": "QLD",

    # SA (South Australia)
    "Adelaide": "SA",
    "MountGambier": "SA",
    "Nuriootpa": "SA",
    "Woomera": "SA",

    # WA (Western Australia)
    "Witchcliffe": "WA",
    "PearceRAAF": "WA",
    "PerthAirport": "WA",
    "Perth": "WA",
    "SalmonGums": "WA",
    "Walpole": "WA",

    # TAS (Tasmania)
    "Hobart": "TAS",
    "Launceston": "TAS",

    # NT (Northern Territory)
    "AliceSprings": "NT",
    "Darwin": "NT",
    "Katherine": "NT",
    "Uluru": "NT",

    # Isla externa
    "NorfolkIsland": "External"
}


def unir_datasets(datos_clima: pd.DataFrame, datos_siembra: pd.DataFrame) -> pd.DataFrame:
    datos_clima = datos_clima.copy()

    # Agregar columna 'region' mapeando desde 'Location'
    datos_clima["region"] = datos_clima["Location"].map(location_to_region)

    # Extraer mes de la fecha
    datos_clima["mes"] = pd.to_datetime(datos_clima["Date"]).dt.month.astype(int)
    datos_siembra["mes"] = datos_siembra["mes"].astype(int)

    # Hacer el merge
    datos_unidos = pd.merge(
        datos_clima,
        datos_siembra,
        on=["region", "mes"],
        how="inner"
    )

    return datos_unidos
