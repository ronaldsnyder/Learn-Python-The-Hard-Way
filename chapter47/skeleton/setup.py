try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
          'description' : 'My Project',
          'author' : 'Ron Snyder',
          'url' : 'complete me',
          'download_url' : 'complete me',
          'author_email' : 'ronalddsnyder@gmail.com',
          'version' : '0.1',
          'install_requires': 'nose',
          'packages' : 'ex47',
          'scripts' : [],
          'name' : 'ex47'
}

setup(**config)