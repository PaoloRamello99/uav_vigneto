from setuptools import setup, find_packages

package_name = 'uav_vigneto_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(include=[package_name]),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='paolo',
    maintainer_email='paolo@todo.todo',
    description='UAV vigneto package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'navigation = uav_vigneto_pkg.navigation:main',
            'monitor = uav_vigneto_pkg.monitor:main',
            'refill = uav_vigneto_pkg.refill:main',
            'sprayer = uav_vigneto_pkg.sprayer:main',
            'map = uav_vigneto_pkg.map:main',
            'mission_control = uav_vigneto_pkg.mission_control:main',
            'dashboard = uav_vigneto_pkg.dashboard:main',
        ],
    },
)
