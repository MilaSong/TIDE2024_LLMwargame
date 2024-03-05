selected = {
    "attacker": "",
    "target": ""
}


def str_to_unit(unit_str):
    unit_list = unit_str.split("_")
    # air_drone_working_Brest
    if len(unit_list) == 3:
        return {
            "domain": unit_list[0],
            "name": unit_list[1],
            "condition": unit_list[2],
            "location": None
        }
    else:
        return {
            "domain": unit_list[0],
            "name": unit_list[1],
            "condition": unit_list[2],
            "location": unit_list[3]
        }
