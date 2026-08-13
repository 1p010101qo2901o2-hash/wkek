from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class PygameCERecipe(CompiledComponentsPythonRecipe):
    version = "2.5.2"
    url = (
        "https://github.com/pygame-community/pygame-ce/"
        "archive/refs/tags/{version}.tar.gz"
    )

    name = "pygame-ce"
    site_packages_name = "pygame-ce"

    depends = [
        "sdl2",
        "sdl2_image",
        "sdl2_mixer",
        "sdl2_ttf",
        "setuptools",
        "jpeg",
        "png",
    ]

    call_hostpython_via_targetpython = False


recipe = PygameCERecipe()
