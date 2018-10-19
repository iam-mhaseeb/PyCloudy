import  io
from setuptools import setup

with io.open('README.md', encoding='utf_8') as fp:
    readme = fp.read()

setup(name='pywordcloud',
      version='1.0',
      description='A happy light weight word cloud generator in Python',
      long_description=readme,
      long_description_content_type='text/markdown',
      classifiers=[
        'Programming Language :: Python :: 3.6',
      ],
      keywords='wordcloud textprocessing',
      url='https://github.com/iam-mhaseeb/py_word_cloud',
      author='Muhammad Haseeb',
      author_email='haseeb.emailbox@gmail.com',
      license='MIT',
      packages=['pywordcloud'],
      install_requires=[
          'nltk', 'pillow'
      ],
      data_files=[('static', [
          'pywordcloud/font.ttf', 'pywordcloud/stop_words_list.txt'])],
      zip_safe=False,
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      )

