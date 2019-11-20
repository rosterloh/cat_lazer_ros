from setuptools import find_packages
from setuptools import setup

package_name = 'lazerbot_node'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='rosterloh',
    maintainer_email='richard.osterloh@gmail.com',
    keywords=['ROS', 'ROS2', 'rclpy'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='ROS 2 Lazer cat toy',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lazerbot = lazerbot_node.main:main'
        ],
    },
)
