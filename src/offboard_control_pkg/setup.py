from setuptools import setup
import os
from glob import glob

package_name = 'offboard_control_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros',
    maintainer_email='s319891@studenti.polito.it',
    description='PX4 Offboard control for UAV Vigneto',
    license='BSD',
    entry_points={
        'console_scripts': [
            'offboard_control = offboard_control_pkg.offboard_control:main',
        ],
    },
)
