from setuptools import setup, find_packages

setup(
    name="greenmind",
    version="0.1.0",
    author="Oussama Dbibih",
    author_email="oussama.dbibih@viacesi.fr",
    description="GreenMind - Serre intelligente avec Raspberry Pi et ESP32",
    # long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Ossama1999-DEV/GreenMind",
    packages=find_packages(where="."),  # auto-détection des modules Python
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "scikit-learn",
        "paho-mqtt",
        # "opencv-python-headless",  # décommente si vision avec caméra
    ],
    entry_points={
        "console_scripts": [
            "greenmind-train=greenmind.ai.train:main",   # ex: script d'entraînement
            "greenmind-predict=greenmind.ai.predict:main", # ex: script de prédiction
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Home Automation",
    ],
)
