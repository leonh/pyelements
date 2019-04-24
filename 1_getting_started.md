# 1 Before We Start...

### Do you have python3.7, git and PyCharm installed? 
www.python.org
https://git-scm.com/downloads
https://www.jetbrains.com/pycharm/download/

* Another editor will do if you are more comfortable with that. If you are starting from scratch PyCharm is a recommended option.

## 2 A Little History...

Python’s origins lie way back in distant December 1989, nearly 30 years ago

Created by **Guido van Rossum** a Dutch computer scientist. AKA The BDFL
(the Python community’s **Benevolent Dictator for Life**)

Last year Guido stepped down from this role. 
We are yet to see the impact that has departure makes on the language.

Python also served a central role in van Rossum’s **Computer Programming for Everybody** initiative. 
The goal was to make programming more accessible to the ‘layman’.
To encourage a basic level of coding literacy along with English literacy and math skills.

Python 2 the first open source version available on sourceforge was introduced in 2000
As the release notes stated,

‘the most important change in Python 2.0 may not be to the code at all, but to how Python is developed’.

Since large number of startup 'unicorns' have used python : youtube, google, airbnb, instagram, dropbox.

Adoption has been also been driven by Django - Popular web framework set a high standard for how a open-source project should be conducted. extensive docs help for new users.

2008 python 3 appeared. The 3 version was a full overhaul with many backwards incompatible features.
Adoption has been slow Only in the last 2 years or so the balance has switched to python3 being the default.


## Characteristics of the Language
* It's not 'better' than Java. Different way to solve problems with its own set of trade-offs.
* Slow
* Though optimised options to exist. (Rewrite portions of code in C++, Cython)
* Open Source. Evolution through PEP's 
* Focus on your solution to a problem and not the requirements of the interpreter
* Mixed functional and object orientated style
* Loose typing - you can add 'type hints' in 3.6+ versions
* Readability (leads to maintainability) via a high level / Declarative style and use of whitespace
* Productivity
* Fun
* There are no locks on the doors in terms of 'public' and 'private'. Agreed conventions instead.
* "A language between consenting adults" - Raymond Hettinger.
* Strong helpful community and ecosystem. 
Recently making big efforts to redress the lack of ethnic and gender diversity among it's community.
* Strong presence in web and data science

## Notable packages on PyPI Python Package index 
flask, django, wagtail, geodjango, ipython, jupyter notebook, requests, click , fabric, ansible, numpy, pandas, boto3 , pillow, PIL

1000's Talks on youtube , anything by **Raymond Hettinger** is recommended
Notes:
https://github.com/leonh/pyelements

python3 -m venv my_env_name

source bin/activate   on mac
\path\to\env\Scripts\activate.bat  on windows cmd

pip install flask
