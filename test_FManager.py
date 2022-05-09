import os
import shutil

def filenames():
    result = []
    for item in os.listdir():
        if os.path.isfile(item):
            result.append(item)
    return result

def author_info():
    return 'Leonid Orlov'

def test_filenames():
    assert filenames() == ['account.py',
                            'Console File Manager.py',
                            'main.py',
                            'test_FManager.py',
                            'test_python.py',
                            'victorina.py',
                            'victorina23.py']

def test_author_info():
    assert author_info() == 'Leonid Orlov'

def copy_file_or_directory(name, new_name):
    if os.path.isdir(name):
        shutil.copytree(name, new_name)
    else:
        shutil.copyfile(name, new_name)

def test_copyfile():
    if 'victorina23.py' in os.listdir():
        assert 'victorina23.py' in os.listdir()
    else:
        copy_file_or_directory('victorina.py', 'victorina23.py')
        assert 'victorina23.py' in os.listdir()
