import os
from conans import ConanFile
from conans.tools import download, check_sha256, unzip

class Utf8CppConan(ConanFile):
    name = 'utf8-cpp'
    version = '2.3.4'
    description = 'A portable UTF-8 C++ library'
    url = 'https://github.com/jjones646/conan-utf8-cpp'
    settings = None

    def source(self):
        download_url = 'https://github.com/jjones646/utf8-cpp/archive/v{!s}.zip'.format(self.version)
        zip_name = os.path.basename(download_url)
        download(download_url, zip_name)
        check_sha256(zip_name, '450de5cf72fd3162aa191e089cccd0c0a49b95809a00f2993bb5d61b5676d8c1')
        unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        return  # do nothing - header only

    def package(self):
        src_dir = 'utf8-cpp-{!s}'.format(self.version)
        self.copy(pattern='*', src='{!s}/source'.format(src_dir), dst='include/utf8-cpp')

    def package_id(self):
        self.info.requires.clear()
