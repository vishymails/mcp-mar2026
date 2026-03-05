from fastmcp import FastMCP

mcp = FastMCP("Wholesale-Inventory")

@mcp.tool()
def check_stock(sku: str) -> str :
    """Check the stock level for a given SKU."""
    # mock database 
    inventory = {
        "SKU-101": 100,
        "SKU-102": 200,
        "SKU-103": 300,
        "SKU-104": 400,
        "SKU-105": 500,
        "SKU-106": 600,
        "SKU-107": 700,
        "SKU-108": 800,
        "SKU-109": 900,
        "SKU-110": 1000,
    }
    count = inventory.get(sku.upper(), "Unknown SKU")
    return f"Inventory for {sku}: {count} units available "


@mcp.tool()
def get_lead_time(zip_code: str) -> str:
    """ Calculates shipping lead time based on zip code."""
    if zip_code.startswith("9"): # west coast
        return "Lead time: 3-5 business days"
    return "Lead time: 5-7 business days"

if __name__ == "__main__":
    print("Inventory server is running on port 9000")
    mcp.run(transport = "streamable-http", host="0.0.0.0", port=9000)


