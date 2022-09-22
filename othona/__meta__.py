# `name` is the name of the package as used for `pip install package`
name = "othona"
# `path` is the name of the package for `import package`
path = name.lower().replace("-", "_").replace(" ", "_")
# Your version number should follow https://python.org/dev/peps/pep-0440 and
# https://semver.org
version = "2022.9.dev0"
author = "Tom Farley"
author_email = "farleytpm@gmail.com"
description = "Python tools for the Othona Community"  # One-liner
url = ""  # your project homepage
license = "MIT"  # See https://choosealicense.com
