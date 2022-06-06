from setuptools import setup, find_namespace_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# workaround a bug introduced by pyproject.toml
# https://github.com/pypa/pip/issues/7953#issuecomment-645133255
import site; site.ENABLE_USER_SITE = True

setup(
  name='spinalcordtoolbox-data-${dataset_name}',
  version="dev",
  description='Part of https://github.com/neuropoly/spinalcordtoolbox',
  long_description=(here / 'README.md').read_text(encoding='utf-8'),
  long_description_content_type='text/markdown',
  author='Neuropoly',
  author_email='pip@neuropoly.org',
  url='https://spinalcordtoolbox.com/',
  project_urls={
      'Source': 'https://github.com/spinalcordtoolbox/data-${dataset_name}',
      'Documentation': 'https://spinalcordtoolbox.com/',
  },
  license='CC-BY-4.0',
  license_files=[ 'LICENSE.txt' ], # TODO?

  packages=find_namespace_packages('src/'),
  package_dir={"":"src/"},

  # with setuptools_scm, means it includes non-python files if they're under git
  include_package_data=True,

  # pyproject.toml::build-system.requires is supposed to supersede this, but it's still very new so we duplicate it.
  setup_requires=[
    'setuptools',
    'wheel',
  ],

  zip_safe=False, # guarantees that importlib.resources.path() is safe
)

