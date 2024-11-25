from setuptools import setup, find_packages

setup(
    name='kraken-trading-bot',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==2.0.1',
        'Werkzeug==2.0.1',
        'gunicorn==20.1.0',
        'python-dotenv==0.19.0'
    ]
)
