from setuptools import setup, find_packages

setup(name='babywatcher_server',
      version='0.1.0',
      description='Babywatcher app server',
      author='Kim Desrosiers',
      author_email='kimdesro@gmail.com',
      packages=find_packages(),
      include_package_data = True,
      data_files=[('/etc/babywatcher', ['etc/config.yaml'])],
      entry_points = {
          'console_scripts': ['babywat=babywatcher_server.cli:main'],
      }
      )
