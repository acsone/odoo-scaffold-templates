import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo8-addons-acsone-odoo-scaffold-templates",
    description="Meta package for acsone-odoo-scaffold-templates Odoo addons",
    version=version,
    install_requires=[
        'odoo8-addon-acsone-custom-module',
        'odoo8-addon-acsone-oca-module',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 8.0',
    ]
)
