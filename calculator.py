def bush_acre_to_kg_hec(bush_acre, crop):
    """Function to convert bushels per acre to kilograms to hectar
    Parameters are: bush_acre and crop
    bush_acre
        yield in bushels per acre
    crop
        Crop you are working with, the function works with corn, soybean, and sorghum """

    if crop == "corn":
        kg_ha = bush_acre * 62.77
    elif crop == "soybean":
        kg_ha = bush_acre * 67.25
    elif crop == "sorghum":
        kg_ha = bush_acre * 56
    else: 
        print("crop conversion not available")
    return kg_ha
