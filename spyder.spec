%define name	spyder
%define version 2.0.3
%define release %mkrel 1

Summary:	Scientific Python Development Environment
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.zip
License:	MIT
Group:		Development/Python
Url:		http://spyderlib.googlecode.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python >= 2.5
Requires:	python-qt4 >= 4.4, python-qt4-qscintilla >= 2.1
Requires:	python-matplotlib-qt4
Suggests:	pylint, python-numpy, python-scipy
Suggests:	ipython, python-rope >= 0.9.2, pyflakes >= 0.3.0
Suggests:	python-matplotlib, pylint
BuildRequires:	python-sphinx
%py_requires -d

%description
Spyder is a Python development environment with tons of features:

* Editor - Multi-language editor with function/class browser, code
  analysis (pyflakes and pylint are currently supported),
  horizontal/verti- cal splitting, etc.

* Documentation viewer - Automatically show documentation (if
  available, or source code otherwise) for any class instantiation or
  function call made in a Python shell (interactive/external console,
  see below).
        
* Interactive console - Python shell with workspace support (variable
  explorer with GUI based editors: dictionary editor, array editor,
  ...) and matplotlib figures integration.

* External console (separate process) - Run Python scripts
  (interactive, debugging or normal mode) or open a Python interpreter
  with variable explorer and documentation viewer support (a basic
  terminal window may also be opened with the external console)

* File/directories explorer
            
* Find in files feature - Supports regular expressions and mercurial
  repositories

* History log

Spyder may also be used as a PyQt4 extension library (module 'spyderlib').
For example, the Python interactive shell widget used in Spyder may be
embedded in your own PyQt4 application.

%prep
%setup -q -n %{name}-%{version}
chmod 600 README

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc README 
%py_sitedir/spyderlib/doc
