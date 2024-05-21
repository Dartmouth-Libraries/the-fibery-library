import pandas as pd

from pathlib import Path


class DefaultDict(dict):
    def __missing__(self, key):
        return key


def ingest_bd(file: Path) -> pd.DataFrame:
    """Read a file containing Borrow Direct records

    :param file: Path to the file
    :type file: Path
    :return: Records contained in the file
    :rtype: pd.DataFrame
    """
    df = pd.read_excel(file)
    if "borrowed" in file.name:
        partner_col = "Lender"
        direction = "Borrowed"
    else:
        partner_col = "Borrower"
        direction = "Lent"
    incomplete_status = ["REQ_UNFILLED", "REQ_END_OF_ROTA", "REQ_CANCELLED"]
    df = df[~df["Borrower status"].isin(incomplete_status)]
    df = df[~df["Lender status"].isin(incomplete_status)]
    df = df[
        [
            partner_col,
            "Pick location",
            "Pickup location",
            "Date created",
            "Local Library Call Number",
        ]
    ]

    df["Pickup location"] = df["Pickup location"].map(DARTMOUTH_LIBRARIES)

    df = df.rename(
        columns={
            partner_col: "Partner",
            "Shelving location": "Location",
            "Date created": "Date",
        }
    )
    df["Direction"] = direction
    df["System"] = "BorrowDirect"
    df["Type"] = "Non-article"
    return df


def ingest_ill(file: Path) -> pd.DataFrame:
    """Read a file containing Interlibrary Loan records

    :param file: Path to the file
    :type file: Path
    :return: Records contained in the file
    :rtype: pd.DataFrame
    """
    df = pd.read_excel(file)
    if "borrowed" in file.name:
        partner_col = "Lending Library"
        direction = "Borrowed"
    else:
        partner_col = "Lending Library"
        direction = "Lent"
    incomplete_status = ["Cancelled by ILL Staff"]
    df = df[~df["Transaction Status"].isin(incomplete_status)]
    df = df[
        [
            "Lending Library",
            "Location",
            "Creation Date",
            "Document Type",
            "Library Name",
            "Call Number",
        ]
    ]
    df = df.rename(
        columns={
            partner_col: "Partner",
            "Location": "Location",
            "Creation Date": "Date",
            "Document Type": "Type",
        }
    )
    df["Direction"] = direction
    if "rapid" in file.name:
        df["System"] = "RAPID"
        df["Type"] = "Article"
    else:
        df["System"] = "ILL"

    m = DefaultDict(
        CGU="University of Chicago",
        COO="Cornell University",
        HUL="Harvard University",
        JHE="Johns Hopkins University",
        MYG="Massachusetts Institute of Technology",
        NDD="Duke University",
        PAU="University of Pennsylvania",
        PUL="Princeton University",
        RBN="Brown University",
        ST2="Stanford University",
        STF="Stanford University",
        YUS="Yale University",
        ZCU="Columbia University Libraries",
    )

    df.Partner = df.Partner.str.replace("RAPID:", "")
    df.Partner = df.Partner.map(m)
    df = df.dropna(subset="Partner")

    return df


def get_data() -> pd.DataFrame:
    """Helper function to read all data files
    :return: All records
    :rtype: pd.DataFrame
    """
    files = Path("../data/").glob("*.xlsx")

    dfs = []
    for file in files:
        if file.name.startswith("borrow_direct"):
            df = ingest_bd(file)
            dfs.append(df)
        if file.name.startswith("ill"):
            df = ingest_ill(file)
            dfs.append(df)

    df = pd.concat(dfs, axis=0)

    return df


IVY_COLORS = {
    "Harvard University": "#A51C30",
    "Massachusetts Institute of Technology": "#750014",
    "Yale University": "#00356B",
    "University of Pennsylvania": "#990000",
    "Johns Hopkins University": "#002D72",
    "Columbia University Libraries": "#012169",
    "University of Chicago": "#800000",
    "Cornell University": "#B31B1B",
    "Duke University": "#012169",
    "Princeton University": "#E77500",
    "Brown University": "#4E3629",
    "Stanford University": "#8C1515",
    "Dartmouth College": "#00693e",
}

DARTMOUTH_LIBRARIES = DefaultDict(
    {
        "DART_BAKER": "Baker-Berry",
        "DART_DANA": "Dana",
        "DART_MFHSL": "Matthews-Fuller",
        "DART_FELDBERG": "Feldberg",
    }
)
