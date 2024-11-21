import subprocess


def upload_package_to_pypi():
    subprocess.run(['venv/bin/python', '-m', 'twine', 'upload', 'dist/*'])


if __name__ == '__main__':
    upload_package_to_pypi()
