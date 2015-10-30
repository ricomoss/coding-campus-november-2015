# Coding Campus
Prepared to support the presentation given to the Coding Campus students on November 18th, 2015.


Installation
============

To begin, you can clone this repository and following the instructions below to setup everything to run correctly.

Linux Installation (Debian/Ubuntu)
----------------------------------

**Please Note**:

- The following will assume you are cloning the sourcecode to ~/Projects/coding-campus-november-2015.  If you are cloning to a different location, you will need to adjust these instructions accordingly.

- A dollar sign ($) indicates a terminal prompt, as your user, not root.

1.  Clone the source::

        $ cd ~/Projects
        $ git clone git@github.com:ricomoss/coding-campus-november-2015.git

2. Install some required packages::

        $ sudo apt-get install python3 python3-dev python-pip

3.  Install virtualenv and virtualenvwrapper::

        $ pip install virtualenv
        $ pip install virtualenvwrapper

4.  Add the following to your **~/.bashrc** or **~/.zshrc** file::

        source /usr/local/bin/virtualenvwrapper.sh

5.  Type the following::

        $ source /usr/local/bin/virtualenvwrapper.sh

6.  Create your virtualenv (for Python 3)::

        $ mkvirtualenv coding_campus -p /usr/bin/python3


7.  Activate the virtualenv::

        $ workon coding_campus

8.  Install the required Python libraries (ensure you're within the new virtual environment).::

        (coding_campus)$ pip install -r ~/Projects/coding-campus-november-2015/requirements.pip


OSX Installation
----------------

**Please Note**:

- The following will assume you are cloning the sourcecode to ~/Projects/coding-campus-november-2015.  If you are cloning to a different location, you will need to adjust these instructions accordingly.

- A dollar sign ($) indicates a terminal prompt, as your user, not root.

1.  Clone the source::

        $ cd ~/Projects
        $ git clone git@github.com:ricomoss/coding-campus-november-2015.git

2.  Install Xcode if you don't have it already.  You can find it in the Apple store.  Install the Command Line Tools of Xcode.::

        $ xcode-select --install

3.  Install Homebrew.::

        $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

4.  Add Homebrew to your `PATH`.  Do this by modifying your `rc` file (`bashrc`, `zshrc`, etc).  You'll need to source this file before the changes will take effect.::

        export PATH=/usr/local/bin:$PATH

5.  Install Python 3.  This example will work with Python 2.7 - but Python 3 is cooler!::

        $ brew install python3

6.  Install virtualenvwrapper::

        $ pip3 install virtualenv
        $ pip3 install virtualenvwrapper

7.  Run `virtualenv-burrito` to help setup your virtual environment without the normal MAC issues.::

        $ curl -sL https://raw.githubusercontent.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL

8.  Create your virtualenv (for Python 3)::

        $ mkvirtualenv coding_campus -p /usr/local/bin/python3

9.  Activate the virtualenv::

        $ workon coding_campus

10.  Install the required Python libraries (ensure you're within the new virtual environment).::

        (coding_campus)$ pip3 install -r ~Projects/coding-campus-november-2015/requirements.pip
