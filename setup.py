from distutils.core import setup

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(
  name = 'timewatch',
  packages = ['timewatch'], # this must be the same as the name above
  version = '0.5.1',
  description = 'A library automating worktime reports for timewatch.co.il',
  author = 'Nir Izraeli',
  author_email = 'nirizr@gmail.com',
  url = 'https://github.com/nirizr/timewatch', # use the URL to the github repo
  download_url = 'https://github.com/nirizr/timewatch/tarball/0.5.1', # I'll explain this in a second
  keywords = ['timewatch', 'timewatch.co.il'], # arbitrary keywords
  install_requires = requirements,
  classifiers = [],
)