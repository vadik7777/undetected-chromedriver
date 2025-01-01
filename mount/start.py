import re
from os import listdir, system
from os.path import isdir, join

mypath = '/opt/wd/tests/'
for file in (join(mypath, filename) for filename in listdir(mypath)):
    if isdir(file):
        continue
    with open(file, 'r') as f:
        filedata = f.read()
    filedata = filedata.replace('from selenium import webdriver',
                                'import undetected_chromedriver as webdriver\n'
                                'import ssl\n'
                                'ssl._create_default_https_context = ssl._create_unverified_context')
    filedata = filedata.replace('    self.driver = webdriver.Firefox()',
                                '    self.options = webdriver.ChromeOptions()\n'
                                '    self.options.add_argument("--disable-setuid-sandbox")\n'
                                '    self.options.add_argument("--ignore-certificate-errors")\n'
                                '    self.options.add_argument("--ignore-certificate-errors")\n'
                                '    self.driver = webdriver.Chrome(self.options)')
    filedata = filedata.replace(', 0, 0', '')
    with open(file, 'w') as file:
        file.write(filedata)
system('pytest ' + mypath)
