Title: How to update GenomeDepot from Python 3.10 to Python 3.12
Date: 2026-05-08 17:32
Modified: 2026-05-08 17:32
Tags: genomedepot, Python
Category: Python
Slug: genomedepotupdate
Authors: aekazakov
Summary: GenomeDepot update to python 3.12

1. Delete (or rename) old virtual environment directory and create a new environment. 

2. Upgrade Python libraries

```
pip install --upgrade PyMySQL toyplot "django-q2==1.10.0" "biopython==1.87" "django==6.0.5" "django-admin-shortcuts==3.0.1" "django-cors-headers==4.9.0" "django-debug-toolbar==6.3.0" "openpyxl==3.1.5" "pandas==3.0.2" "plotly==6.7.0" "setuptools==82.0.1" "numpy==2.4.4"

```

Important! Do not upgrade parasail and toyplot libraries.

3. Delete Jbrowse folder (in the external_tools folder) and re-install it:

```
curl -L -O https://github.com/GMOD/jbrowse/releases/download/1.16.11-release/JBrowse-1.16.11.zip
unzip JBrowse-1.16.11.zip
mv JBrowse-1.16.11 jbrowse
rm JBrowse-1.16.11.zip
cd jbrowse
./setup.sh
```

4. Activate the virtual environment, go to the genomebrowser folder and run:

```
git pull
python manage.py migrate
python manage.py collectstatic
```

5. Restart the web server

```
sudo systemctl restart apache2
```

6. For Ubuntu users. If Python was upgraded with an OS upgrade, check the muscle version. If muscle v.5 was installed, replace it with muscle version 3.8 from <https://drive5.com/muscle/downloads_v3.htm>. 

```
cd /usr/bin
sudo mv muscle muscle5
sudo ln -s muscle3.8.31_i86linux64 muscle
```
