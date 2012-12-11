%define name	spyder
%define version 2.1.11
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %rel
%else
%define	release %rel
%endif

Summary:	Scientific Python Development Environment
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://spyderlib.googlecode.com/files/%{name}-%{version}.zip
Source1:	%name.desktop
License:	MIT
Group:		Development/Python
URL:		http://spyderlib.googlecode.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python >= 2.5
Requires:	python-qt4 >= 4.4, python-qt4-qscintilla >= 2.1
Requires:	python-matplotlib-qt4
Suggests:	pylint, python-numpy, python-scipy
Suggests:	ipython, python-rope >= 0.9.2, pyflakes >= 0.3.0
Suggests:	python-matplotlib, pylint
BuildRequires:	python-sphinx >= 0.6.0
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

# adding a launcher

%{__install} -d -m755 %{buildroot}%{_datadir}/applications
%{__install} -d -m755 %{buildroot}%{_datadir}/pixmaps

%{__install} -m644 %SOURCE1 %buildroot%_datadir/applications
%{__install} -m644 spyderlib/images/spyder.svg %buildroot%_datadir/pixmaps


%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc README 
%py_sitedir/spyderlib/doc
%_datadir/applications/*.desktop
%_datadir/pixmaps/*.svg


%changelog
* Tue Jul 31 2012 Lev Givon <lev@mandriva.org> 2.1.11-1
+ Revision: 811504
- Update to 2.1.11.

* Fri Jun 08 2012 Lev Givon <lev@mandriva.org> 2.1.10-1
+ Revision: 803542
- Update to 2.1.10.

  + Cristobal Lopez Silla <tobal@mandriva.org>
    - added a launcher for the program

* Tue Apr 03 2012 Lev Givon <lev@mandriva.org> 2.1.9-1
+ Revision: 788902
- Update to 2.1.9.

* Wed Mar 07 2012 Lev Givon <lev@mandriva.org> 2.1.8-1
+ Revision: 782571
- Update to 2.1.8.

* Sun Jan 15 2012 Lev Givon <lev@mandriva.org> 2.1.7-1
+ Revision: 760894
- Update to 2.1.7.

* Tue Dec 20 2011 Lev Givon <lev@mandriva.org> 2.1.6-1
+ Revision: 743963
- Update to 2.1.6

* Sun Dec 18 2011 Lev Givon <lev@mandriva.org> 2.1.5-1
+ Revision: 743400
- Update to 2.1.5.

* Wed Nov 30 2011 Lev Givon <lev@mandriva.org> 2.1.4-1
+ Revision: 735740
- Update to 2.1.4.

* Mon Nov 28 2011 Lev Givon <lev@mandriva.org> 2.1.3-1
+ Revision: 735142
- Update to 2.1.3.

* Fri Nov 18 2011 Lev Givon <lev@mandriva.org> 2.1.2-1
+ Revision: 731618
- Update to 2.1.2.

* Mon Nov 07 2011 Lev Givon <lev@mandriva.org> 2.1.1-1
+ Revision: 727181
- Update to 2.1.1.

* Thu Nov 03 2011 Lev Givon <lev@mandriva.org> 2.1.0-1
+ Revision: 714294
- Update to 2.1.0.

* Sun Jun 12 2011 Lev Givon <lev@mandriva.org> 2.0.12-1
+ Revision: 684339
- Update to 2.0.12.

* Sun May 01 2011 Lev Givon <lev@mandriva.org> 2.0.11-1
+ Revision: 661302
- Update to 2.0.11.

* Wed Apr 06 2011 Lev Givon <lev@mandriva.org> 2.0.10-1
+ Revision: 651052
- Update to 2.0.10.

* Mon Apr 04 2011 Lev Givon <lev@mandriva.org> 2.0.9-1
+ Revision: 650109
- Update to 2.0.9.

* Sun Feb 27 2011 Lev Givon <lev@mandriva.org> 2.0.8-1
+ Revision: 640670
- Update to 2.0.8.

* Mon Jan 10 2011 Lev Givon <lev@mandriva.org> 2.0.6-1
+ Revision: 630834
- Update to 2.0.6.

* Thu Dec 16 2010 Lev Givon <lev@mandriva.org> 2.0.5-1mdv2011.0
+ Revision: 622222
- Update to 2.0.5.

* Mon Dec 13 2010 Lev Givon <lev@mandriva.org> 2.0.4-1mdv2011.0
+ Revision: 620685
- Update to 2.0.4.

* Tue Dec 07 2010 Lev Givon <lev@mandriva.org> 2.0.3-1mdv2011.0
+ Revision: 614423
- Update to 2.0.3.

* Wed Dec 01 2010 Lev Givon <lev@mandriva.org> 2.0.2-1mdv2011.0
+ Revision: 604554
- Update to 2.0.2.

* Tue Nov 30 2010 Lev Givon <lev@mandriva.org> 2.0.1-1mdv2011.0
+ Revision: 603777
- Update to 2.0.1.

* Tue Nov 30 2010 Lev Givon <lev@mandriva.org> 2.0.0-1mdv2011.0
+ Revision: 603750
- import spyder


