import pandas as pd

df = pd.read_csv("ill-flow/data/derived/all_records.csv")

origin_locations = df[df.From == "Dartmouth College"].OriginLocation.unique()
destination_locations = df[df.To == "Dartmouth College"].DestinationLocation.unique()

origin_locations = pd.DataFrame(data={"OriginLocation": origin_locations}).sort_values(
    by="OriginLocation"
)
origin_locations["UnifiedLocation"] = None

destination_locations = pd.DataFrame(
    data={"DestinationLocation": destination_locations}
).sort_values(by="DestinationLocation")
destination_locations["UnifiedLocation"] = None

with pd.ExcelWriter("unify_locations.xlsx") as writer:
    origin_locations.to_excel(writer, sheet_name="OriginLocations", index=None)
    destination_locations.to_excel(
        writer, sheet_name="DestinationLocations", index=None
    )
