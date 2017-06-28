from conan.packager import ConanMultiPackager
import os

os.environ['CONAN_USERNAME'] = os.getenv('CONAN_USERNAME', 'jjones646')
os.environ['CONAN_CHANNEL'] = os.getenv('CONAN_CHANNEL', 'stable')

if __name__ == '__main__':
    builder = ConanMultiPackager(
        gcc_versions=['5.2', '5.3', '5.4', '6.2', '6.3'],
        apple_clang_versions=['6.1', '7.0', '7.3', '8.0'],
        visual_versions=['14'],
        archs=['x86_64', 'x86'],
        reference='utf8/2.3.4',
    )
    builder.add_common_builds(pure_c=False)
    builder.run()
