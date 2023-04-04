def abs_path_from_project(relative_path: str):
    from petstore_api_test import framework
    from pathlib import Path

    return (
        Path(framework.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )


teddy = abs_path_from_project('framework/data/pet_jsons/niffler_0.json')
pumpkin = abs_path_from_project('framework/data/pet_jsons/niffler_1.json')
